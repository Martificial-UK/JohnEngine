# feedback.py
class Feedback:
    def __init__(self):
        self.reports = []
    def submit(self, user, message):
        self.reports.append({"user": user, "message": message})
    def all_reports(self):
        return self.reports
