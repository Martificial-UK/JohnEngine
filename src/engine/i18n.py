# i18n.py

class I18N:
    def __init__(self, translations=None):
        self.translations = translations or {}
    def translate(self, key, lang="en"):
        return self.translations.get(lang, {}).get(key, key)
