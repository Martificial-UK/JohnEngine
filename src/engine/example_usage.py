# Example: Using the engine core in a product
from engine.engine import load_config, setup_logging, normalize_path
import os

CONFIG_PATH = normalize_path("./turbosort.config.json")
LOG_PATH = normalize_path("./logs/example_product.log")

def main():
    # Load configuration
    config = load_config(CONFIG_PATH)
    # Set up logging
    setup_logging(LOG_PATH, log_level="INFO", name="ExampleProduct")
    # Example logic using config
    print("Loaded config:", config)
    # ... product logic here ...

if __name__ == "__main__":
    main()
