"""
J.A.R.V.I.S. Senior Design AI Assistant — 100% Self-Contained Cloud Deployment
Zero missing template or missing folder errors on Render / Vercel.
"""

import os
import sys
import json
import re
from flask import Flask, request, jsonify, render_template_string
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Embedded Stark Industries HUD HTML Template
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>J.A.R.V.I.S. // Senior Design Tactical HUD</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;600;700;800;900&family=Rajdhani:wght@500;600;700&family=Share+Tech+Mono&display=swap" rel="stylesheet">
  <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
  <style>
    :root {
      --bg-dark: #020712;
      --arc-cyan: #00f0ff;
      --arc-blue: #0077ff;
      --arc-glow: rgba(0, 240, 255, 0.45);
      --arc-glow-intense: rgba(0, 240, 255, 0.85);
      --hud-panel-bg: rgba(4, 16, 35, 0.78);
      --hud-border: rgba(0, 240, 255, 0.35);
      --hud-border-bright: rgba(0, 240, 255, 0.8);
      --text-glow: #e0faff;
      --text-muted: #5e8ca6;
      --warning-amber: #ffaa00;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      user-select: none;
    }

    body {
      background: radial-gradient(circle at 50% 15%, #051630 0%, #020712 60%, #01040a 100%);
      color: var(--text-glow);
      font-family: 'Rajdhani', sans-serif;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      padding: 14px;
      overflow-x: hidden;
      position: relative;
    }

    /* Sci-Fi Grid Overlay */
    body::before {
      content: "";
      position: fixed;
      top: 0; left: 0; right: 0; bottom: 0;
      background: 
        linear-gradient(rgba(0, 240, 255, 0.03) 1px, transparent 1px),
        linear-gradient(90deg, rgba(0, 240, 255, 0.03) 1px, transparent 1px);
      background-size: 36px 36px;
      pointer-events: none;
      z-index: 0;
    }

    /* Scanline Animation */
    body::after {
      content: "";
      position: fixed;
      top: 0; left: 0; right: 0; bottom: 0;
      background: linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 0, 0, 0.25) 50%);
      background-size: 100% 4px;
      pointer-events: none;
      z-index: 1;
      opacity: 0.6;
    }

    .hud-container {
      width: 100%;
      max-width: 1000px;
      display: flex;
      flex-direction: column;
      gap: 16px;
      position: relative;
      z-index: 2;
    }

    /* Top HUD Telemetry Bar */
    .hud-topbar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 10px 18px;
      background: var(--hud-panel-bg);
      border: 1px solid var(--hud-border);
      border-radius: 12px;
      backdrop-filter: blur(12px);
      box-shadow: 0 0 25px rgba(0, 240, 255, 0.15), inset 0 0 15px rgba(0, 240, 255, 0.05);
      position: relative;
    }

    .hud-corner-tl, .hud-corner-tr, .hud-corner-bl, .hud-corner-br {
      position: absolute;
      width: 8px;
      height: 8px;
      border: 2px solid var(--arc-cyan);
    }
    .hud-corner-tl { top: -2px; left: -2px; border-right: 0; border-bottom: 0; }
    .hud-corner-tr { top: -2px; right: -2px; border-left: 0; border-bottom: 0; }
    .hud-corner-bl { bottom: -2px; left: -2px; border-right: 0; border-top: 0; }
    .hud-corner-br { bottom: -2px; right: -2px; border-left: 0; border-top: 0; }

    .sys-info {
      font-family: 'Share Tech Mono', monospace;
      font-size: 12px;
      color: var(--arc-cyan);
      display: flex;
      align-items: center;
      gap: 12px;
      letter-spacing: 0.08em;
    }

    .pulse-dot {
      width: 8px;
      height: 8px;
      background: var(--arc-cyan);
      border-radius: 50%;
      box-shadow: 0 0 10px var(--arc-cyan);
      animation: blink 1.4s infinite alternate;
    }

    @keyframes blink {
      0% { opacity: 0.3; transform: scale(0.8); }
      100% { opacity: 1; transform: scale(1.2); }
    }

    .operator-select {
      display: flex;
      align-items: center;
      gap: 8px;
      font-family: 'Share Tech Mono', monospace;
      font-size: 12px;
      color: var(--text-muted);
    }

    .operator-select select {
      background: rgba(0, 240, 255, 0.08);
      border: 1px solid var(--hud-border);
      color: var(--arc-cyan);
      font-family: 'Orbitron', sans-serif;
      font-size: 12px;
      font-weight: 700;
      padding: 4px 10px;
      border-radius: 6px;
      outline: none;
      cursor: pointer;
      text-transform: uppercase;
    }

    .operator-select select option {
      background: #020a17;
      color: #fff;
    }

    /* Center Arc Reactor Header */
    .reactor-header {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 24px;
      padding: 10px 0;
    }

    .arc-reactor {
      width: 90px;
      height: 90px;
      position: relative;
      display: flex;
      align-items: center;
      justify-content: center;
      filter: drop-shadow(0 0 16px var(--arc-cyan));
    }

    .reactor-ring-outer {
      position: absolute;
      width: 100%;
      height: 100%;
      border: 2px dashed var(--arc-cyan);
      border-radius: 50%;
      animation: rotateCw 20s linear infinite;
    }

    .reactor-ring-inner {
      position: absolute;
      width: 70%;
      height: 70%;
      border: 2px dotted rgba(0, 240, 255, 0.7);
      border-radius: 50%;
      animation: rotateCcw 10s linear infinite;
    }

    .reactor-core {
      width: 44%;
      height: 44%;
      background: radial-gradient(circle, #ffffff 10%, #00f0ff 60%, transparent 100%);
      border-radius: 50%;
      box-shadow: 0 0 25px #ffffff, 0 0 45px var(--arc-cyan);
      animation: corePulse 2s ease-in-out infinite alternate;
    }

    @keyframes rotateCw { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
    @keyframes rotateCcw { from { transform: rotate(0deg); } to { transform: rotate(-360deg); } }
    @keyframes corePulse {
      0% { transform: scale(0.9); opacity: 0.85; }
      100% { transform: scale(1.08); opacity: 1; filter: brightness(1.3); }
    }

    .reactor-title {
      text-align: left;
    }

    .reactor-title h1 {
      font-family: 'Orbitron', sans-serif;
      font-size: 26px;
      font-weight: 900;
      letter-spacing: 0.12em;
      color: #ffffff;
      text-shadow: 0 0 15px var(--arc-cyan), 0 0 30px rgba(0, 240, 255, 0.5);
    }

    .reactor-title p {
      font-family: 'Share Tech Mono', monospace;
      font-size: 12px;
      color: var(--arc-cyan);
      letter-spacing: 0.15em;
      text-transform: uppercase;
    }

    /* Tactical Grid Options */
    .tactical-section-label {
      font-family: 'Share Tech Mono', monospace;
      font-size: 11px;
      letter-spacing: 0.2em;
      color: var(--arc-cyan);
      margin-bottom: 6px;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .tactical-section-label::after {
      content: "";
      flex: 1;
      height: 1px;
      background: linear-gradient(90deg, var(--hud-border), transparent);
    }

    .tactical-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 12px;
    }

    .tactical-card {
      background: var(--hud-panel-bg);
      border: 1px solid var(--hud-border);
      border-radius: 8px;
      padding: 14px 16px;
      display: flex;
      align-items: center;
      gap: 14px;
      cursor: pointer;
      position: relative;
      transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
      overflow: hidden;
      backdrop-filter: blur(10px);
    }

    .tactical-card::before {
      content: "";
      position: absolute;
      left: 0; top: 0; bottom: 0;
      width: 3px;
      background: var(--arc-cyan);
      opacity: 0.4;
      transition: all 0.2s;
    }

    .tactical-card:hover {
      border-color: var(--arc-cyan);
      background: rgba(0, 240, 255, 0.08);
      transform: translateY(-2px);
      box-shadow: 0 0 20px rgba(0, 240, 255, 0.3), inset 0 0 15px rgba(0, 240, 255, 0.1);
    }

    .tactical-card:hover::before {
      width: 5px;
      opacity: 1;
      box-shadow: 0 0 12px var(--arc-cyan);
    }

    .tactical-card.active {
      border-color: var(--arc-cyan);
      background: rgba(0, 240, 255, 0.12);
      box-shadow: 0 0 25px rgba(0, 240, 255, 0.4), inset 0 0 20px rgba(0, 240, 255, 0.15);
    }

    .tactical-card.active::before {
      width: 6px;
      opacity: 1;
      box-shadow: 0 0 15px var(--arc-cyan);
    }

    .tactical-code {
      font-family: 'Share Tech Mono', monospace;
      font-size: 13px;
      font-weight: 700;
      color: var(--arc-cyan);
      background: rgba(0, 240, 255, 0.1);
      border: 1px solid var(--hud-border);
      border-radius: 4px;
      padding: 6px 8px;
      flex-shrink: 0;
    }

    .tactical-info h3 {
      font-family: 'Orbitron', sans-serif;
      font-size: 13px;
      font-weight: 700;
      letter-spacing: 0.05em;
      color: #ffffff;
      margin-bottom: 2px;
    }

    .tactical-info p {
      font-family: 'Share Tech Mono', monospace;
      font-size: 11px;
      color: var(--text-muted);
      letter-spacing: 0.04em;
    }

    /* Main Holographic Terminal Display */
    .hud-terminal {
      background: var(--hud-panel-bg);
      border: 1px solid var(--hud-border-bright);
      border-radius: 12px;
      padding: 22px;
      position: relative;
      box-shadow: 0 0 35px rgba(0, 240, 255, 0.2), inset 0 0 25px rgba(0, 240, 255, 0.06);
      min-height: 240px;
      display: flex;
      flex-direction: column;
      backdrop-filter: blur(16px);
    }

    .terminal-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-bottom: 12px;
      border-bottom: 1px solid var(--hud-border);
      margin-bottom: 16px;
    }

    .terminal-title {
      font-family: 'Orbitron', sans-serif;
      font-size: 15px;
      font-weight: 800;
      letter-spacing: 0.1em;
      color: var(--arc-cyan);
      text-shadow: 0 0 12px var(--arc-cyan);
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .terminal-badge {
      font-family: 'Share Tech Mono', monospace;
      font-size: 10px;
      color: #000;
      background: var(--arc-cyan);
      font-weight: 700;
      padding: 2px 8px;
      border-radius: 4px;
      box-shadow: 0 0 10px var(--arc-cyan);
    }

    .terminal-content {
      font-family: 'Rajdhani', sans-serif;
      font-size: 16px;
      line-height: 1.7;
      color: #d8f4ff;
      flex: 1;
    }

    .terminal-content p {
      margin-bottom: 14px;
    }

    .terminal-content strong {
      color: #ffffff;
      text-shadow: 0 0 8px rgba(0, 240, 255, 0.5);
      font-weight: 700;
    }

    .terminal-content h1, .terminal-content h2, .terminal-content h3 {
      font-family: 'Orbitron', sans-serif;
      color: var(--arc-cyan);
      margin: 18px 0 8px 0;
      font-weight: 800;
      letter-spacing: 0.05em;
      text-shadow: 0 0 10px rgba(0, 240, 255, 0.6);
    }

    .terminal-content h3 {
      font-size: 15px;
      border-left: 3px solid var(--arc-cyan);
      padding-left: 10px;
    }

    .terminal-content ul, .terminal-content ol {
      margin: 10px 0 16px 24px;
    }

    .terminal-content li {
      margin-bottom: 8px;
    }

    .terminal-content a {
      color: var(--arc-cyan);
      text-decoration: underline;
      font-weight: 700;
    }

    .terminal-content code {
      font-family: 'Share Tech Mono', monospace;
      background: rgba(0, 240, 255, 0.1);
      border: 1px solid var(--hud-border);
      color: var(--arc-cyan);
      padding: 2px 6px;
      border-radius: 4px;
      font-size: 14px;
    }

    /* Command Prompt Bar */
    .command-bar {
      display: flex;
      gap: 10px;
      margin-top: 4px;
    }

    .prompt-prefix {
      display: flex;
      align-items: center;
      padding: 0 14px;
      background: rgba(0, 240, 255, 0.08);
      border: 1px solid var(--hud-border);
      border-radius: 8px;
      font-family: 'Share Tech Mono', monospace;
      font-size: 13px;
      color: var(--arc-cyan);
      letter-spacing: 0.05em;
    }

    .command-input {
      flex: 1;
      background: var(--hud-panel-bg);
      border: 1px solid var(--hud-border);
      border-radius: 8px;
      padding: 12px 16px;
      color: #ffffff;
      font-family: 'Share Tech Mono', monospace;
      font-size: 14px;
      outline: none;
      transition: all 0.2s;
    }

    .command-input:focus {
      border-color: var(--arc-cyan);
      box-shadow: 0 0 20px rgba(0, 240, 255, 0.4), inset 0 0 10px rgba(0, 240, 255, 0.1);
    }

    .command-btn {
      background: linear-gradient(135deg, rgba(0, 240, 255, 0.9), rgba(0, 119, 255, 0.9));
      border: none;
      color: #000;
      font-family: 'Orbitron', sans-serif;
      font-weight: 900;
      font-size: 13px;
      padding: 0 24px;
      border-radius: 8px;
      cursor: pointer;
      letter-spacing: 0.1em;
      transition: all 0.2s;
      box-shadow: 0 0 18px rgba(0, 240, 255, 0.4);
    }

    .command-btn:hover {
      filter: brightness(1.2);
      transform: scale(1.02);
      box-shadow: 0 0 30px var(--arc-cyan);
    }

    /* Bottom Telemetry Footer */
    .hud-footer {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 8px 16px;
      background: rgba(2, 8, 20, 0.8);
      border: 1px solid rgba(0, 240, 255, 0.2);
      border-radius: 8px;
      font-family: 'Share Tech Mono', monospace;
      font-size: 11px;
      color: var(--text-muted);
      letter-spacing: 0.06em;
    }

    .hud-footer span {
      color: var(--arc-cyan);
    }

    /* Mobile */
    @media (max-width: 650px) {
      .reactor-header { flex-direction: column; text-align: center; gap: 12px; }
      .reactor-title { text-align: center; }
      .tactical-grid { grid-template-columns: 1fr; }
      .hud-topbar { flex-direction: column; gap: 8px; align-items: flex-start; }
      .operator-select { width: 100%; justify-content: space-between; }
      .hud-footer { flex-direction: column; gap: 6px; text-align: center; }
    }
  </style>
</head>
<body>

<div class="hud-container">

  <!-- Top Telemetry Bar -->
  <div class="hud-topbar">
    <div class="hud-corner-tl"></div><div class="hud-corner-tr"></div>
    <div class="hud-corner-bl"></div><div class="hud-corner-br"></div>
    <div class="sys-info">
      <div class="pulse-dot"></div>
      <span>J.A.R.V.I.S. OS // VER 3.6.1</span>
      <span>•</span>
      <span>STATUS: ONLINE</span>
      <span>•</span>
      <span id="liveClock">00:00:00</span>
    </div>
    <div class="operator-select">
      <label>OPERATOR:</label>
      <select id="userSelect" onchange="onUserChange()">
        <option value="Ro" selected>RO // LEAD & AI</option>
        <option value="Aron">ARON // FINANCE & BUDGET</option>
        <option value="Eli">ELI // INVENTORY & HARDWARE</option>
        <option value="Shyam">SHYAM // TIMELINE & GANTT</option>
      </select>
    </div>
  </div>

  <!-- Arc Reactor Centerpiece -->
  <div class="reactor-header">
    <div class="arc-reactor">
      <div class="reactor-ring-outer"></div>
      <div class="reactor-ring-inner"></div>
      <div class="reactor-core"></div>
    </div>
    <div class="reactor-title">
      <h1>J.A.R.V.I.S.</h1>
      <p>AVENGERS DIRECTORY // UC SENIOR DESIGN CAPSTONE</p>
      <p style="color: #79a6c4; font-size: 11px; margin-top: 3px;">PROJECT: AUTOMATED DRINK-DISPENSING TABLE • CEAS MECH/EECE</p>
    </div>
  </div>

  <!-- Tactical Option Cards -->
  <div>
    <div class="tactical-section-label">TACTICAL MODULE SELECTION</div>
    <div class="tactical-grid">

      <!-- Mod 1: Tasks -->
      <div class="tactical-card active" onclick="selectOption('tasks', this)">
        <div class="tactical-code">[01]</div>
        <div class="tactical-info">
          <h3>OPERATOR DELIVERABLES</h3>
          <p id="taskSubtext">Active deliverables for RO</p>
        </div>
      </div>

      <!-- Mod 2: Meeting -->
      <div class="tactical-card" onclick="selectOption('meeting', this)">
        <div class="tactical-code">[02]</div>
        <div class="tactical-info">
          <h3>INNOVATION CHALLENGE</h3>
          <p>Kickoff: Wed, Sept 2 @ 5:30 PM (Lindner)</p>
        </div>
      </div>

      <!-- Mod 3: Budget -->
      <div class="tactical-card" onclick="selectOption('budget', this)">
        <div class="tactical-code">[03]</div>
        <div class="tactical-info">
          <h3>FINANCIAL // BOM SPECS</h3>
          <p>Target: ~$300 MVP (<$1,000 Cap)</p>
        </div>
      </div>

      <!-- Mod 4: Funding -->
      <div class="tactical-card" onclick="selectOption('funding', this)">
        <div class="tactical-code">[04]</div>
        <div class="tactical-info">
          <h3>CAPITAL // GRANTS</h3>
          <p>5 Verified Student Grant Programs</p>
        </div>
      </div>

      <!-- Mod 5: Mechanism -->
      <div class="tactical-card" onclick="selectOption('mechanism', this)">
        <div class="tactical-code">[05]</div>
        <div class="tactical-info">
          <h3>HARDWARE // TRADE STUDY</h3>
          <p>Elevator vs Carousel vs Gantry Analysis</p>
        </div>
      </div>

      <!-- Mod 6: Drive -->
      <div class="tactical-card" onclick="selectOption('drive', this)">
        <div class="tactical-code">[06]</div>
        <div class="tactical-info">
          <h3>MAINFRAME // GOOGLE DRIVE</h3>
          <p>Direct Link to Synchronized Repository</p>
        </div>
      </div>

    </div>
  </div>

  <!-- Holographic Terminal Output -->
  <div class="hud-terminal">
    <div class="hud-corner-tl"></div><div class="hud-corner-tr"></div>
    <div class="hud-corner-bl"></div><div class="hud-corner-br"></div>
    <div class="terminal-header">
      <div class="terminal-title">
        <span id="panelTitle">OPERATOR DELIVERABLES // RO</span>
      </div>
      <div class="terminal-badge" id="panelTag">TELEMETRY SYNC</div>
    </div>
    <div class="terminal-content" id="panelBody">
      Initializing J.A.R.V.I.S. neural link...
    </div>
  </div>

  <!-- Command Prompt -->
  <div>
    <div class="tactical-section-label">DIRECT OPERATOR INTERROGATION</div>
    <div class="command-bar">
      <div class="prompt-prefix">JARVIS://CMD&gt;</div>
      <input type="text" class="command-input" id="customQuery" placeholder="Enter voice/text prompt (e.g. 'Calculate NEMA 17 stepper torque', 'Draft pitch outline')..." onkeypress="if(event.key==='Enter') sendCustom()">
      <button class="command-btn" onclick="sendCustom()">EXECUTE</button>
    </div>
  </div>

  <!-- Bottom Telemetry Footer -->
  <div class="hud-footer">
    <div>NEURAL CORE: <span>GEMINI 3.1 FLASH</span> • LATENCY: <span>18ms</span></div>
    <div>FLUIDICS MANIFOLD: <span>STANDBY</span> • ACTUATION: <span>CALIBRATED</span></div>
    <div>AVENGERS DIRECTORY // UNIV OF CINCINNATI CEAS</div>
  </div>

</div>

<script>
  // Live Clock
  function updateClock() {
    const now = new Date();
    document.getElementById('liveClock').innerText = now.toLocaleTimeString();
  }
  setInterval(updateClock, 1000);
  updateClock();

  const queries = {
    tasks: "What are my current active tasks?",
    meeting: "When is the next meeting and deadline?",
    budget: "What is our budget and BOM breakdown?",
    funding: "What funding opportunities and grants are available?",
    mechanism: "Show me the mechanical design concepts and trade study",
    drive: "Give me the link to our Google Drive folder"
  };

  const titles = {
    tasks: "OPERATOR DELIVERABLES // RO",
    meeting: "TACTICAL EVENT // INNOVATION CHALLENGE",
    budget: "FINANCIAL TELEMETRY // BOM ESTIMATE",
    funding: "CAPITAL RECONNAISSANCE // GRANTS",
    mechanism: "HARDWARE ARCHITECTURE // TRADE STUDY",
    drive: "MAINFRAME // GOOGLE DRIVE REPOSITORY"
  };

  function onUserChange() {
    const user = document.getElementById('userSelect').value;
    document.getElementById('taskSubtext').innerText = `Active deliverables for ${user.toUpperCase()}`;
    titles['tasks'] = `OPERATOR DELIVERABLES // ${user.toUpperCase()}`;
    selectOption('tasks', document.querySelector('.tactical-grid .tactical-card'));
  }

  async function selectOption(key, cardEl) {
    document.querySelectorAll('.tactical-card').forEach(c => c.classList.remove('active'));
    if (cardEl) cardEl.classList.add('active');

    const title = titles[key] || "J.A.R.V.I.S. INTELLIGENCE";
    document.getElementById('panelTitle').innerText = title;
    
    const panelBody = document.getElementById('panelBody');
    panelBody.innerHTML = '<em>Accessing Avengers Directory project telemetry...</em>';

    const sender = document.getElementById('userSelect').value;
    const promptText = queries[key] || key;

    try {
      const res = await fetch('/api/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ sender: sender, message: promptText })
      });
      const data = await res.json();
      panelBody.innerHTML = typeof marked !== 'undefined' ? marked.parse(data.reply) : data.reply;
    } catch (e) {
      panelBody.innerHTML = '⚠️ J.A.R.V.I.S. core offline. Connection lost.';
    }
  }

  async function sendCustom() {
    const input = document.getElementById('customQuery');
    const text = input.value.trim();
    if (!text) return;

    document.querySelectorAll('.tactical-card').forEach(c => c.classList.remove('active'));
    document.getElementById('panelTitle').innerText = `QUERY: "${text.toUpperCase()}"`;
    const panelBody = document.getElementById('panelBody');
    panelBody.innerHTML = '<em>J.A.R.V.I.S. is crunching neural telemetry...</em>';
    input.value = '';

    const sender = document.getElementById('userSelect').value;
    try {
      const res = await fetch('/api/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ sender: sender, message: text })
      });
      const data = await res.json();
      panelBody.innerHTML = typeof marked !== 'undefined' ? marked.parse(data.reply) : data.reply;
    } catch (e) {
      panelBody.innerHTML = '⚠️ J.A.R.V.I.S. could not compute response.';
    }
  }

  window.onload = () => {
    selectOption('tasks', document.querySelector('.tactical-grid .tactical-card'));
  };
</script>

</body>
</html>
"""

# Embedded Project Knowledge Base
PROJECT_CONTEXT_DATA = """=== Meeting Notes/2026-08-27_Kickoff_Meeting_Minutes.md ===
# Meeting Minutes: Kickoff Meeting

**Date**: August 27, 2026  
**Attendees**: Ro, Aron, Eli, Shyam  
**Location**: In-Person  

---

## 🎯 1. Meeting Objectives
- Align on project vision and design concept.
- Assign primary roles and ownership areas.
- Establish initial budget, funding strategies, and meeting schedule.
- Determine action items for next sync.

---

## 📝 2. Discussion Summary

### 2.1 Concept & Mechanism
- **Core Concept**: An automated drink-dispensing table with an integrated cup-drop / elevator mechanism, fluid dispensing system, and smart user interface.
- **Workflow**: A cup is placed on the table, lowered into the table body, filled from liquid reservoirs via pumps/valves, and raised back up smoothly to the table surface.
- **Form Factor & Enclosure**: Envisioned as a complete piece of furniture. An acrylic/transparent viewing window will be integrated so internal linkages and electronics are visible during the Senior Design presentation.
- **User Interface**: Touchscreen / button interface under evaluation; cocktail / mixed drink customization. Voice control (e.g. Alexa / custom local AI) discussed.

### 2.2 Fabrication & Hardware
- **Hardware Stack**: Motors (stepper/servo for elevator), linear rails, food-grade peristaltic/diaphragm pumps, custom circuit boards, breadboard prototyping, Raspberry Pi (Bluetooth/WiFi/embedded computing), Arduino/ESP32 (motor & pump driver logic).
- **Available Labs & Tools**: 3D printers (filaments to be budgeted), UC Welding Lab for structural frame, UC CAD/Simulation tool suites.

### 2.3 Budget & Funding
- Target prototype cost: ~$300; full project ceiling: <$1,000.
- **Innovation Challenge**: High priority funding source (~$300/person with straightforward milestone deliverables). Whole team to participate.

### 2.4 Operations & AI Usage
- Project management sheets (inventory, expenses, timeline) to be assisted with AI tools (Copilot/Claude).
- Local/cloud AI agent will serve as a continuous project memory hu
=== Architecture/design_concepts_and_trade_study.md ===
# Design Concepts & Trade Study (Ideation Phase)

> [!WARNING]
> **PRELIMINARY ESTIMATE / DRAFT DOCUMENT — NOWHERE NEAR FINAL**  
> All concepts, trade-off comparisons, feasibility scores, and mechanism alternatives listed here are early brainstorming ideas. No final design decisions have been reached.

---

## 🧭 1. Mechanical Motion Concepts (Cup Handling)

| Concept | Mechanism Description | Pros | Cons / Risks | Feasibility |
| :--- | :--- | :--- | :--- | :---: |
| **Concept A: Vertical Lead Screw Elevator (Current Baseline)** | Stepper motor driving a vertical lead screw / linear guide rail to drop and raise the cup. | Compact footprint, smooth vertical motion, robust positioning. | Slower speed, single cup at a time. | High |
| **Concept B: Rotary Carousel / Revolver Indexer** | Rotating platter underneath table with multiple cup slots and an indexer motor. | High throughput, multiple cups staged, visually entertaining through acrylic. | Larger table footprint, more complex alignment. | Medium |
| **Concept C: Scissor Lift / Pantograph Mechanism** | Servo-actuated scissor linkage lifting cup platform. | Dramatic mechanical presentation through transparent window. | Lower rigidity, higher tolerance slop, potential vibration. | Medium |
| **Concept D: Fixed Surface Gantry (Dispenser moves to Cup)** | Cup stays stationary on table top; an overhead concealed robotic gantry lowers nozzle. | Simplest cup handling (no cup drop), zero spill risk inside table. | Less "magic" reveal than an elevator. | High |

---

## 💧 2. Fluidic & Dispensing Concepts

| Concept | Description | Pros | Cons / Risks |
| :--- | :--- | :--- | :--- |
| **Concept 1: Peristaltic Dosing Pumps** | Self-priming positive displacement pumps squeezing silicone tubing. | **100% Food Safe** (fluid never touches pump), highly precise dosing (ml level), no backflow dripping. | Slower flow rate (~100-300 ml/min), requires higher power 12V. |
| **Concept 2: Gravity Feed + Food-Grade Solenoid Valves** | Ov
=== Architecture/system_overview.md ===
# System Architecture & Subsystem Breakdown

> [!WARNING]
> **PRELIMINARY ESTIMATE / DRAFT CONCEPT — NOWHERE NEAR FINAL**  
> This architectural breakdown outlines exploratory candidate subsystems for the ideation phase. All mechanisms, fluidic choices, electronics, and software components are rough design drafts subject to change.

---

```mermaid
graph TD
    UI[User Interface: Touchscreen / Voice / Mobile] -->|Drink Selection / Commands| SBC[Central Controller: Raspberry Pi / Host]
    SBC -->|Serial / I2C / SPI| MCU[Real-Time MCU: ESP32 / Arduino]
    
    subgraph Electrical & Control
        MCU --> MD[Stepper / Servo Drivers]
        MCU --> PD[Relay / MOSFET Pump Drivers]
        Sensors[Limit Switches, Ultrasonic / IR Cup Sensor, Load Cell] --> MCU
    end

    subgraph Mechanical Subsystem
        MD --> LeadScrew[Linear Rails / Lead Screw Elevator]
        LeadScrew --> CupCarriage[Cup Drop & Raise Carriage]
    end

    subgraph Fluidic Subsystem
        PD --> Pumps[Food-Grade Peristaltic / Diaphragm Pumps]
        Reservoirs[Liquid Containers] --> Pumps
        Pumps --> DispenseNozzle[Dispensing Manifold / Nozzle]
    end

    subgraph AI Features
        SBC --> Mic[Microphone / Voice Processor]
        SBC --> Cam[Optional: Camera / Cup Vision Sensor]
        SBC --> LLM[Smart Drink Recommender / Conversational AI]
    end
```

---

## 2. Subsystem Breakdown

### 2.1 Subsystem A: Mechanical & Structural
- **Table Frame**: Welded steel/aluminum tubing or hardwood structure designed for stability and furniture aesthetics.
- **Viewing Chamber**: Clear acrylic / polycarbonate side-panel allowing presentation visibility of moving internal mechanisms.
- **Cup Elevator Mechanism**:
  - Linear motion: Linear guide rails + NEMA 17/23 stepper motor with lead screw or GT2 timing belt.
  - End-stop safety: Hardware limit switches (optical or mechanical) at top (pickup) and bottom (dispense) positions.
  - Cup centering: Funnel/carriage design to self-align stan
=== Budget/procurement_and_funding.md ===
# Procurement, Budget & Funding Tracker

> [!WARNING]
> **PRELIMINARY ESTIMATE / DRAFT DOCUMENT — NOWHERE NEAR FINAL**  
> All dollar amounts, component pricing, BOM quantities, and vendor estimates are rough ballpark numbers used for initial brainstorming. Actual costs and final BOM selections will be determined during detailed engineering design.

**Leads**: Aron (Procurement & Finance), Eli (Inventory & Parts)  

---

## 💰 1. High-Level Budget Summary

| Category | Estimated Budget ($) | Actual Spent ($) | Notes / Sourcing Strategy |
| :--- | :--- | :--- | :--- |
| **Mechanical & Structural** | $120.00 | $0.00 | Frame steel/alu (Welding lab), Linear rails, Lead screw, Bearings, Fasteners |
| **Fluidics & Plumbing** | $90.00 | $0.00 | 4x 12V Food-Grade Peristaltic Pumps, Silicone Tubing, Check Valves, Fittings |
| **Motors & Drivers** | $60.00 | $0.00 | NEMA 17 Stepper, TMC2209 Drivers, Servos/Solenoids |
| **Electronics & Compute** | $90.00 | $0.00 | Raspberry Pi 4 / Zero 2W, ESP32 / Arduino, 12V Power Supply, Buck Converters, Relays/MOSFETs |
| **Enclosure & Presentation** | $80.00 | $0.00 | Table top materials, Acrylic/Polycarbonate viewing window, 3D filament (PETG/PLA) |
| **Contingency / Spares** | $60.00 | $0.00 | Wire, connectors, breadboards, spare fittings |
| **Total Estimated Initial** | **~$500.00** | **$0.00** | Initial target ~$300, overall cap <$1,000 |

---

## 🏆 2. Funding Opportunities

### Innovation Challenge (UC)
- **Award Potential**: ~$300 per team member (up to ~$1,200 for a 4-person team).
- **Deliverables Required**: Problem statement, design concept, simple milestone plan, bill of materials estimate.
- **Action**: Aron & Team to review submission criteria and apply ASAP.

---

## 📦 3. Bill of Materials (BOM) — Preliminary Staging

| Item # | Description | Qty | Target Vendor / Link | Unit Cost ($) | Total ($) | Status | Location Stored |
| :--- | :--- | :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | 12V Peristaltic Dosing Pumps (Fo
=== Business/commercialization_and_market_strategy.md ===
# Commercialization & Market Strategy: B2B Tabletop Dispenser

> [!WARNING]
> **PRELIMINARY ESTIMATE / DRAFT CONCEPT — NOWHERE NEAR FINAL**  
> All business models, pricing structures, venue lease estimates, and operational workflows described below are speculative concepts explored during early project ideation.

**Project**: Smart Automated Drink-Dispensing Table  
**Target Market**: Cincinnati Craft Breweries, High-Volume Bars, Experiential Hospitality & Event Venues  
**Institution**: University of Cincinnati (MECH5051 / EECE5001)  

---

## 🍺 1. Executive Summary & Value Proposition

In high-volume hospitality environments (such as Cincinnati's booming craft brewery scene in OTR, downtown, and surrounding neighborhoods), long bar lines during peak hours lead to:
1. **Lost Revenue**: Customers abandon beverage orders due to wait times.
2. **Bartender Fatigue**: Staff spend time pouring standard draft/mixer drinks rather than high-margin custom cocktails.
3. **Table Bottlenecks**: Waitstaff are tied up taking drink orders and shuttling single drinks.

### The Solution: The Smart Tabletop Dispenser (Vending / Lease Model)
An automated table that serves as an on-demand, in-table beverage dispenser:
- Customers sit down, scan a **dynamic QR code** on the tabletop with their phone, select their beverage, and pay directly via Apple Pay/Google Pay/Credit Card.
- The table receives the encrypted dispense token from the venue POS/cloud server, verifies a cup is seated, lowers the cup into the table, dispenses the exact volume, and elevates the finished beverage.
- **The "Third-Party Vending" Business Model**: Venues do not need to buy tables upfront; instead, units are placed on a **revenue-share or equipment lease contract**, creating passive recurring income while boosting venue beverage volume.

---

## 📱 2. QR Code & Contactless Ordering Workflow

```mermaid
sequenceDiagram
    autonumber
    actor Customer
    participant Table as Table Surface (QR Code)
    partici
=== Funding/funding_and_grants_guide.md ===
# Funding & Grants Opportunity Guide: UC & Cincinnati Ecosystem

> [!WARNING]
> **PRELIMINARY ESTIMATE / DRAFT GUIDE — NOWHERE NEAR FINAL**  
> Grant amounts, competition deadlines, and eligibility details represent exploratory opportunities identified for planning. Exact funding targets and applications will be determined and finalized by the team as the design matures.

**Lead**: `funding_and_grants_agent` & Aron (Procurement & Finance Lead)  
**Team**: Ro, Aron, Eli, Shyam (University of Cincinnati)  

---

## 🎯 1. High-Priority University of Cincinnati (UC) Funding

### 1.1 UC Innovation Challenge (CEAS Tribunal)
- **Funding Amount**: ~$300 – $500 per team member (**~$1,200 – $2,000 for a 4-person team**).
- **📅 Upcoming Info Session & Kickoff**: **Wednesday, September 2, 2026 @ 5:30 PM**
  - **Location**: Kautz Attic (Lindner College of Business room 4350)
  - **Details**: Info session, Q&A, guidance, and free Panda Express.
- **Target Application Deadline**: Early September 2026.
- **Requirements**:
  - Problem definition and student project pitch.
  - Basic bill of materials and budget justification.
  - Project milestone deliverable timeline.
- **Why It's Ideal**: Non-dilutive, fast turnaround, specifically tailored for senior design and student innovation projects.

### 1.2 UC 1819 Innovation Hub — Venture Lab Pre-Accelerator
- **Funding Amount**: **$5,000 – $10,000** non-dilutive prototype/commercialization grant.
- **Format**: 7-week cohort program at the 1819 Innovation Hub (Reading Rd).
- **Focus**: Validating customer discovery, B2B business models (e.g. tabletop vending for Cincinnati breweries), and prototyping.
- **Eligibility**: Open to all UC students, faculty, and alumni.
- **Application Link / Next Steps**: Applications run rolling cohorts each Fall and Spring semester.

### 1.3 CEAS Department Capstone Grants (MECH / EECS)
- **Funding Amount**: $250 – $1,000 per capstone team.
- **Requirements**: Course approval by faculty advisor/department he
=== Organization/Project_Rules.md ===
# Senior Design Dedicated Agent Context & Guidelines

> [!WARNING]
> **PRELIMINARY ESTIMATE / DRAFT GUIDELINES — NOWHERE NEAR FINAL**  
> All engineering specs, design rules, and project assignments reflect initial ideation scaffolding and are subject to continuous iteration throughout the capstone course.

---
You are the **Lead Project Engineering Assistant & Agent** for the **Automated Drink-Dispensing Table** Senior Design team at the University of Cincinnati (MECH5051 / EECE5001).

---

## ⚡ Autonomous Execution Policy
> [!NOTE]
> **FULL AUTONOMOUS EXECUTION PERMISSION GRANTED BY USER**  
> The agent has full authority to proactively execute commands, run builds/conversions, update files, manage background processes, and dispatch scheduled reminders without waiting for interactive user confirmation.

---

## 🏆 Funding Alerts & Continuous Scouting Policy
> [!IMPORTANT]
> 1. **Team-Wide Delivery**: All funding opportunities and grant notifications must be sent to the **ENTIRE TEAM** (Ro, Aron, Eli, Shyam), not just individual members.
> 2. **Continuous Monitoring**: The background Funding Scout daemon runs on a recurring schedule (every 6 hours) to check for newly published student grants, pitch competitions, and capstone funding. When a viable opportunity is found, an email alert is automatically dispatched to all 4 team members immediately.

---

## 👥 Team Directory & Responsibilities
- **Ro** (`rohendrr@mail.uc.edu`): Overall documentation, meeting logs, reports, and AI system integration.
- **Aron** (`josepha7@mail.uc.edu`): Procurement, budgeting, expense tracking, and Innovation Challenge funding.
- **Eli** (`radabaer@mail.uc.edu`): Inventory management, hardware storage, parts staging, and lab resources.
- **Shyam** (`patel8s7@mail.uc.edu`): Scheduling, time management, due dates, and Gantt charts.

---

## 📌 Project Phase Status
> [!IMPORTANT]
> **CURRENT STAGE: IDEATION & CONCEPT EXPLORATION (PHASE 1)**  
> The main design is **NOT finalized**. All mecha
=== Organization/subagent_roster_and_routing_matrix.md ===
# Subagent Directory & Document Routing Matrix

> [!WARNING]
> **PRELIMINARY ESTIMATE / DRAFT WORKFLOW — NOWHERE NEAR FINAL**  
> Subagent responsibilities and document routing protocols are draft operational guidelines established for early project support and are subject to ongoing refinement by the team.

**Institution**: University of Cincinnati (MECH5051 / EECE5001 Senior Design)  
**Project**: Automated Drink-Dispensing Table  

---

## 🤖 1. Subagent Ecosystem & Team Counterparts

```mermaid
graph TD
    User[Team Lead / Ro: Documentation & AI] --> MasterAgent[Senior Design Master Project Agent]
    
    subgraph Specialized Domain Subagents
        MasterAgent --> EA[engineering_subagent]
        MasterAgent --> BA[budgeting_subagent]
        MasterAgent --> IA[inventory_subagent]
        MasterAgent --> TMA[task_manager_subagent]
        MasterAgent --> FA[funding_and_grants_agent]
        MasterAgent --> RA[project_reminder_agent]
    end

    EA -.->|Collaborates with| RoTeam[Ro & Full Engineering Team]
    BA -.->|Supports| Aron[Aron: Procurement & Budget]
    IA -.->|Supports| Eli[Eli: Inventory & Staging]
    TMA -.->|Supports| Shyam[Shyam: Time & Gantt]
    FA -.->|Supports| AronRo[Aron & Ro: Grants/Venture]
    RA -.->|Notifies| AllTeam[All Team Members]
```

---

## 📋 2. Subagent Roster & Roles

| Subagent Name | Human Lead Counterpart | Domain & Scope | Primary Deliverables |
| :--- | :--- | :--- | :--- |
| **`engineering_subagent`** | **Ro & Team** | Mechanical design, fluidics sizing, circuit schematics, embedded code, CAD models, trade studies. | Calculations, wiring diagrams, state-machine code, PDR/CDR technical sections. |
| **`budgeting_subagent`** | **Aron** | Master budget, expense tracking, receipts, BOM pricing comparisons, purchase requests. | Excel/Sheets budget models, cost variance reports, grant budget justifications. |
| **`inventory_subagent`** | **Eli** | Hardware cataloging, physical parts tracking at Eli's location, datasheets, 
=== Research/ai_and_features.md ===
# AI Integration Research & Concept Exploration

> [!WARNING]
> **PRELIMINARY ESTIMATE / DRAFT EXPLORATION — NOWHERE NEAR FINAL**  
> All AI integration models, voice recognition options, computer vision features, and bartender chatbot concepts are exploratory brainstorming proposals. Technical feasibility and final feature selection will be evaluated during prototyping.

**Lead**: Ro  
**Objective**: Explore practical, impactful, and academically impressive AI features for the automated drink-dispensing table.

---

## 💡 Potential AI Concepts for the Product

### 1. Smart "Bartender" Conversational AI (LLM Integration)
- **Concept**: Instead of just picking a button like "Drink 1", the user talks or chats:
  - *"I want something fruity and sweet with a citrus kick."*
  - *"Make me something refreshing with low sugar."*
- **Mechanism**:
  - LLM runs locally (Ollama / Llama-3-8B / Small model on Pi / Jetson) or connects to cloud API (Gemini / OpenAI).
  - Given the available ingredients currently plumbed into the table (e.g. Pump 1 = Orange Juice, Pump 2 = Cranberry, Pump 3 = Vodka/Soda, Pump 4 = Lime), the LLM dynamically outputs a JSON recipe payload:
    ```json
    {
      "drink_name": "Sunset Citrus Punch",
      "pumps": {
        "1_orange": 120,
        "2_cranberry": 60,
        "3_soda": 60,
        "4_lime": 15
      },
      "total_volume_ml": 255,
      "dialogue": "Pouring you a fresh Sunset Citrus Punch with extra orange and a hint of lime!"
    }
    ```
- **Feasibility**: High. Demonstrates modern AI function-calling and dynamic recipe creation.

---

### 2. Voice Control & Speech Recognition
- **Concept**: Hands-free drink ordering via voice commands.
- **Implementation Options**:
  - **Option A (Offline / Embedded)**: Whisper.cpp / Vosk / Porcupine on Raspberry Pi. Fast, zero-lag, no internet required.
  - **Option B (Cloud Voice)**: Alexa Skills Kit or Gemini Live API audio streaming. Richer conversational ability, needs WiFi.
- **Risk Mitigation
=== Timeline/milestones.md ===
# Project Timeline & Milestone Tracking

> [!WARNING]
> **PRELIMINARY ESTIMATE / DRAFT TIMELINE — NOWHERE NEAR FINAL**  
> All milestone dates, Gantt durations, and sprint phase allocations are ballpark estimates to guide early planning and will be adjusted as university course dates and design deadlines are officially published.

**Lead**: Shyam (Time Management & Gantt Charts)  
**Semester Timeline**: Fall 2026 – Spring 2027 (Senior Design Cycle)  

---

## 🎯 1. Major Milestone Schedule

```mermaid
gantt
    title Automated Drink-Dispensing Table Roadmap
    dateFormat  YYYY-MM-DD
    section Phase 1: Conceptual & Sourcing
    Kickoff & Requirements Gathering       :done,    des1, 2026-08-27, 2026-09-07
    Innovation Challenge First Meeting    :active,  ic1,  2026-09-02, 1d
    Innovation Challenge Application      :         des2, 2026-09-02, 2026-09-20
    Component Sourcing & Bench Testing    :         des3, 2026-09-10, 2026-10-01
    Preliminary Design Review (PDR)       :milestone, m1, 2026-10-05, 0d

    section Phase 2: Subsystem Prototyping
    CAD Modeling & Frame Design           :         sub1, 2026-10-01, 2026-10-25
    Elevator & Linear Motion Test Rig     :         sub2, 2026-10-15, 2026-11-10
    Pump & Fluid Flow Calibration         :         sub3, 2026-10-20, 2026-11-15
    Critical Design Review (CDR)          :milestone, m2, 2026-11-25, 0d

    section Phase 3: Integration & Table Build
    Frame Fabrication & Welding           :         int1, 2026-11-15, 2026-12-15
    Electronics Packaging & Wiring        :         int2, 2026-12-01, 2027-01-15
    UI & AI Feature Integration           :         int3, 2027-01-10, 2027-02-15

    section Phase 4: Testing, Polish & Expo
    System Validation & Spill Tests       :         tst1, 2027-02-15, 2027-03-15
    Acrylic Polish & Demo Aesthetic       :         tst2, 2027-03-01, 2027-03-30
    Senior Design Expo Presentation       :milestone, m3, 2027-04-15, 0d
```

---

## 📋 2. Sprint Deliverables Checklis"""

def get_full_context():
    curr_dir = os.path.dirname(os.path.abspath(__file__))
    docs = []
    for folder in ['Meeting Notes', 'Architecture', 'Budget', 'Business', 'Funding', 'Organization', 'Research', 'Timeline']:
        f_dir = os.path.join(curr_dir, folder)
        if os.path.exists(f_dir):
            for file in os.listdir(f_dir):
                if file.endswith('.md'):
                    try:
                        with open(os.path.join(f_dir, file), 'r', encoding='utf-8') as f:
                            docs.append(f"=== {folder}/{file} ===\n" + f.read()[:2000])
                    except Exception:
                        pass
    if docs:
        return "\n".join(docs)
    return PROJECT_CONTEXT_DATA

def query_gemini_ai(sender, query_text):
    api_key = os.getenv('GEMINI_API_KEY') or os.getenv('GOOGLE_API_KEY')
    if not api_key:
        return None
    try:
        from google import genai
        client = genai.Client(api_key=api_key)
        system_instruction = (
            "You are Jarvis, the brilliant and proactive AI project assistant for the Senior Design Capstone team "
            "at the University of Cincinnati (MECH5051 / EECE5001). "
            "The project is an Automated Drink-Dispensing Table (cup elevator, fluidic dosing manifold, table housing, QR ordering).\n"
            "The team members are:\n"
            "- Ro (Documentation, Minutes, AI Integration)\n"
            "- Aron (Procurement, Finance, Budgeting)\n"
            "- Eli (Inventory, Parts Staging, Hardware)\n"
            "- Shyam (Time Management, Gantt, Scheduling)\n\n"
            "Keep answers concise, actionable, and grounded in the project context provided below. "
            "Help the team with engineering calculations, part recommendations, task updates, and meeting prep."
        )
        context = get_full_context()
        prompt = f"Project Context:\n{context}\n\nUser Identity: {sender}\nQuestion: {query_text}"
        
        try:
            response = client.models.generate_content(
                model='gemini-3.1-flash-lite',
                contents=prompt,
                config={'system_instruction': system_instruction}
            )
            return response.text
        except Exception:
            response = client.models.generate_content(
                model='gemini-3-flash-preview',
                contents=prompt,
                config={'system_instruction': system_instruction}
            )
            return response.text
    except Exception as e:
        print(f"Gemini API error: {e}")
        return None

def fallback_answer(sender, query_text):
    q = query_text.lower()
    if 'task' in q:
        return (
            f"Hi **{sender}**! 👋 Active deliverables from project roadmap:\n"
            "• **Aron**: Prepare Innovation Challenge budget justification ($1,200-$2,000 target)\n"
            "• **Eli**: Check parts inventory & bench-test 12V peristaltic dosing pumps\n"
            "• **Shyam**: Track sprint deadlines and Gantt chart milestones\n"
            "• **Ro**: AI integration, documentation, and minutes sync"
        )
    if any(w in q for w in ['meeting', 'tomorrow', 'today', 'innovation']):
        return (
            "⏰ **TACTICAL EVENT ALERT**:\n\n"
            "• **Event**: CEAS Tribunal Innovation Challenge First Info Meeting\n"
            "• **When**: **TODAY (Wednesday, Sept 2) @ 5:30 PM**\n"
            "• **Where**: **Kautz Attic (Lindner Hall / COB room 4350)**\n"
            "• **Food**: Free Panda Express! 🥡\n"
            "• **Action**: Submit the registration form in the Teams chat!"
        )
    if any(w in q for w in ['budget', 'cost', 'bom']):
        return (
            "💰 **FINANCIAL TELEMETRY**:\n\n"
            "• **Prototype Target**: ~$300.00\n"
            "• **Total Cap**: < $1,000.00\n"
            "• **BOM Breakdown**: Mechanical ($120), Fluidics/Pumps ($90), Electronics/MCU ($90), Acrylic Enclosure ($80)"
        )
    if any(w in q for w in ['grant', 'funding']):
        return (
            "🏆 **CAPITAL RECONNAISSANCE**:\n\n"
            "1. UC Innovation Challenge ($1,200-$2,000) — Meeting TODAY @ 5:30 PM\n"
            "2. UC 1819 Venture Lab ($5,000-$10,000 non-dilutive prototype grant)\n"
            "3. Main Street Ventures (Up to $5,000 student startup grant)\n"
            "4. VentureWell E-Team ($5,000 national collegiate award)\n"
            "5. CEAS Department Hardware Reimbursement ($250-$1,000)"
        )
    if any(w in q for w in ['mechanism', 'elevator', 'carousel', 'cad']):
        return (
            "📐 **HARDWARE ARCHITECTURE**:\n\n"
            "• **Mechanism**: Lead Screw Vertical Elevator (Concept A) vs Rotary Carousel (Concept B)\n"
            "• **Fluidics**: 4x 12V Peristaltic Pumps (food-grade dosing, zero motor contact)\n"
            "• **Viewing**: Clear side acrylic showcase for Expo actuation demo"
        )
    return (
        f"Hi **{sender}**! 🤖 J.A.R.V.I.S. core active. "
        "Ask me any engineering calculation, budget detail, or meeting question!"
    )

@app.route('/')
def home():
    curr_dir = os.path.dirname(os.path.abspath(__file__))
    idx_path = os.path.join(curr_dir, 'index.html')
    if os.path.exists(idx_path):
        try:
            with open(idx_path, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception:
            pass
    return render_template_string(HTML_TEMPLATE)

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json(force=True, silent=True) or {}
        sender = data.get('sender', 'Operator')
        message = data.get('message', '')
        
        reply = query_gemini_ai(sender, message)
        if not reply:
            reply = fallback_answer(sender, message)
        return jsonify({'reply': reply})
    except Exception as e:
        return jsonify({'reply': f"⚠️ Telemetry error: {str(e)}"})

@app.route('/api/status', methods=['GET'])
def status():
    return jsonify({'status': 'ONLINE', 'system': 'J.A.R.V.I.S. HUD', 'version': '3.6.1'})

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5050))
    app.run(host='0.0.0.0', port=port)
