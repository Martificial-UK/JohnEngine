from loguru import logger

logger.add("engine.log", rotation="1 MB")

# Usage: logger.info("message")
