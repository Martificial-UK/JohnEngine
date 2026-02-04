# security_review.py
# Checklist for regular code/dependency review

CHECKLIST = [
    "Check for unused dependencies",
    "Scan for known vulnerabilities",
    "Review input validation",
    "Audit logging coverage",
    "Review plugin/task isolation",
    "Check for unsafe config options",
    "Verify dependency versions",
    "Review access controls",
    "Test error boundaries",
    "Run resource limit checks"
]

def run_security_review():
    print("Security Review Checklist:")
    for item in CHECKLIST:
        print(f"- {item}")
