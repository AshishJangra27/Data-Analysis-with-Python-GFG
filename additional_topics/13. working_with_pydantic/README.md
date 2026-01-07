# Working with Pydantic

This folder contains 15 step-by-step examples demonstrating Pydantic for data validation and model management. The examples start from the absolute basics and progress to advanced features including schema generation and configuration management.

## Contents & Quick Summary

1. `01_minimal_model.py` — Minimal Pydantic model showing model definition, instance creation, and field access.
2. `02_basic_field_types.py` — Demonstrates int, str, float, bool fields and automatic type conversion.
3. `03_default_and_required_fields.py` — Required vs default fields and how defaults work.
4. `04_type_conversion_and_parsing.py` — Pydantic's automatic parsing from strings and other types.
5. `05_optional_and_missing_fields.py` — Using `Optional` fields and defaulting to `None`.
6. `06_model_methods_and_repr.py` — Adding methods and custom __str__ representation to models.
7. `07_custom_field_validator.py` — Using `@validator` for field-level custom validation.
8. `08_nested_models_and_structures.py` — Models as fields, lists of models, and nested parsing.
9. `09_enum_fields.py` — Using Python `Enum` types to restrict field values.
10. `10_error_handling.py` — Capturing and printing `ValidationError` details.
11. `11_inheritance_and_composition.py` — Model inheritance and composing models.
12. `12_custom_types_and_constraints.py` — Constrained types (`constr`, `conint`) and `EmailStr` for validated email fields.
13. `13_settings_management.py` — Using `BaseSettings` for environment/configuration management.
14. `14_root_validator.py` — Cross-field validation using `@root_validator`.
15. `15_advanced_schema_and_v2.py` — JSON schema generation and notes on Pydantic V2 / OpenAPI.

## How to use these examples
- Run them individually using the project's virtual environment's Python executable:

```bash
/Users/ashishzangra/Desktop/gfg/.venv/bin/python working_with_pydantic/01_minimal_model.py
```

- Most scripts print a concise result showing what Pydantic did (type conversion, validation, error messages, schema JSON, etc.).

## Notes & Requirements
- Pydantic is required. Install it into your project virtual environment:

```bash
/Users/ashishzangra/Desktop/gfg/.venv/bin/python -m pip install pydantic
```

- Some examples use optional extras (for example, `EmailStr` requires `email-validator`). Install with extras when needed:

```bash
/Users/ashishzangra/Desktop/gfg/.venv/bin/python -m pip install "pydantic[email]"
```

- For Pydantic V2 migration notes and FastAPI integration, consult the Pydantic and FastAPI documentation.

## Learning path recommendation
1. Start with `01_minimal_model.py` and `02_basic_field_types.py` to understand model basics.
2. Progress to validators and nested models (`07_custom_field_validator.py`, `08_nested_models_and_structures.py`).
3. Explore configuration (`13_settings_management.py`) and schema generation (`15_advanced_schema_and_v2.py`).

## License
Educational resources — feel free to reuse and modify.
