from knowledge_base import KNOWLEDGE_BASE

NO_MATCH = (
    "No specific rule matched your answers.\n"
    "Please contact the IT Help Desk and describe your\n"
    "problem in detail for further assistance."
)


class InferenceEngine:
    """
    Forward-chaining inference engine.
    Rules are checked in order. The FIRST rule whose conditions
    ALL match the user answers wins (AND logic per rule).
    A rule with an empty conditions dict acts as the fallback.
    """

    def __init__(self, problem_key):
        self.problem_key = problem_key
        data = KNOWLEDGE_BASE.get(problem_key, {})
        self.questions = data.get("questions", [])   # list of (key, text)
        self.rules = data.get("rules", [])            # list of rule dicts
        self.answers = {}            # {question_key: "yes"/"no"}
        self.current_q_index = 0    # pointer into self.questions

    def get_next_question(self):
        """Return (key, text) of the next unanswered question, or None."""
        if self.current_q_index < len(self.questions):
            return self.questions[self.current_q_index]
        return None

    def record_answer(self, question_key, answer):
        """Store the user answer (normalised to lowercase) and advance."""
        self.answers[question_key] = answer.strip().lower()
        self.current_q_index += 1

    def infer(self):
        """
        Match collected answers against all rules.
        Returns the solution string of the first matching rule.
        """
        for rule in self.rules:
            conditions = rule.get("conditions", {})
            # Empty conditions dict == unconditional default rule
            if not conditions:
                return rule["solution"]
            # All conditions must be satisfied (AND logic)
            if all(self.answers.get(k) == v for k, v in conditions.items()):
                return rule["solution"]
        return NO_MATCH

    def reset(self):
        """Clear state for a fresh session."""
        self.answers.clear()
        self.current_q_index = 0
