import platform

def notify(message):
    """Cross-platform notification (prints, can be extended for desktop/email/webhook)."""
    print(f"NOTIFY: {message}")
    # Extend here for desktop, email, webhook, etc.
