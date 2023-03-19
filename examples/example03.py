import os
import datetime
from openapi_object_sanitizer.sanitizer import Sanitizer

dirpath = os.path.dirname(os.path.abspath(__file__))
spec_file_path = os.path.join(dirpath, "openapi.yaml")

EXAMPLE_DATE = datetime.date(2023, 1, 1)
EXAMPLE_DATETIME = datetime.datetime(2023, 1, 1, 0, 0, 0, 0)

spec = Sanitizer.read_spec_file(spec_file_path)
print(spec["components"]["schemas"]["Example03"])
dummy = {
    "date_string": EXAMPLE_DATE,
    "datetime_string": EXAMPLE_DATETIME,
    "datetime_number": EXAMPLE_DATETIME,
    "datetime_integer": EXAMPLE_DATETIME,
}
result = Sanitizer.sanitize(dummy, "Example03", spec)

print(result)
