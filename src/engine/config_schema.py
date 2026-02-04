import jsonschema

def validate_config_schema(config, schema):
    """Validate config dict against a JSON schema."""
    jsonschema.validate(instance=config, schema=schema)
