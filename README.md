# 🩺 AMU Ultrasound Tracker

A lightweight, Streamlit-based web application designed to eliminate equipment loss and reduce clinical downtime on the Acute Medical Unit (AMU).

## 🏥 Clinical Context
In busy medical environments, portable diagnostic equipment (like ultrasound machines) is frequently moved between wards for bedside procedures (e.g., US-guided cannulation, pleural drains). A common point of failure is the lack of real-time visibility, leading to clinicians wasting time searching for equipment during emergencies.

This project implements a **"Scan-to-Log"** workflow using QR codes to ensure the last known location of the ultrasound is always accessible to the multidisciplinary team.

## 🚀 Key Features
- **Real-Time Localization:** Instant visibility of the machine's current ward or bay.
- **Minimal Friction UI:** Designed for high-pressure environments—updates take <10 seconds.
- **Audit Trail:** Maintains a permanent history of equipment movement for Clinical Governance and QI analysis.
- **Home-Base Logic:** One-touch "Return to AMU" button to encourage proper equipment docking.
- **Clean Interface:** Custom CSS used to hide developer toolbars for a bespoke, "Trust-approved" feel.

## 🛠️ Technical Stack
- **Frontend/Backend:** [Streamlit](https://streamlit.io/) (Python)
- **Database:** SQLite (Persistent relational storage)
- **Data Handling:** Pandas
- **Deployment:** Streamlit Community Cloud (linked via GitHub)
