#!/usr/bin/env python3
"""collect-n8n.py — Lit la DB n8n et génère un JSON de monitoring."""
import sqlite3, json, os, subprocess
from datetime import datetime, timezone

DB_PATH = "/var/lib/docker/volumes/n8n_data/_data/database.sqlite"
OUTPUT = os.path.expanduser("~/.hermes/metrics/n8n.json")

def collect():
    # Copier la DB en local (permissions)
    tmp = "/tmp/n8n_collect.sqlite"
    subprocess.run(["sudo", "cp", DB_PATH, tmp], check=True, capture_output=True)
    subprocess.run(["sudo", "chmod", "644", tmp], check=True, capture_output=True)
    
    conn = sqlite3.connect(tmp)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    
    # Workflows
    c.execute("SELECT id, name, active, updatedAt FROM workflow_entity")
    workflows = []
    for row in c.fetchall():
        wf = dict(row)
        wf_id = wf["id"]
        
        # Dernières exécutions
        c.execute("""
            SELECT status, startedAt, stoppedAt 
            FROM execution_entity 
            WHERE workflowId=? 
            ORDER BY startedAt DESC LIMIT 5
        """, (wf_id,))
        execs = []
        for e in c.fetchall():
            execs.append({
                "status": e["status"],
                "started": e["startedAt"],
                "stopped": e["stoppedAt"]
            })
        
        # Stats
        c.execute("SELECT COUNT(*) FROM execution_entity WHERE workflowId=? AND status='success'", (wf_id,))
        ok = c.fetchone()[0]
        c.execute("SELECT COUNT(*) FROM execution_entity WHERE workflowId=? AND status='error'", (wf_id,))
        err = c.fetchone()[0]
        c.execute("SELECT COUNT(*) FROM execution_entity WHERE workflowId=?", (wf_id,))
        total = c.fetchone()[0]
        
        wf["executions"] = execs
        wf["stats"] = {"success": ok, "error": err, "total": total}
        wf["health"] = "ok" if err == 0 else ("warning" if err <= 2 else "error")
        workflows.append(wf)
    
    conn.close()
    
    result = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "workflows": workflows,
        "total": len(workflows),
        "active": sum(1 for w in workflows if w["active"]),
        "errors": sum(w["stats"]["error"] for w in workflows),
        "all_ok": all(w["health"] == "ok" for w in workflows if w["active"])
    }
    
    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    with open(OUTPUT, "w") as f:
        json.dump(result, f, indent=2, default=str)
    
    print(f"✅ {result['total']} workflows ({result['active']} actifs) — {result['errors']} erreurs")
    return result

if __name__ == "__main__":
    collect()
