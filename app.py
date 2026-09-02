"""
Jarvis Senior Design Web Chat Hub — Dynamic AI Backend
Combines project file knowledge retrieval with Google Gemini Generative AI for real, dynamic reasoning.
"""

import os
import sys
import json
import re
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

# Ensure safe utf-8 stdout on Windows
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

curr_dir = os.path.dirname(os.path.abspath(__file__))
if os.path.exists(os.path.join(curr_dir, "Architecture")):
    PROJECT_ROOT = curr_dir
else:
    PROJECT_ROOT = os.path.abspath(os.path.join(curr_dir, "..", ".."))
LOCAL_ROOT = PROJECT_ROOT
load_dotenv(os.path.join(LOCAL_ROOT, ".env"))

app = Flask(__name__, template_folder="templates")

def get_full_project_context():
    """Aggregates all project documentation for AI grounding."""
    docs = []
    for folder in ["Meeting Notes", "Architecture", "Budget", "Business", "Funding", "Organization", "Research", "Timeline"]:
        f_dir = os.path.join(LOCAL_ROOT, folder)
        if os.path.exists(f_dir):
            for file in os.listdir(f_dir):
                if file.endswith(".md"):
                    path = os.path.join(f_dir, file)
                    try:
                        with open(path, "r", encoding="utf-8") as f:
                            docs.append(f"=== {folder}/{file} ===\n{f.read()[:2000]}\n")
                    except Exception:
                        pass
    # Add roster
    r_path = os.path.join(LOCAL_ROOT, "Tools", "reminders", "team_roster.json")
    if os.path.exists(r_path):
        try:
            with open(r_path, "r", encoding="utf-8") as f:
                docs.append(f"=== Active Team Roster & Tasks ===\n{f.read()}\n")
        except Exception:
            pass
    return "\n".join(docs)

def query_gemini_ai(sender, query_text):
    """Calls Gemini API if key is available in .env."""
    api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
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
        
        context = get_full_project_context()
        prompt = f"Project Context:\n{context}\n\nUser Identity: {sender}\nQuestion: {query_text}"
        
        response = client.models.generate_content(
            model="gemini-3.1-flash-lite",
            contents=prompt,
            config={"system_instruction": system_instruction}
        )
        return response.text
    except Exception as e:
        print(f"⚠️ Gemini API query error: {e}")
        return None

def fallback_retrieval(sender, query_text):
    """Smart contextual answer if Gemini API key is not configured."""
    query = query_text.lower().strip()
    roster_path = os.path.join(LOCAL_ROOT, "Tools", "reminders", "team_roster.json")
    roster = {"team": []}
    if os.path.exists(roster_path):
        with open(roster_path, "r", encoding="utf-8") as f:
            roster = json.load(f)

    # 1. Tasks
    if any(w in query for w in ["my task", "my tasks", "what are my tasks", "what do i do"]):
        matched = next((m for m in roster.get("team", []) if m["name"].lower() == sender.lower()), None)
        if matched:
            tasks = matched.get("active_tasks", [])
            if tasks:
                bullets = "\n• " + "\n• ".join(tasks[:6])
                return f"Hi **{matched['name']}**! 👋 Here are your current active project tasks:{bullets}"
            return f"Hi **{matched['name']}**! You have no pending tasks right now."
        return f"Logged in as **{sender}**. Select your name from the dropdown to check assigned deliverables."

    for m in roster.get("team", []):
        m_name = m["name"].lower()
        if f"tasks for {m_name}" in query or f"{m_name}'s tasks" in query or f"{m_name} task" in query:
            tasks = m.get("active_tasks", [])
            if tasks:
                return f"📋 **Active Tasks for {m['name']}** ({m['role']}):\n• " + "\n• ".join(tasks[:6])

    # 2. Meeting
    if any(w in query for w in ["meeting", "tomorrow", "innovation challenge", "when", "time", "where", "location"]):
        return (
            "⏰ **Upcoming Meeting & Event Alert**:\n\n"
            "• **Event**: CEAS Tribunal Innovation Challenge First Info Session\n"
            "• **When**: **Wednesday, September 2 @ 5:30 PM**\n"
            "• **Where**: **Kautz Attic (Lindner Hall / COB room 4350)**\n"
            "• **Perks**: Free Panda Express provided! 🥡\n"
            "• **Funding Target**: **$1,200 – $2,000** for our Senior Design team.\n"
            "• ⚠️ **Action Required**: Please fill out the registration form in our Teams chat!"
        )

    # 3. Budget
    if any(w in query for w in ["budget", "cost", "bom", "price", "money", "spent"]):
        return (
            "💰 **Preliminary Budget & BOM Overview**:\n\n"
            "• **Initial Prototype Target**: **~$300.00**\n"
            "• **Total Project Ceiling**: **< $1,000.00**\n"
            "• **Breakdown**: Mechanical (~$120), Fluidics/Pumps (~$90), Electronics/MCU (~$90), Acrylic Enclosure (~$80).\n"
            "• **Finance Lead**: Aron (`josepha7@mail.uc.edu`)"
        )

    # 4. Funding
    if any(w in query for w in ["funding", "grant", "grants", "venture lab", "main street"]):
        return (
            "🏆 **Top Viable Funding Opportunities**:\n\n"
            "1. **UC Innovation Challenge**: $1,200–$2,000 (Kickoff tomorrow @ 5:30 PM)\n"
            "2. **UC 1819 Venture Lab**: $5,000–$10,000 non-dilutive prototype grant\n"
            "3. **Main Street Ventures**: Up to $5,000 local student founder grant\n"
            "4. **VentureWell E-Team**: $5,000 national collegiate STEM award\n"
            "5. **CEAS Department Capstone Grant**: $250–$1,000 lab reimbursement"
        )

    # 5. Mechanism
    if any(w in query for w in ["mechanism", "cad", "elevator", "carousel", "motor", "pump", "solenoid"]):
        return (
            "🔬 **Current Engineering Trade Study (Ideation Phase)**:\n\n"
            "• **Cup Handling**: Concept A (Lead Screw Elevator) vs Concept B (Rotary Carousel Indexer)\n"
            "• **Fluidics**: 12V Food-Grade Peristaltic Dosing Pumps (accurate ml dosing, no fluid contact with motor)\n"
            "• **Viewing Chamber**: Clear acrylic side-panel to highlight moving actuation during Senior Design Expo!"
        )

    # 6. Drive
    if any(w in query for w in ["drive", "google drive", "files", "link", "folder"]):
        return (
            "📂 **Project Google Drive Hub**:\n\n"
            "<a href='https://drive.google.com/drive/folders/1HixFp6gy4giz3lrETgw27XZ3tMVkiEs2?usp=drive_link' target='_blank'>Click here to open our Senior Design Google Drive</a>"
        )

    # Fallback
    return (
        f"Hi **{sender}**! 🤖 I'm **Jarvis**, your Senior Design AI.\n\n"
        f"You asked: *\"{query_text}\"*\n\n"
        "*(To enable unlimited open-ended reasoning, engineering calculations, and code generation, add your free Gemini API key to .env)*"
    )

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json(force=True, silent=True) or {}
    sender = data.get("sender", "Teammate")
    message = data.get("message", "")
    
    # Try real generative AI first
    ai_reply = query_gemini_ai(sender, message)
    if ai_reply:
        return jsonify({"reply": ai_reply})

    # Use structured retrieval if no API key
    reply = fallback_retrieval(sender, message)
    return jsonify({"reply": reply})

@app.route("/api/status", methods=["GET"])
def status():
    has_gemini = bool(os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY"))
    return jsonify({
        "project": "Automated Drink-Dispensing Table",
        "phase": "Phase 1: Ideation & Concept Exploration",
        "next_event": "CEAS Innovation Challenge Kickoff (Wed, Sept 2 @ 5:30 PM)",
        "prototype_budget": "$300.00",
        "ai_engine": "Gemini 2.5 Flash" if has_gemini else "Local Project Knowledge Engine"
    })

if __name__ == "__main__":
    port = 5050
    print(f"🚀 Jarvis Senior Design Web Hub running on http://0.0.0.0:{port}")
    app.run(host="0.0.0.0", port=port, debug=False)
