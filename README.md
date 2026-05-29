# HelpDeskExpertSystem
#A Help Desk Expert System is a knowledge-based AI application that automates technical support by replicating the problem-solving capabilities of a human IT specialist.
#It is an AI-powered, production-ready desktop application designed to diagnose and resolve common IT problems automatically. Using a production rule-based approach, the system mimics a human IT specialist by asking up to four targeted diagnostic questions to pinpoint technical issues and recommend instant solutions

#Features:
* **Interactive Category Selection:** Includes dedicated diagnostic tracks for common enterprise IT issues:
  * Internet & Email Connectivity
  * System Performance & Crashes (Blue Screen)
  * Hardware, Devices, & Audio Issues
  * Login, Password, & Software Issues
  * Printers, Viruses, and Malware Suspicions
* **Dynamic 4-Question Diagnostics:** Utilizes an inference engine to evaluate user symptoms using a maximum of 4 targeted "Yes/No" questions.
* **Instant Recommended Solutions:** Generates comprehensive, step-by-step resolution steps that can be copied directly to the clipboard with a single click.
* **State Reset:** A one-click "Reset / Home" mechanism to instantly clear the inference state and start a new evaluation.

## Project Architeture

##The project follows a highly modular, clean architectural separation of concerns:

```text
├── knowledge_base.py     # Data Layer: Contains IT domain facts and complex "If-Then" rules
├── inference_engine.py   # Brain Layer: Processes user logic and drives the question routing
├── ui.py                 # Presentation Layer: Custom graphical interface with a sleek dark theme
├── main.py               # Orchestrator: App entry point tying UI and Inference logic together
└── requirement.txt       # Dependencies: Required manifest packages for running the app
