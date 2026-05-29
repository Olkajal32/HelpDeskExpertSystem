PROBLEM_CATEGORIES = {
    "internet":    "Internet Not Working",
    "slow_system": "System Running Slow",
    "software":    "Software / Application Issue",
    "login":       "Login / Password Problem",
    "printer":     "Printer Not Working",
    "blue_screen": "Blue Screen / System Crash",
    "virus":       "Virus / Malware Suspected",
    "email":       "Email Not Working",
    "hardware":    "Hardware / Device Not Detected",
    "sound":       "No Sound / Audio Issue",
}

KNOWLEDGE_BASE = {

    "internet": {
        "questions": [
            ("router_on",        "Is the router/modem powered ON with stable indicator lights?"),
            ("other_device",     "Can other devices (phone/tablet) connect to the internet fine?"),
            ("browser_err",      "Do you see a browser error message (e.g. DNS_PROBE_FINISHED)?"),
            ("recently_changed", "Was any network setting or cable changed recently?"),
        ],
        "rules": [
            {
                "conditions": {"router_on": "no"},
                "solution": (
                    "SOLUTION - Router/Modem Off or Unstable\n"
                    "=========================================\n"
                    "1. Turn the router OFF, wait 30 seconds, turn back ON.\n"
                    "2. Check all cables (power + LAN/WAN) are firmly connected.\n"
                    "3. Wait 2 minutes for the router to fully boot up.\n"
                    "4. If the issue persists, contact your ISP helpline."
                ),
            },
            {
                "conditions": {"router_on": "yes", "other_device": "yes"},
                "solution": (
                    "SOLUTION - Problem is with THIS Computer Only\n"
                    "=============================================\n"
                    "1. Open CMD and run: ipconfig /release then ipconfig /renew\n"
                    "2. Also run: netsh winsock reset (restart after this).\n"
                    "3. Forget the Wi-Fi network and reconnect with correct password.\n"
                    "4. Update or reinstall the network adapter driver."
                ),
            },
            {
                "conditions": {"router_on": "yes", "other_device": "no", "browser_err": "yes"},
                "solution": (
                    "SOLUTION - DNS / Browser Error Detected\n"
                    "========================================\n"
                    "1. Open CMD and run: ipconfig /flushdns\n"
                    "2. Change DNS to Google: 8.8.8.8 and 8.8.4.4\n"
                    "   (Network Adapter -> IPv4 Properties)\n"
                    "3. Disable any VPN or Proxy temporarily.\n"
                    "4. Try a different browser to isolate the issue."
                ),
            },
            {
                "conditions": {"recently_changed": "yes"},
                "solution": (
                    "SOLUTION - Recent Configuration Change\n"
                    "=======================================\n"
                    "1. Undo the recent network setting change.\n"
                    "2. Restore the LAN cable to its previous port.\n"
                    "3. Reconfigure the router with correct ISP credentials.\n"
                    "4. Use System Restore to revert to before the change."
                ),
            },
            {
                "conditions": {},
                "solution": (
                    "GENERAL INTERNET TROUBLESHOOTING\n"
                    "==================================\n"
                    "1. Restart your computer and router.\n"
                    "2. Run Windows Troubleshooter: Settings -> System -> Troubleshoot.\n"
                    "3. Check if ISP has an outage in your area.\n"
                    "4. Contact your ISP helpline for further support."
                ),
            },
        ],
    },

    "slow_system": {
        "questions": [
            ("startup_slow",  "Is the system slow mainly during startup / boot?"),
            ("ram_full",      "Do you see 'Low Memory' warnings or RAM above 90% in Task Manager?"),
            ("old_system",    "Is the system more than 4 years old?"),
            ("many_programs", "Do many programs run in the background automatically?"),
        ],
        "rules": [
            {
                "conditions": {"startup_slow": "yes", "many_programs": "yes"},
                "solution": (
                    "SOLUTION - Too Many Startup Programs\n"
                    "=====================================\n"
                    "1. Ctrl+Shift+Esc -> Task Manager -> Startup tab.\n"
                    "2. Disable unnecessary startup programs.\n"
                    "3. Uninstall unused applications via Control Panel.\n"
                    "4. Run Disk Cleanup (search in Start menu)."
                ),
            },
            {
                "conditions": {"ram_full": "yes", "old_system": "no"},
                "solution": (
                    "SOLUTION - High RAM / Memory Usage\n"
                    "====================================\n"
                    "1. Close unused browser tabs and background apps.\n"
                    "2. In Task Manager, end high-memory processes.\n"
                    "3. Increase Virtual Memory: System -> Advanced -> Performance.\n"
                    "4. Consider upgrading RAM if this is a frequent issue."
                ),
            },
            {
                "conditions": {"old_system": "yes"},
                "solution": (
                    "SOLUTION - Aging Hardware\n"
                    "=========================\n"
                    "1. Replace HDD with an SSD for a major speed improvement.\n"
                    "2. Add more RAM if expansion slots are available.\n"
                    "3. Reinstall Windows for a clean, fresh environment.\n"
                    "4. Consult IT support about hardware upgrade options."
                ),
            },
            {
                "conditions": {},
                "solution": (
                    "GENERAL SLOW SYSTEM TIPS\n"
                    "=========================\n"
                    "1. Restart your PC to clear RAM and refresh processes.\n"
                    "2. Check for and install Windows Updates.\n"
                    "3. Run: sfc /scannow in CMD (as Administrator).\n"
                    "4. Run a full antivirus scan for hidden malware."
                ),
            },
        ],
    },

    "software": {
        "questions": [
            ("crashes",            "Does the application crash or freeze when you open it?"),
            ("error_code",         "Is there a specific error code or message shown?"),
            ("recently_installed", "Was the software recently installed or updated?"),
            ("compatibility",      "Are you using an older software version on a new OS?"),
        ],
        "rules": [
            {
                "conditions": {"recently_installed": "yes", "crashes": "yes"},
                "solution": (
                    "SOLUTION - Newly Installed / Updated Software Crashing\n"
                    "=======================================================\n"
                    "1. Uninstall and download the latest stable version.\n"
                    "2. Run installer as Administrator (right-click -> Run as Admin).\n"
                    "3. Disable antivirus temporarily during installation.\n"
                    "4. Check the vendor website for known bugs or patches."
                ),
            },
            {
                "conditions": {"error_code": "yes"},
                "solution": (
                    "SOLUTION - Error Code / Message Shown\n"
                    "======================================\n"
                    "1. Search the error code on the vendor support page.\n"
                    "2. Check Event Viewer: Win+R -> eventvwr -> Application Logs.\n"
                    "3. Reinstall required runtimes (Visual C++, .NET Framework).\n"
                    "4. Report the error code to IT support for analysis."
                ),
            },
            {
                "conditions": {"compatibility": "yes"},
                "solution": (
                    "SOLUTION - Compatibility Issue\n"
                    "================================\n"
                    "1. Right-click app -> Properties -> Compatibility tab.\n"
                    "2. Enable 'Run in compatibility mode' for an older OS.\n"
                    "3. Check for an updated version supporting your current OS.\n"
                    "4. Use a virtual machine as a workaround."
                ),
            },
            {
                "conditions": {},
                "solution": (
                    "GENERAL SOFTWARE TROUBLESHOOTING\n"
                    "==================================\n"
                    "1. Restart the application and try again.\n"
                    "2. Ensure the OS and software are up to date.\n"
                    "3. Perform a clean uninstall then reinstall.\n"
                    "4. Raise an IT ticket with the app name and version."
                ),
            },
        ],
    },

    "login": {
        "questions": [
            ("forgot_pass",    "Did you forget your password?"),
            ("account_locked", "Is there a message saying the account is locked?"),
            ("new_system",     "Is this a new computer or a first-time login attempt?"),
            ("caps_lock",      "Is the Caps Lock key accidentally turned ON?"),
        ],
        "rules": [
            {
                "conditions": {"caps_lock": "yes"},
                "solution": (
                    "SOLUTION - Caps Lock Issue\n"
                    "===========================\n"
                    "1. Press Caps Lock to turn it OFF.\n"
                    "2. Re-enter your password carefully - it is case-sensitive.\n"
                    "3. Check the keyboard indicator light before typing."
                ),
            },
            {
                "conditions": {"forgot_pass": "yes", "account_locked": "no"},
                "solution": (
                    "SOLUTION - Forgotten Password\n"
                    "==============================\n"
                    "1. Use the 'Forgot Password' link on the login screen.\n"
                    "2. Contact IT Help Desk to reset your password.\n"
                    "3. For Windows local account: use Admin account in Safe Mode.\n"
                    "4. Verify your identity per your organization policy."
                ),
            },
            {
                "conditions": {"account_locked": "yes"},
                "solution": (
                    "SOLUTION - Account Locked\n"
                    "==========================\n"
                    "1. Wait 15-30 minutes - accounts often auto-unlock after timeout.\n"
                    "2. Contact IT Help Desk for manual unlock.\n"
                    "3. Do NOT retry login until IT confirms the account is unlocked.\n"
                    "4. After unlock, immediately set a new strong password."
                ),
            },
            {
                "conditions": {"new_system": "yes"},
                "solution": (
                    "SOLUTION - First-Time / New System Login\n"
                    "=========================================\n"
                    "1. Use default credentials provided by IT during setup.\n"
                    "2. Ensure you are connected to the organization network/VPN.\n"
                    "3. Contact IT to verify your account exists on this machine.\n"
                    "4. Confirm whether domain login or local account is needed."
                ),
            },
            {
                "conditions": {},
                "solution": (
                    "GENERAL LOGIN TROUBLESHOOTING\n"
                    "==============================\n"
                    "1. Double-check the username spelling.\n"
                    "2. Try a different keyboard to rule out hardware issues.\n"
                    "3. Contact IT Help Desk with your employee / student ID.\n"
                    "4. For OS login issues, boot from a recovery drive."
                ),
            },
        ],
    },

    "printer": {
        "questions": [
            ("printer_on",  "Is the printer powered ON and showing a Ready status?"),
            ("connected",   "Is the printer properly connected (USB or network)?"),
            ("paper_jam",   "Is there a paper jam or a paper-related warning on the printer?"),
            ("driver_issue","Was the printer driver recently updated or changed?"),
        ],
        "rules": [
            {
                "conditions": {"paper_jam": "yes"},
                "solution": (
                    "SOLUTION - Paper Jam\n"
                    "=====================\n"
                    "1. Turn the printer OFF before removing jammed paper.\n"
                    "2. Gently pull the paper in the direction of paper travel.\n"
                    "3. Check all trays and the rear panel for stuck paper.\n"
                    "4. Turn back ON and run a test print."
                ),
            },
            {
                "conditions": {"printer_on": "no"},
                "solution": (
                    "SOLUTION - Printer Not Powered\n"
                    "================================\n"
                    "1. Check the power cable connection.\n"
                    "2. Press the power button firmly.\n"
                    "3. Test the power outlet with another device.\n"
                    "4. Try a different power cable."
                ),
            },
            {
                "conditions": {"connected": "no"},
                "solution": (
                    "SOLUTION - Printer Not Connected\n"
                    "==================================\n"
                    "1. USB: Unplug and replug the cable; try a different port.\n"
                    "2. Network: Ensure printer and PC are on the same Wi-Fi.\n"
                    "3. Remove and re-add the printer in Devices and Printers.\n"
                    "4. Ping the printer IP address to verify connectivity."
                ),
            },
            {
                "conditions": {"driver_issue": "yes"},
                "solution": (
                    "SOLUTION - Printer Driver Issue\n"
                    "=================================\n"
                    "1. Device Manager -> Printers -> Uninstall driver.\n"
                    "2. Download latest driver from the manufacturer website.\n"
                    "3. Install driver and restart the system.\n"
                    "4. Set as Default Printer after reinstallation."
                ),
            },
            {
                "conditions": {},
                "solution": (
                    "GENERAL PRINTER TROUBLESHOOTING\n"
                    "=================================\n"
                    "1. Restart the printer and computer.\n"
                    "2. Clear print queue: Services -> Print Spooler -> Restart.\n"
                    "3. Run Windows Printer Troubleshooter.\n"
                    "4. Contact IT if it is a shared network printer."
                ),
            },
        ],
    },

    "blue_screen": {
        "questions": [
            ("error_code",   "Did you note the STOP error code shown on the blue screen?"),
            ("after_update", "Did the BSOD start after a Windows or driver update?"),
            ("hardware_new", "Was new hardware (RAM, GPU, HDD) installed recently?"),
            ("frequent",     "Does the blue screen occur more than once a day?"),
        ],
        "rules": [
            {
                "conditions": {"after_update": "yes"},
                "solution": (
                    "SOLUTION - Blue Screen After Update\n"
                    "=====================================\n"
                    "1. Boot into Safe Mode (press F8 at startup).\n"
                    "2. Uninstall the update: Settings -> Update -> History -> Uninstall.\n"
                    "3. Roll back the updated driver via Device Manager.\n"
                    "4. Use System Restore to revert to before the update."
                ),
            },
            {
                "conditions": {"hardware_new": "yes"},
                "solution": (
                    "SOLUTION - New Hardware Causing Crash\n"
                    "======================================\n"
                    "1. Remove the newly installed hardware and retest.\n"
                    "2. Reseat RAM sticks firmly in their slots.\n"
                    "3. Run Memory Diagnostic: Win+R -> mdsched.exe\n"
                    "4. Verify hardware compatibility with your system specs."
                ),
            },
            {
                "conditions": {"frequent": "yes"},
                "solution": (
                    "SOLUTION - Frequent Crashes\n"
                    "============================\n"
                    "1. Run sfc /scannow and chkdsk /f /r in CMD (Admin).\n"
                    "2. Check disk health using CrystalDiskInfo.\n"
                    "3. Back up data IMMEDIATELY.\n"
                    "4. Contact IT for OS repair or reinstallation."
                ),
            },
            {
                "conditions": {},
                "solution": (
                    "GENERAL BSOD TROUBLESHOOTING\n"
                    "==============================\n"
                    "1. Boot into Safe Mode and check for driver issues.\n"
                    "2. Run a full malware scan.\n"
                    "3. Check system temperature - overheating causes crashes.\n"
                    "4. Contact IT with the error code and crash time."
                ),
            },
        ],
    },

    "virus": {
        "questions": [
            ("pop_ups",      "Are you seeing unexpected pop-ups or browser redirects?"),
            ("slow_after",   "Did the system slow down suddenly after visiting a site or opening an email?"),
            ("antivirus_on", "Do you have an active and updated antivirus program installed?"),
            ("data_missing", "Are files missing or renamed with unknown extensions (.locked, .crypt)?"),
        ],
        "rules": [
            {
                "conditions": {"data_missing": "yes"},
                "solution": (
                    "SOLUTION - Possible Ransomware Detected!\n"
                    "==========================================\n"
                    "1. IMMEDIATELY disconnect from the internet and all networks.\n"
                    "2. Do NOT pay the ransom - contact IT Security team NOW.\n"
                    "3. Restore files from the latest clean backup.\n"
                    "4. Format and reinstall the OS completely."
                ),
            },
            {
                "conditions": {"pop_ups": "yes", "antivirus_on": "no"},
                "solution": (
                    "SOLUTION - Adware / No Antivirus Protection\n"
                    "=============================================\n"
                    "1. Install a reputable antivirus (Windows Defender, Malwarebytes).\n"
                    "2. Run a full system scan immediately.\n"
                    "3. Remove suspicious browser extensions.\n"
                    "4. Reset browser settings to default."
                ),
            },
            {
                "conditions": {"slow_after": "yes", "antivirus_on": "yes"},
                "solution": (
                    "SOLUTION - Infection Despite Active Antivirus\n"
                    "==============================================\n"
                    "1. Update antivirus definitions and run a full scan.\n"
                    "2. Boot into Safe Mode and scan again.\n"
                    "3. Use Malwarebytes as a second-opinion scanner.\n"
                    "4. Check Task Manager Startup tab for suspicious entries."
                ),
            },
            {
                "conditions": {},
                "solution": (
                    "GENERAL VIRUS / MALWARE RESPONSE\n"
                    "==================================\n"
                    "1. Disconnect from the internet immediately.\n"
                    "2. Run a full antivirus scan.\n"
                    "3. Back up important data to an external drive.\n"
                    "4. Report the incident to your IT security team."
                ),
            },
        ],
    },

    "email": {
        "questions": [
            ("cant_send",    "Are you unable to SEND emails (outbox stuck or error on send)?"),
            ("cant_receive", "Are you unable to RECEIVE emails (inbox not updating)?"),
            ("wrong_config", "Was the email account recently set up or were settings changed?"),
            ("web_works",    "Does email work on browser-based webmail?"),
        ],
        "rules": [
            {
                "conditions": {"web_works": "yes", "cant_send": "yes"},
                "solution": (
                    "SOLUTION - Desktop Client Send Issue (Webmail Works)\n"
                    "=====================================================\n"
                    "1. Verify SMTP settings: smtp.yourdomain.com, Port 587, STARTTLS.\n"
                    "2. Re-enter your password in the email client account settings.\n"
                    "3. Temporarily disable antivirus email scanning feature.\n"
                    "4. Repair email profile: Control Panel -> Mail -> Repair."
                ),
            },
            {
                "conditions": {"cant_receive": "yes", "web_works": "no"},
                "solution": (
                    "SOLUTION - Cannot Receive Emails (Server-Side Issue)\n"
                    "======================================================\n"
                    "1. Contact email administrator - mail server may be down.\n"
                    "2. Check your spam / junk folder.\n"
                    "3. Verify IMAP / POP3 server settings.\n"
                    "4. Check mailbox quota - a full mailbox blocks new mail."
                ),
            },
            {
                "conditions": {"wrong_config": "yes"},
                "solution": (
                    "SOLUTION - Misconfigured Email Settings\n"
                    "========================================\n"
                    "1. Remove and re-add the email account.\n"
                    "2. Use auto-discover settings if supported.\n"
                    "3. Get correct settings from IT: IMAP=993(SSL), SMTP=587(TLS).\n"
                    "4. Ensure the password stored in the client is current."
                ),
            },
            {
                "conditions": {},
                "solution": (
                    "GENERAL EMAIL TROUBLESHOOTING\n"
                    "==============================\n"
                    "1. Restart your email client.\n"
                    "2. Check your internet connection.\n"
                    "3. Verify credentials with IT if password was recently changed.\n"
                    "4. Contact IT Help Desk with the exact error message."
                ),
            },
        ],
    },

    "hardware": {
        "questions": [
            ("usb_device",    "Is the device a USB device (pen drive, mouse, keyboard, etc.)?"),
            ("device_sound",  "Does the PC make a sound when the device is plugged in?"),
            ("works_other",   "Does the device work correctly on another computer?"),
            ("driver_missing","Is there a yellow (!) mark in Device Manager for this device?"),
        ],
        "rules": [
            {
                "conditions": {"usb_device": "yes", "device_sound": "no"},
                "solution": (
                    "SOLUTION - USB Device Not Recognized\n"
                    "======================================\n"
                    "1. Try a different USB port on the same computer.\n"
                    "2. Try a different USB cable.\n"
                    "3. Device Manager -> Scan for hardware changes.\n"
                    "4. Update USB controller drivers."
                ),
            },
            {
                "conditions": {"works_other": "no"},
                "solution": (
                    "SOLUTION - Device Itself is Faulty\n"
                    "====================================\n"
                    "1. The hardware device appears to be defective.\n"
                    "2. Check warranty status and arrange replacement.\n"
                    "3. Confirm failure on a third machine.\n"
                    "4. Contact vendor for RMA (Return Merchandise Authorization)."
                ),
            },
            {
                "conditions": {"driver_missing": "yes"},
                "solution": (
                    "SOLUTION - Missing / Corrupt Driver\n"
                    "=====================================\n"
                    "1. Device Manager -> right-click device -> Update Driver.\n"
                    "2. Download driver from the manufacturer official website.\n"
                    "3. Uninstall device entry and reboot - Windows reinstalls it.\n"
                    "4. Check Windows Update for optional driver updates."
                ),
            },
            {
                "conditions": {},
                "solution": (
                    "GENERAL HARDWARE TROUBLESHOOTING\n"
                    "==================================\n"
                    "1. Restart the computer with the device connected.\n"
                    "2. Check Device Manager for unknown devices.\n"
                    "3. Test the device on another system to isolate the problem.\n"
                    "4. Contact IT for internal hardware issues."
                ),
            },
        ],
    },

    "sound": {
        "questions": [
            ("muted",        "Is the volume muted or set to zero in the system taskbar?"),
            ("headphone",    "Are you using headphones or external speakers?"),
            ("after_update", "Did audio stop working after a Windows or driver update?"),
            ("device_shown", "Is the audio device visible in Device Manager without any errors?"),
        ],
        "rules": [
            {
                "conditions": {"muted": "yes"},
                "solution": (
                    "SOLUTION - System is Muted\n"
                    "===========================\n"
                    "1. Click the speaker icon in the taskbar and unmute.\n"
                    "2. Right-click speaker -> Open Volume Mixer -> check all channels.\n"
                    "3. Check application-specific volume in Volume Mixer."
                ),
            },
            {
                "conditions": {"headphone": "yes", "muted": "no"},
                "solution": (
                    "SOLUTION - Headphone / External Speaker Issue\n"
                    "==============================================\n"
                    "1. Unplug and re-plug the headphone or speaker firmly.\n"
                    "2. Right-click speaker -> Sounds -> Playback -> set correct output as Default.\n"
                    "3. Try a different audio jack (front vs rear panel).\n"
                    "4. Test the headphone on another device."
                ),
            },
            {
                "conditions": {"after_update": "yes"},
                "solution": (
                    "SOLUTION - Audio Broken After Update\n"
                    "=====================================\n"
                    "1. Device Manager -> Sound -> Roll Back Driver.\n"
                    "2. Uninstall audio driver and reboot (Windows reinstalls it).\n"
                    "3. Download audio driver from the manufacturer site.\n"
                    "4. Uninstall the recent Windows Update via Update History."
                ),
            },
            {
                "conditions": {"device_shown": "no"},
                "solution": (
                    "SOLUTION - Audio Device Not Detected\n"
                    "======================================\n"
                    "1. Scan for Hardware Changes in Device Manager.\n"
                    "2. Check if audio is disabled in BIOS settings.\n"
                    "3. Install the correct audio driver for your hardware.\n"
                    "4. Contact IT - the audio hardware may have failed."
                ),
            },
            {
                "conditions": {},
                "solution": (
                    "GENERAL AUDIO TROUBLESHOOTING\n"
                    "==============================\n"
                    "1. Run Windows Audio Troubleshooter: Settings -> Troubleshoot.\n"
                    "2. Restart Windows Audio: services.msc -> Windows Audio -> Restart.\n"
                    "3. Update audio drivers to the latest version.\n"
                    "4. Check all physical cable connections."
                ),
            },
        ],
    },
}
