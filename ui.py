import tkinter as tk
from tkinter import ttk, messagebox

from knowledge_base import PROBLEM_CATEGORIES
from inference_engine import InferenceEngine


# ── Colour palette ───────────────────────────────────────────
BG_DARK   = "#1e2a38"   # window background
BG_CARD   = "#263545"   # card / panel background
BG_BTN    = "#2e7bcf"   # primary button blue
BG_BTN_HO = "#3a8fe8"   # hover
BG_YES    = "#27ae60"   # Yes button
BG_NO     = "#c0392b"   # No button
FG_WHITE  = "#ffffff"
FG_ACCENT = "#5dade2"   # section headings
FG_MUTED  = "#95a5a6"
FG_SOL    = "#d5f5e3"   # solution text colour

FONT_TITLE  = ("Segoe UI", 20, "bold")
FONT_HEAD   = ("Segoe UI", 11, "bold")
FONT_BODY   = ("Segoe UI", 10)
FONT_SMALL  = ("Segoe UI", 9)
FONT_MONO   = ("Courier New", 10)


class HelpDeskApp(tk.Tk):
    """Main application window."""

    def __init__(self):
        super().__init__()
        self.title("Help Desk Expert System")
        self.geometry("860x680")
        self.resizable(True, True)
        self.configure(bg=BG_DARK)
        self.engine: InferenceEngine | None = None
        self._build_ui()

    # ==========================================================
    # UI CONSTRUCTION
    # ==========================================================
    def _build_ui(self):
        # ── Title bar ─────────────────────────────────────────
        title_frame = tk.Frame(self, bg="#15202e", pady=14)
        title_frame.pack(fill="x")

        tk.Label(
            title_frame,
            text="  Help Desk Expert System",
            font=FONT_TITLE, bg="#15202e", fg=FG_WHITE,
        ).pack(side="left", padx=20)

        tk.Label(
            title_frame,
            text="AI-Based Diagnosis & Solutions",
            font=FONT_SMALL, bg="#15202e", fg=FG_MUTED,
        ).pack(side="right", padx=20)

        # ── Main layout: left panel + right panel ─────────────
        main = tk.Frame(self, bg=BG_DARK)
        main.pack(fill="both", expand=True, padx=14, pady=10)

        # LEFT: Problem category buttons
        self._build_left_panel(main)

        # RIGHT: Question + Solution area
        self._build_right_panel(main)

        # ── Status bar ────────────────────────────────────────
        self.status_var = tk.StringVar(value="Select a problem category to begin.")
        status = tk.Label(
            self, textvariable=self.status_var,
            bg="#15202e", fg=FG_MUTED,
            font=FONT_SMALL, anchor="w", padx=12, pady=4,
        )
        status.pack(fill="x", side="bottom")

    # ── Left panel ────────────────────────────────────────────
    def _build_left_panel(self, parent):
        frame = tk.Frame(parent, bg=BG_CARD, bd=0, width=220)
        frame.pack(side="left", fill="y", padx=(0, 10))
        frame.pack_propagate(False)

        tk.Label(
            frame, text="Problem Categories",
            font=FONT_HEAD, bg=BG_CARD, fg=FG_ACCENT, pady=10,
        ).pack(fill="x", padx=10)

        ttk.Separator(frame, orient="horizontal").pack(fill="x", padx=10)

        # One button per problem category
        self.cat_buttons = {}
        for key, label in PROBLEM_CATEGORIES.items():
            btn = tk.Button(
                frame, text=label,
                font=FONT_SMALL, bg=BG_DARK, fg=FG_WHITE,
                activebackground=BG_BTN, activeforeground=FG_WHITE,
                bd=0, pady=8, padx=10, anchor="w",
                cursor="hand2", wraplength=195,
                command=lambda k=key: self._start_session(k),
            )
            btn.pack(fill="x", padx=6, pady=3)
            self._bind_hover(btn)
            self.cat_buttons[key] = btn

        # Reset button at the bottom
        tk.Frame(frame, bg=BG_CARD).pack(expand=True, fill="y")
        tk.Button(
            frame, text="Reset / Home",
            font=FONT_SMALL, bg="#6c3483", fg=FG_WHITE,
            activebackground="#884ea0", bd=0, pady=6,
            cursor="hand2",
            command=self._reset,
        ).pack(fill="x", padx=6, pady=(0, 10))

    # ── Right panel ───────────────────────────────────────────
    def _build_right_panel(self, parent):
        frame = tk.Frame(parent, bg=BG_DARK)
        frame.pack(side="left", fill="both", expand=True)

        # Selected problem label
        self.problem_var = tk.StringVar(value="No problem selected")
        tk.Label(
            frame, textvariable=self.problem_var,
            font=FONT_HEAD, bg=BG_DARK, fg=FG_ACCENT, anchor="w",
        ).pack(fill="x", pady=(0, 6))

        ttk.Separator(frame, orient="horizontal").pack(fill="x", pady=4)

        # ── Question section ──────────────────────────────────
        q_card = tk.Frame(frame, bg=BG_CARD, pady=12, padx=12)
        q_card.pack(fill="x", pady=(4, 8))

        tk.Label(
            q_card, text="Diagnostic Question",
            font=FONT_HEAD, bg=BG_CARD, fg=FG_ACCENT,
        ).pack(anchor="w")

        self.question_var = tk.StringVar(value="Please select a problem category from the left panel.")
        tk.Label(
            q_card, textvariable=self.question_var,
            font=FONT_BODY, bg=BG_CARD, fg=FG_WHITE,
            wraplength=580, justify="left", pady=6,
        ).pack(anchor="w")

        # Yes / No answer buttons
        btn_row = tk.Frame(q_card, bg=BG_CARD)
        btn_row.pack(anchor="w", pady=(4, 0))

        self.yes_btn = tk.Button(
            btn_row, text="Yes",
            font=FONT_HEAD, bg=BG_YES, fg=FG_WHITE,
            activebackground="#2ecc71", bd=0,
            padx=24, pady=6, cursor="hand2",
            command=lambda: self._answer("yes"),
        )
        self.yes_btn.pack(side="left", padx=(0, 8))

        self.no_btn = tk.Button(
            btn_row, text="No",
            font=FONT_HEAD, bg=BG_NO, fg=FG_WHITE,
            activebackground="#e74c3c", bd=0,
            padx=24, pady=6, cursor="hand2",
            command=lambda: self._answer("no"),
        )
        self.no_btn.pack(side="left")

        # Progress indicator
        self.progress_var = tk.StringVar(value="")
        tk.Label(
            q_card, textvariable=self.progress_var,
            font=FONT_SMALL, bg=BG_CARD, fg=FG_MUTED,
        ).pack(anchor="w", pady=(6, 0))

        # ── Solution section ──────────────────────────────────
        sol_card = tk.Frame(frame, bg=BG_CARD, pady=10, padx=12)
        sol_card.pack(fill="both", expand=True)

        sol_header = tk.Frame(sol_card, bg=BG_CARD)
        sol_header.pack(fill="x")

        tk.Label(
            sol_header, text="Recommended Solution",
            font=FONT_HEAD, bg=BG_CARD, fg=FG_ACCENT,
        ).pack(side="left")

        tk.Button(
            sol_header, text="Copy",
            font=FONT_SMALL, bg=BG_BTN, fg=FG_WHITE,
            activebackground=BG_BTN_HO, bd=0,
            padx=10, pady=2, cursor="hand2",
            command=self._copy_solution,
        ).pack(side="right")

        # Scrollable text box
        txt_frame = tk.Frame(sol_card, bg=BG_CARD)
        txt_frame.pack(fill="both", expand=True, pady=(6, 0))

        scrollbar = ttk.Scrollbar(txt_frame)
        scrollbar.pack(side="right", fill="y")

        self.solution_txt = tk.Text(
            txt_frame,
            font=FONT_MONO, bg="#1a2636", fg=FG_SOL,
            bd=0, padx=10, pady=8,
            wrap="word", state="disabled",
            yscrollcommand=scrollbar.set,
        )
        self.solution_txt.pack(fill="both", expand=True)
        scrollbar.config(command=self.solution_txt.yview)

        # Start fresh message
        self._show_solution("Waiting for your input...\n\nSelect a category on the left,\nthen answer the Yes/No questions.\nThe expert system will diagnose your problem\nand provide a step-by-step solution.")

        # Initially disable answer buttons
        self._set_answer_buttons(False)

    # ==========================================================
    # SESSION LOGIC
    # ==========================================================
    def _start_session(self, problem_key: str):
        """Initialise a new diagnostic session for the chosen problem."""
        # Highlight the selected button
        for k, btn in self.cat_buttons.items():
            btn.configure(bg=BG_BTN if k == problem_key else BG_DARK)

        label = PROBLEM_CATEGORIES[problem_key]
        self.problem_var.set(f"Problem: {label}")
        self.engine = InferenceEngine(problem_key)
        self.progress_var.set("")
        self._show_solution("Answering the diagnostic questions...")
        self._next_question()

    # ----------------------------------------------------------
    def _next_question(self):
        """Show the next question or trigger inference if done."""
        q = self.engine.get_next_question()
        if q is None:
            # All questions answered – run the inference engine
            self._run_inference()
            return

        key, text = q
        total = len(self.engine.questions)
        done  = self.engine.current_q_index + 1
        self.question_var.set(text)
        self.progress_var.set(f"Question {done} of {total}")
        self.status_var.set(f"Please answer: {text[:60]}...")
        self._set_answer_buttons(True)

    # ----------------------------------------------------------
    def _answer(self, ans: str):
        """Record the user answer and advance."""
        q = self.engine.get_next_question()
        if q is None:
            return
        key, _ = q
        self.engine.record_answer(key, ans)
        self._next_question()

    # ----------------------------------------------------------
    def _run_inference(self):
        """Ask the inference engine for a solution and display it."""
        solution = self.engine.infer()
        self._set_answer_buttons(False)
        self.question_var.set("Diagnosis complete. See solution below.")
        self.progress_var.set("All questions answered.")
        self._show_solution(solution)
        self.status_var.set("Solution generated. Click Reset to start a new session.")

    # ==========================================================
    # HELPERS
    # ==========================================================
    def _show_solution(self, text: str):
        """Write text into the read-only solution box."""
        self.solution_txt.configure(state="normal")
        self.solution_txt.delete("1.0", "end")
        self.solution_txt.insert("1.0", text)
        self.solution_txt.configure(state="disabled")

    # ----------------------------------------------------------
    def _set_answer_buttons(self, enabled: bool):
        state = "normal" if enabled else "disabled"
        self.yes_btn.configure(state=state)
        self.no_btn.configure(state=state)

    # ----------------------------------------------------------
    def _copy_solution(self):
        """Copy current solution text to the system clipboard."""
        text = self.solution_txt.get("1.0", "end").strip()
        if text and text != "Waiting for your input...\nSelect a category...".strip():
            self.clipboard_clear()
            self.clipboard_append(text)
            messagebox.showinfo("Copied", "Solution copied to clipboard!", parent=self)
        else:
            messagebox.showwarning("Nothing to copy", "No solution available yet.", parent=self)

    # ----------------------------------------------------------
    def _reset(self):
        """Reset the entire session back to the welcome state."""
        self.engine = None
        self.problem_var.set("No problem selected")
        self.question_var.set("Please select a problem category from the left panel.")
        self.progress_var.set("")
        self.status_var.set("Select a problem category to begin.")
        self._show_solution("Waiting for your input...\n\nSelect a category on the left,\nthen answer the Yes/No questions.\nThe expert system will diagnose your problem\nand provide a step-by-step solution.")
        self._set_answer_buttons(False)
        for btn in self.cat_buttons.values():
            btn.configure(bg=BG_DARK)

    # ----------------------------------------------------------
    def _bind_hover(self, btn):
        """Add simple hover effect to category buttons."""
        btn.bind("<Enter>", lambda e: btn.configure(bg=BG_BTN))
        btn.bind("<Leave>", lambda e: btn.configure(bg=BG_DARK if btn.cget("bg") != BG_BTN else BG_BTN))
