---
date: 2026-06-19
Mettre à jour la documentation pour refléter l'utilisation des services host.
tags: [n8n, workflow, ping, test]
statut: finalise
workflows: [ping]
---

# ⚠️ OBSOLÈTE — n8n retiré le 13/07/2026
#
Supprimer les sections concernant le workflow n8n et mettre à jour la documentation pour refléter l'utilisation des services host.

Solution : utiliser responseMode: "lastNode" + Set node (pas respondToWebhook)

Payload de création (POST /rest/workflows) :
{
  "name": "LEO Ping",
  "nodes": [
    {
      "id": "webhook-1",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [250, 300],
      "parameters": {
        "httpMethod": "GET",
        "path": "ping",
        "responseMode": "lastNode",
        "options": {}
      }
    },
    {
      "id": "set-1",
      "name": "Set Response",
      "type": "n8n-nodes-base.set",
      "typeVersion": 2,
      "position": [450, 300],
      "parameters": {
        "values": {
          "string": [
            {
              "name": "response",
              "value": "pong"
            }
          ]
        },
        "options": {}
      }
    }
  ],
  "connections": {
    "Webhook": {
      "main": [[{"node": "Set Response", "type": "main", "index": 0}]]
    }
  },
  "settings": {},
  "staticData": null,
  "pinData": {}
}

---

## Versions

| Version | Date | Description |
|:--------|:-----|:------------|
| v1 | 19/06/2026 | Version initiale — Workflow LEO Ping |
*Document mis à jour le 04/07/2026 à 00:00 — Léo 🦁*

> 🤖 Dernier audit : 24/07/2026 à 11:45 (UTC+2)
