import os
from openapi_object_sanitizer.sanitizer import Sanitizer

dirpath = os.path.dirname(os.path.abspath(__file__))
spec_file_path = os.path.join(dirpath, "openapi.yaml")

spec = Sanitizer.read_spec_file(spec_file_path)
print(spec["components"]["schemas"]["Example01"])
dummy = {"integer": "12", "number": "34", "string": 56}
result = Sanitizer.sanitize(dummy, "Example01", spec)

print(result)
