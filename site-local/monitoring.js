// Monitoring temps réel LEO
var monInterval = null;
var monChart = null;
var monHistory = { labels: [], cpu: [], ram: [], disk: [], temp: [] };
var MAX_HISTORY = 30;

function startMonitoring() {
  if (monInterval) return;
  // Wait for panel to be visible before initializing canvases
  setTimeout(function() {
    fetchMonitoring();
    monInterval = setInterval(fetchMonitoring, 10000);
  }, 200);
}

function stopMonitoring() {
  if (monInterval) { clearInterval(monInterval); monInterval = null; }
  if (monChart) { monChart.destroy(); monChart = null; }
}

function fetchMonitoring() {
  fetch('/api/machine-kpi')
    .then(function(r) { return r.json(); })
    .then(function(d) {
      var now = new Date().toLocaleTimeString('fr-BE', {hour:'2-digit',minute:'2-digit',second:'2-digit'});

      // CPU
      var cpuPct = Math.round((d.cpu ? d.cpu.load1 : 0) * 100);
      var cpuEl = document.getElementById('mon-cpu-val');
      if (cpuEl) cpuEl.textContent = cpuPct + '%';
      var cpuDet = document.getElementById('mon-cpu-detail');
      if (cpuDet) cpuDet.textContent = 'Load ' + (d.cpu?d.cpu.load1:'-') + ' | ' + (d.cpu?d.cpu.cores:'?') + ' cores';
      drawGauge('mon-cpu-gauge', cpuPct);

      // RAM (fix comma)
      var ram = d.ram || {};
      var ramUsed = parseFloat((ram.used||'0').replace(',','.')) || 0;
      var ramTotal = parseFloat((ram.total||'1').replace(',','.')) || 1;
      var ramPct = Math.round(ramUsed / ramTotal * 100);
      var ramEl = document.getElementById('mon-ram-val');
      if (ramEl) ramEl.textContent = ramPct + '%';
      var ramDet = document.getElementById('mon-ram-detail');
      if (ramDet) ramDet.textContent = (ram.used||'-') + ' / ' + (ram.total||'-') + ' (dispo: ' + (ram.avail||'-') + ')';
      drawGauge('mon-ram-gauge', ramPct);

      // Disk
      var diskParts = (d.disk||'').split(' ');
      var diskPct = parseInt(diskParts[3]) || 0;
      var diskEl = document.getElementById('mon-disk-val');
      if (diskEl) diskEl.textContent = diskPct + '%';
      var diskDet = document.getElementById('mon-disk-detail');
      if (diskDet) diskDet.textContent = 'Utilise: ' + (diskParts[1]||'-') + ' / ' + (diskParts[0]||'-');
      drawGauge('mon-disk-gauge', diskPct);

      // Temp
      var temp = d.cpu ? d.cpu.temp : '-';
      var tempN = parseFloat(temp) || 0;
      var tempEl = document.getElementById('mon-temp-val');
      if (tempEl) {
        tempEl.textContent = temp + '°C';
        tempEl.style.color = tempN > 75 ? '#f87171' : tempN > 60 ? '#fbbf24' : '#34d399';
      }

      // Services
      var svc = d.services || {};
      var svcHtml = '';
      for (var k in svc) {
        var cls = svc[k] === 'UP' ? 'up' : 'down';
        svcHtml += '<div class="mon-svc"><span>' + k + '</span><span class="badge ' + cls + '">' + svc[k] + '</span></div>';
      }
      var svcDiv = document.getElementById('mon-services');
      if (svcDiv) svcDiv.innerHTML = svcHtml;

      // History
      monHistory.labels.push(now);
      monHistory.cpu.push(cpuPct);
      monHistory.ram.push(ramPct);
      monHistory.disk.push(diskPct);
      monHistory.temp.push(tempN);
      if (monHistory.labels.length > MAX_HISTORY) {
        monHistory.labels.shift();
        monHistory.cpu.shift();
        monHistory.ram.shift();
        monHistory.disk.shift();
        monHistory.temp.shift();
      }
      drawHistoryChart();

      var upd = document.getElementById('mon-updated');
      if (upd) upd.textContent = 'Mis a jour: ' + now;
    })
    .catch(function(e) {
      var upd = document.getElementById('mon-updated');
      if (upd) upd.textContent = 'Erreur: ' + e.message;
    });
}

function drawGauge(id, pct) {
  var c = document.getElementById(id);
  if (!c) return;
  // Ensure canvas has proper size
  var parent = c.parentElement;
  if (parent && parent.offsetWidth > 0) {
    c.width = Math.min(parent.offsetWidth, 120);
    c.height = c.width;
  }
  if (c.width === 0 || c.height === 0) {
    c.width = 100;
    c.height = 100;
  }
  var ctx = c.getContext('2d');
  var w = c.width, h = c.height;
  ctx.clearRect(0, 0, w, h);
  var cx = w/2, cy = h/2, r = Math.min(cx, cy) - 10;
  var start = 0.75 * Math.PI, end = 2.25 * Math.PI;
  var angle = start + (pct / 100) * (end - start);

  // Background
  ctx.beginPath();
  ctx.arc(cx, cy, r, start, end);
  ctx.strokeStyle = '#334155';
  ctx.lineWidth = 10;
  ctx.stroke();

  // Value
  var color = pct > 85 ? '#f87171' : pct > 60 ? '#fbbf24' : '#34d399';
  ctx.beginPath();
  ctx.arc(cx, cy, r, start, angle);
  ctx.strokeStyle = color;
  ctx.lineWidth = 10;
  ctx.lineCap = 'round';
  ctx.stroke();

  // Text
  ctx.fillStyle = '#e2e8f0';
  ctx.font = 'bold 18px system-ui, sans-serif';
  ctx.textAlign = 'center';
  ctx.textBaseline = 'middle';
  ctx.fillText(pct + '%', cx, cy);
}

function drawHistoryChart() {
  var ctx = document.getElementById('mon-history-chart');
  if (!ctx) return;

  var isDark = document.documentElement.getAttribute('data-theme') !== 'light';
  var gridColor = isDark ? '#334155' : '#e2e8f0';
  var textColor = isDark ? '#94a3b8' : '#64748b';

  if (monChart) {
    monChart.data.labels = monHistory.labels;
    monChart.data.datasets[0].data = monHistory.cpu;
    monChart.data.datasets[1].data = monHistory.ram;
    monChart.data.datasets[2].data = monHistory.disk;
    monChart.data.datasets[3].data = monHistory.temp;
    monChart.update('none');
    return;
  }

  // Ensure canvas has size
  var container = ctx.parentElement;
  if (container && container.offsetWidth > 0) {
    ctx.style.height = '250px';
  }

  monChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: monHistory.labels,
      datasets: [
        { label: 'CPU %', data: monHistory.cpu, borderColor: '#f87171', tension: 0.3, pointRadius: 0, borderWidth: 2 },
        { label: 'RAM %', data: monHistory.ram, borderColor: '#60a5fa', tension: 0.3, pointRadius: 0, borderWidth: 2 },
        { label: 'Disque %', data: monHistory.disk, borderColor: '#34d399', tension: 0.3, pointRadius: 0, borderWidth: 1, borderDash: [4,2] },
        { label: 'Temp °C', data: monHistory.temp, borderColor: '#fbbf24', tension: 0.3, pointRadius: 0, borderWidth: 1.5, yAxisID: 'y1' }
      ]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      animation: { duration: 300 },
      plugins: {
        legend: {
          labels: { color: textColor, font: { size: 10 }, boxWidth: 12, padding: 8 } }
      },
      scales: {
        x: {
          ticks: { color: textColor, font: { size: 9 }, maxTicksLimit: 8, maxRotation: 0 },
          grid: { color: gridColor }
        },
        y: {
          beginAtZero: true,
          max: 100,
          ticks: { color: textColor, font: { size: 9 }, callback: function(v) { return v + '%'; } },
          grid: { color: gridColor }
        },
        y1: {
          position: 'right',
          beginAtZero: true,
          max: 100,
          ticks: { color: '#fbbf24', font: { size: 9 }, callback: function(v) { return v + '°C'; } },
          grid: { display: false }
        }
      }
    }
  });
}
