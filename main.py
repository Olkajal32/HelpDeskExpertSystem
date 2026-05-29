import sys
try:
    import tkinter as tk
except ImportError:
    print("ERROR: tkinter is not installed.")
    print("On Linux run:  sudo apt-get install python3-tk")
    sys.exit(1)

from ui import HelpDeskApp


def main():
    app = HelpDeskApp()
    app.mainloop()


if __name__ == "__main__":
    main()
