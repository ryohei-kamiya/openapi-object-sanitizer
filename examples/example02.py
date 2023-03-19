import os
from openapi_object_sanitizer.sanitizer import Sanitizer

dirpath = os.path.dirname(os.path.abspath(__file__))
spec_file_path = os.path.join(dirpath, "openapi.yaml")

spec = Sanitizer.read_spec_file(spec_file_path)
print(spec["components"]["schemas"]["Example02"])
dummy = {}
result = Sanitizer.sanitize(dummy, "Example02", spec)

print(result)
