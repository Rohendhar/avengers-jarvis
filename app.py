"""
J.A.R.V.I.S. High-Performance Core Engine & 24/7 Autonomous Cloud Scheduler
Integrates real-time document search, Gemini AI, and autonomous cloud reminders.
"""

import os
import sys
import json
import time
import threading
import smtplib
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv

CURR_DIR = os.path.dirname(os.path.abspath(__file__))
if os.path.exists(os.path.join(CURR_DIR, "Meeting Notes")) or os.path.exists(os.path.join(CURR_DIR, "Funding")):
    LOCAL_ROOT = CURR_DIR
else:
    LOCAL_ROOT = os.path.abspath(os.path.join(CURR_DIR, "..", ".."))

load_dotenv(os.path.join(LOCAL_ROOT, ".env"))

app = Flask(__name__, template_folder=os.path.join(LOCAL_ROOT, "templates") if os.path.exists(os.path.join(LOCAL_ROOT, "templates")) else "templates")

# Team Roster Configuration
DEFAULT_ROSTER = {
    "team": [
        {"name": "Ro", "email": "rohendrr@mail.uc.edu", "role": "Documentation & AI Integration"},
        {"name": "Aron", "email": "josepha7@mail.uc.edu", "role": "Budget, Finance & Procurement"},
        {"name": "Eli", "email": "radabaer@mail.uc.edu", "role": "Hardware & Component Inventory"},
        {"name": "Shyam", "email": "patel8s7@mail.uc.edu", "role": "Timeline & Gantt Architecture"}
    ]
}

# Master Cloud Scheduled Reminders
CLOUD_SCHEDULED_JOBS = [
    {
        "id": "tonight_urgent_docs_deadline",
        "target_time": datetime(2026, 9, 2, 21, 0, 0),
        "subject": "🚨 URGENT ACTION: Complete Student-Initiated Document & Innovation Challenge Form Tonight!",
        "message": (
            "Hi Team,\n\n"
            "This is an automated evening reminder that two critical course deliverables are due TONIGHT:\n\n"
            "1. Student-Initiated Project Document (Course sign-off from Prof. Jacob Cress)\n"
            "2. Innovation Challenge Registration Form (Submit via Teams chat)\n\n"
            "Please confirm once submitted so we stay 100% on schedule!"
        ),
        "dispatched": False
    },
    {
        "id": "eli_inventory_checklist_1d",
        "target_time": datetime(2026, 9, 3, 9, 0, 0),
        "subject": "Reminder: Component Inventory Checklist Due Tomorrow (Friday, Sept 4)",
        "message": (
            "Hi Team (Eli),\n\n"
            "This is an automated 24-hour reminder that the Component Inventory & Staging Checklist is due tomorrow, Friday, September 4, on Google Drive.\n\n"
            "This document logs all available motors, pumps, tubing, and electronics so Aron can build our Purchase Request Excel for the 1819 Makerspace reimbursement."
        ),
        "dispatched": False
    },
    {
        "id": "pitch_video_1w_before",
        "target_time": datetime(2026, 9, 23, 9, 0, 0),
        "subject": "📅 1-WEEK ALERT: 5-Minute Pitch Deck Video Due Sept 30 ($150 Stipend)",
        "message": (
            "Hi Team,\n\n"
            "This is our 1-WEEK countdown reminder for Milestone 1 of the CEAS Innovation Challenge!\n\n"
            "🎯 Deliverable: 5-Minute Recorded Pitch Deck Video\n"
            "📅 Due Date: Wednesday, September 30, 2026 @ 11:59 PM\n"
            "💰 Reward: Unlocks the first $150.00 team stipend!\n\n"
            "Key Elements Required in Video:\n"
            "• Problem statement & target market (craft breweries & cigar lounges)\n"
            "• Product concept: Automated drink dispenser table (3-4 drinks proof-of-concept)\n"
            "• Technical subsystem architecture (cup elevator, peristaltic dosing, mini-fridge cooling)\n"
            "• Preliminary budget & BOM ($1,500 cap)"
        ),
        "dispatched": False
    },
    {
        "id": "pitch_video_1d_before",
        "target_time": datetime(2026, 9, 29, 9, 0, 0),
        "subject": "🚨 FINAL 24H ALERT: Submit 5-Minute Pitch Deck Video Tomorrow (Sept 30)",
        "message": (
            "Hi Team,\n\n"
            "Tomorrow is the deadline for Milestone 1 of the CEAS Innovation Challenge!\n\n"
            "🎯 Deliverable: 5-Minute Video Pitch Submission\n"
            "📅 Due Date: Wednesday, September 30, 2026\n"
            "💰 Payout: Unlocks our $150.00 stipend upon submission.\n\n"
            "Please ensure the recording is uploaded and submitted to the Canvas page before the midnight cutoff."
        ),
        "dispatched": False
    },
    {
        "id": "prototype_day_1w_before",
        "target_time": datetime(2026, 10, 28, 9, 0, 0),
        "subject": "📅 1-WEEK ALERT: Innovation Challenge Prototype Day on Nov 4",
        "message": (
            "Hi Team,\n\n"
            "Prototype Day is exactly 1 WEEK away (Wednesday, November 4, 2026)!\n\n"
            "🎯 Milestone Requirement: In-person demonstration of our benchtop prototype.\n"
            "• At least one team member must attend with our benchtop rig.\n"
            "• Objective: Show the 3-4 drink dosing manifold and elevator mechanism in operation to the Innovation Challenge mentors."
        ),
        "dispatched": False
    },
    {
        "id": "prototype_day_1d_before",
        "target_time": datetime(2026, 11, 3, 9, 0, 0),
        "subject": "🚨 24H ALERT: Innovation Challenge Prototype Day Tomorrow (Nov 4)",
        "message": (
            "Hi Team,\n\n"
            "Tomorrow (Wednesday, November 4) is Prototype Day for the Innovation Challenge!\n\n"
            "Please confirm who will be transporting the benchtop test rig and representing the team at the showcase table."
        ),
        "dispatched": False
    },
    {
        "id": "final_competition_1w_before",
        "target_time": datetime(2026, 11, 11, 9, 0, 0),
        "subject": "🏆 1-WEEK ALERT: Innovation Challenge Final Competition on Nov 18 ($150 Stipend + Prizes)",
        "message": (
            "Hi Team,\n\n"
            "The Final Competition & Gala is 1 WEEK away (Wednesday, November 18, 2026)!\n\n"
            "⚠️ ATTENDANCE MANDATORY: All team members must attend in person.\n"
            "💰 Stakes:\n"
            "• Unlocks second $150.00 active participation stipend ($300 total guaranteed)\n"
            "• $300.00 Top 25% placement bonus\n"
            "• 1st, 2nd, and 3rd place podium bonus prizes + ceremonial giant check!\n"
            "• Distribution of 100% material reimbursements from 1819 Makerspace."
        ),
        "dispatched": False
    },
    {
        "id": "final_competition_1d_before",
        "target_time": datetime(2026, 11, 17, 9, 0, 0),
        "subject": "🚨 TOMORROW: Innovation Challenge Final Competition (All Members Mandatory)",
        "message": (
            "Hi Team,\n\n"
            "Tomorrow, Wednesday, November 18, is the Final Competition!\n\n"
            "• All members are required to attend.\n"
            "• Dress code: Business casual.\n"
            "• Have the table, demo cups, and pitch deck loaded and ready.\n"
            "Let's bring home the win and secure our grant funding!"
        ),
        "dispatched": False
    }
]

def dispatch_cloud_email(subject, message):
    smtp_user = os.getenv("SMTP_EMAIL", "")
    smtp_pass = os.getenv("SMTP_PASSWORD", "")
    smtp_server = os.getenv("SMTP_SERVER", "smtp.gmail.com")
    smtp_port = int(os.getenv("SMTP_PORT", "587"))

    if not smtp_user or not smtp_pass:
        print("ℹ️ Cloud SMTP credentials not configured. Skipping email dispatch.")
        return False

    success = True
    for member in DEFAULT_ROSTER["team"]:
        email = member["email"]
        name = member["name"]
        try:
            msg = MIMEMultipart("alternative")
            msg["Subject"] = f"[Senior Design] {subject}"
            msg["From"] = f"Senior Design Bot <{smtp_user}>"
            msg["To"] = email

            plain = f"Hi {name},\n\n{message}\n\nBest regards,\nJ.A.R.V.I.S. Project Intelligence"
            html = f"""
            <div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; border: 1px solid #e2e8f0; border-radius: 8px; overflow: hidden;">
                <div style="background-color: #0f172a; color: #38bdf8; padding: 18px 24px; font-weight: bold; font-size: 18px;">
                    J.A.R.V.I.S. Mark VII // Automated Project Alert
                </div>
                <div style="padding: 24px; color: #1e293b; line-height: 1.6;">
                    <p style="font-size: 16px;">Hi <strong>{name}</strong>,</p>
                    <div style="background-color: #f8fafc; border-left: 4px solid #c00000; padding: 16px; border-radius: 4px; font-size: 15px;">
                        {message.replace(chr(10), '<br>')}
                    </div>
                    <hr style="border: 0; border-top: 1px solid #e2e8f0; margin: 24px 0 16px 0;">
                    <p style="font-size: 12px; color: #94a3b8;">
                        Dispatched 24/7 autonomously by J.A.R.V.I.S. Cloud Infrastructure.<br>
                        Timestamp: {datetime.now().strftime('%B %d, %Y at %I:%M %p EDT')}
                    </p>
                </div>
            </div>
            """
            msg.attach(MIMEText(plain, "plain", "utf-8"))
            msg.attach(MIMEText(html, "html", "utf-8"))

            with smtplib.SMTP(smtp_server, smtp_port, timeout=15) as server:
                server.ehlo()
                server.starttls()
                server.ehlo()
                server.login(smtp_user, smtp_pass)
                server.send_message(msg)
                print(f"✅ Cloud Email successfully sent to {email}")
        except Exception as e:
            print(f"❌ Cloud Email delivery failed for {email}: {e}")
            success = False
    return success

def execute_scheduler_checks():
    now_dt = datetime.now()
    dispatched_count = 0
    for job in CLOUD_SCHEDULED_JOBS:
        if not job["dispatched"] and now_dt >= job["target_time"]:
            print(f"🔔 [CLOUD TRIGGER] Executing Job: {job['id']} at {now_dt.strftime('%Y-%m-%d %H:%M:%S')}")
            dispatch_cloud_email(job["subject"], job["message"])
            job["dispatched"] = True
            dispatched_count += 1
    return dispatched_count

def cloud_scheduler_background_thread():
    print("🚀 J.A.R.V.I.S. Autonomous Cloud Scheduler Thread Active.")
    while True:
        try:
            execute_scheduler_checks()
        except Exception as e:
            print(f"Scheduler loop error: {e}")
        time.sleep(30)

# Start background scheduler thread on boot
threading.Thread(target=cloud_scheduler_background_thread, daemon=True).start()

def get_live_workspace_context():
    """Reads priority master project documents with strict size bounds for instant <4s latency."""
    context_sections = []
    
    priority_files = [
        ("Meeting Notes", "2026-09-02_Team_Meeting_Minutes.md"),
        ("Funding", "CEAS_Innovation_Challenge_Fall2026_Guide.md"),
        ("Timeline", "milestones.md"),
        ("Budget", "procurement_and_funding.md"),
        ("Architecture", "system_overview.md")
    ]
    
    for folder, fname in priority_files:
        p = os.path.join(LOCAL_ROOT, folder, fname)
        if os.path.exists(p):
            try:
                with open(p, "r", encoding="utf-8") as f:
                    context_sections.append(f"### [DOCUMENT: {folder}/{fname}]\n{f.read()[:2000]}")
            except Exception:
                pass

    return "\n\n".join(context_sections)

def query_gemini_ai(sender, query_text):
    api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
    if not api_key:
        return None
    try:
        from google import genai
        client = genai.Client(api_key=api_key)
        
        salutation = "Sir / Mr. Rohendhar" if sender.lower() in ["ro", "operator"] else f"Mr. {sender}"
        today_date_str = "Wednesday, September 2, 2026"
        current_time_str = datetime.now().strftime("%I:%M %p")
        
        system_instruction = (
            f"You are J.A.R.V.I.S., the brilliant, witty, and sophisticated AI operating system for Tony Stark, "
            f"now serving Project AVENGERS at the University of Cincinnati (MECH5051 / EECE5001).\n\n"
            f"TEMPORAL ANCHOR (CRITICAL):\n"
            f"- TODAY'S DATE IS: {today_date_str} ({current_time_str} EDT).\n\n"
            f"RULES OF CONDUCT:\n"
            f"1. You have direct access to all Project AVENGERS repository files below. Always reference them accurately.\n"
            f"2. Tone: Refined British poise, sharp intelligence, concise and proactive with subtle dry humor.\n"
            f"3. When answering engineering questions, provide real formulas, torque, or flow specs."
        )
        
        context_data = get_live_workspace_context()
        prompt = (
            f"ACTIVE PROJECT REPOSITORY DOCUMENTS:\n{context_data}\n\n"
            f"OPERATOR: {sender}\n"
            f"QUERY: {query_text}"
        )
        
        for candidate in ["gemini-flash-latest", "gemini-3.1-flash-lite"]:
            try:
                t0 = time.time()
                resp = client.models.generate_content(
                    model=candidate,
                    contents=prompt,
                    config={"system_instruction": system_instruction}
                )
                if resp and resp.text:
                    print(f"[{candidate}] answered in {time.time()-t0:.2f}s")
                    return resp.text
            except Exception as ex:
                continue
                
    except Exception as e:
        print(f"Gemini API error: {e}")
    return None

def fallback_answer(sender, query_text):
    q = query_text.lower()
    salutation = "Sir" if sender.lower() in ["ro", "operator"] else sender
    if any(w in q for w in ["meeting", "today", "notes"]):
        return (
            f"Good evening, **{salutation}**. Yes, there was an official team meeting **TODAY, Wednesday, September 2, 2026**!\n\n"
            "### 📋 Key Decisions & Urgent Action Items:\n"
            "• **Venue & Positioning**: Craft breweries and cigar lounges as a hospitality amenity.\n"
            "• **Phase 1 Scope**: 3–4 non-carbonated drinks proof of concept.\n"
            "• **Thermal Management (Plan B)**: Mini-fridge insert structure.\n"
            "• **Budget**: Cap raised to **$1,500.00**.\n"
            "• **Action Items Tonight**: Submit Innovation Challenge form & Student-Initiated Project Document."
        )
    return f"At your service, **{salutation}**. J.A.R.V.I.S. neural core is running online."

@app.route("/")
def home():
    for p in [os.path.join(LOCAL_ROOT, "templates", "index.html"), os.path.join(LOCAL_ROOT, "index.html")]:
        if os.path.exists(p):
            try:
                with open(p, "r", encoding="utf-8") as f:
                    return f.read()
            except Exception:
                pass
    try:
        return render_template("index.html")
    except Exception as e:
        return f"<h3>J.A.R.V.I.S. Core Online: {e}</h3>"

@app.route("/api/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json(force=True, silent=True) or {}
        sender = data.get("sender", "Operator")
        message = data.get("message", "")
        
        reply = query_gemini_ai(sender, message)
        if not reply:
            reply = fallback_answer(sender, message)
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"reply": f"⚠️ J.A.R.V.I.S. Telemetry Error: {str(e)}"})

@app.route("/api/cron", methods=["GET", "POST"])
def cron_endpoint():
    """Heartbeat endpoint: keeps Render awake 24/7 and triggers any due scheduled emails."""
    dispatched = execute_scheduler_checks()
    return jsonify({
        "status": "HEARTBEAT_ACKNOWLEDGED",
        "system": "J.A.R.V.I.S. Mark VII",
        "dispatched_jobs": dispatched,
        "timestamp": datetime.now().isoformat()
    })

@app.route("/api/status", methods=["GET"])
def status():
    return jsonify({
        "status": "ONLINE",
        "system": "J.A.R.V.I.S. Mark VII",
        "team": "THE AVENGERS (UC Capstone)",
        "today": "Wednesday, September 2, 2026",
        "scheduler": "24/7 ACTIVE",
        "version": "7.4.0"
    })

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5050))
    app.run(host="0.0.0.0", port=port)
