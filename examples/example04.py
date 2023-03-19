import os
from openapi_object_sanitizer.sanitizer import Sanitizer

dirpath = os.path.dirname(os.path.abspath(__file__))
spec_file_path = os.path.join(dirpath, "openapi.yaml")

spec = Sanitizer.read_spec_file(spec_file_path)
print(spec["components"]["schemas"]["Example04"])
dummy = {"string_pattern": "xxxxxxxxxx", "string_pattern_with_default": "xxxxxxxxxx"}
result = Sanitizer.sanitize(dummy, "Example04", spec)

print(result)
