# OpenAPI Object Sanitizer

## About
OpenAPI Object Sanitizer is used to sanitize an object to match the schema definition of the OpenAPI specification.

## Usage
1. Define an OpenAPI Specification (v3.0) containing the object's schema in components/schemas.
2. Load the OpenAPI Specification in your python script and use it to sanitize your object.
```.py
from openapi_object_sanitizer.sanitizer import Sanitizer

spec = Sanitizer.read_spec_file('openapi.yaml')
object = get_object()  # Get the object from somewhere (e.g. from an API request parameter).
schema_name = 'Object'  # Specify the name of one of the schemas defined under components/schemas in OpenAPI Specification (v3.0).
status, sanitized_object, errmsg = Sanitizer.sanitize(object, schema_name, spec)  # Run sanitize

# The return value status stores the success (True) or failure (False) of sanitize,
# sanitized_object stores the object after sanitization,
# and errmsg stores the error message if status is False.
```

## Examples

### Example01

Fixed basic type mismatch.

```.py
>>> from openapi_object_sanitizer.sanitizer import Sanitizer
>>> spec = Sanitizer.read_spec_file("examples/openapi.yaml")
>>> print(spec["components"]["schemas"]["Example01"])
{'type': 'object', 'properties': {'integer': {'type': 'integer', 'minimum': 0, 'maximum': 100}, 'number': {'type': 'number', 'minimum': 0, 'maximum': 100}, 'string': {'type': 'string'}}}
>>> dummy = {"integer": "12", "number": "34", "string": 56}
>>> Sanitizer.sanitize(dummy, "Example01", spec)
(True, {'integer': 12, 'number': 34.0, 'string': '56'}, None)
```

### Example02

Complete missing values with default values.

```.py
>>> from openapi_object_sanitizer.sanitizer import Sanitizer
>>> spec = Sanitizer.read_spec_file("examples/openapi.yaml")
>>> print(spec["components"]["schemas"]["Example02"])
{'type': 'object', 'properties': {'integer_with_default': {'type': 'integer', 'minimum': 0, 'maximum': 100, 'default': 0}, 'number_with_default': {'type': 'number', 'minimum': 0, 'maximum': 100, 'default': 0}, 'string_with_default': {'type': 'string', 'default': 'abc'}}}
>>> dummy = {}
>>> Sanitizer.sanitize(dummy, "Example02", spec)
(True, {'integer_with_default': 0, 'number_with_default': 0, 'string_with_default': 'abc'}, None)
```

### Example03

Convert date to ISO 8601 formatted string.
And datetime to ISO 8601 formatted string or timestamp (UNIX TIME).

```.py
>>> import datetime
>>> from openapi_object_sanitizer.sanitizer import Sanitizer
>>> spec = Sanitizer.read_spec_file("examples/openapi.yaml")
>>> print(spec["components"]["schemas"]["Example03"])
{'type': 'object', 'properties': {'date_string': {'type': 'string'}, 'datetime_string': {'type': 'string'}, 'datetime_number': {'type': 'number'}, 'datetime_integer': {'type': 'integer'}}}
>>> EXAMPLE_DATE = datetime.date(2023, 1, 1)
>>> EXAMPLE_DATETIME = datetime.datetime(2023, 1, 1, 0, 0, 0, 0)
>>> dummy = {"date_string": EXAMPLE_DATE, "datetime_string": EXAMPLE_DATETIME, "datetime_number": EXAMPLE_DATETIME, "datetime_integer": EXAMPLE_DATETIME}
>>> Sanitizer.sanitize(dummy, "Example03", spec)
(True, {'date_string': '2023-01-01', 'datetime_string': '2023-01-01T00:00:00', 'datetime_number': 1672498800.0, 'datetime_integer': 1672498800}, None)
```

### Example04

Replace strings that do not match the regular expression pattern with an empty string or default string.

```.py
>>> from openapi_object_sanitizer.sanitizer import Sanitizer
>>> spec = Sanitizer.read_spec_file("examples/openapi.yaml")
>>> print(spec["components"]["schemas"]["Example04"])
{'type': 'object', 'properties': {'string_pattern': {'type': 'string', 'pattern': '^[0-9]{4}$'}, 'string_pattern_with_default': {'type': 'string', 'pattern': '^[0-9]{4}$', 'default': '0000'}}}
>>> dummy = {"string_pattern": "xxxxxxxxxx", "string_pattern_with_default": "xxxxxxxxxx"}
>>> Sanitizer.sanitize(dummy, "Example04", spec)
(False, {'string_pattern': '', 'string_pattern_with_default': '0000'}, "'' does not match '^[0-9]{4}$'")
```
