# JohnEngine

A reusable Python engine core for launching config-driven automation products. Extracted and refactored from TurboSort for extensibility and future product integration.

## Features
- Plugin/extension system
- Event hooks/callbacks
- Error handling
- Config validation
- Task/job management
- Notifications
- Metrics/statistics
- Multi-language support
- Security utilities
- API/service layer
- Guardrails/hardening
- CI/CD integration

## Usage
See src/engine/ for modules and usage examples.

## Testing
Run `python -m unittest discover -s tests -p "*.py"` to test all features.

## Security
Run `python src/engine/security_review.py` for a security checklist.

## CI/CD
See .github/workflows/python-app.yml for automated testing and security review.

## License
MIT

# Quickstart Guide

1. Clone or copy the JohnEngine repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Run tests: `python -m unittest discover -s tests -p "*.py"`
4. Explore features in `src/engine/` and usage examples in README.md.
5. Start building your product by creating plugins or using engine modules.
6. For API/service, run: `python src/engine/api.py`
7. For security review: `python src/engine/security_review.py`
8. For monitoring, backup, and feedback, see respective modules in `src/engine/`.
