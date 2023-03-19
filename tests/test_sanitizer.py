import unittest
import os
import datetime
from openapi_object_sanitizer.sanitizer import Sanitizer


class StanitizerTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        dirpath = os.path.dirname(os.path.abspath(__file__))
        spec_file_path = os.path.join(dirpath, "openapi.yaml")
        cls.spec = Sanitizer.read_spec_file(spec_file_path)

    def test_001_validate(self):
        obj = {
            "RequiredInteger": 1,
            "RequiredNumber": 1.5,
            "RequiredString": "required string",
            "RequiredIntegerWithDefault": 1,
            "RequiredNumberWithDefault": 1.5,
            "RequiredStringWithDefault": "required string with default",
            "RequiredNullableInteger": None,
            "RequiredNullableNumber": None,
            "RequiredNullableString": None,
            "RequiredNullableIntegerWithDefault": None,
            "RequiredNullableNumberWithDefault": None,
            "RequiredNullableStringWithDefault": None,
            "DateString": datetime.date.today().isoformat(),
            "DatetimeString": datetime.datetime.now().isoformat(),
            "DatetimeNumber": datetime.datetime.now().timestamp(),
            "DatetimeInteger": int(datetime.datetime.now().timestamp()),
            "StringPattern": "0123",
            "StringPatternWithDefault": "4567",
        }
        status, result, errmsg = Sanitizer.validate(
            obj, "Dummy", self.spec, with_default=False, with_typesafe=False
        )
        self.assertEqual(status, True)
        self.assertIsNone(errmsg)
        self.assertNotIn("Integer", result.keys())
        self.assertNotIn("Number", result.keys())
        self.assertNotIn("String", result.keys())
        self.assertNotIn("NullableInteger", result.keys())
        self.assertNotIn("NullableNumber", result.keys())
        self.assertNotIn("NullableString", result.keys())
        self.assertNotIn("IntegerWithDefault", result.keys())
        self.assertNotIn("NumberWithDefault", result.keys())
        self.assertNotIn("StringWithDefault", result.keys())
        self.assertNotIn("NullableIntegerWithDefault", result.keys())
        self.assertNotIn("NullableNumberWithDefault", result.keys())
        self.assertNotIn("NullableStringWithDefault", result.keys())

        obj = {
            "RequiredInteger": "1",
            "RequiredNumber": 1.5,
            "RequiredString": "required string",
            "RequiredIntegerWithDefault": 1,
            "RequiredNumberWithDefault": 1.5,
            "RequiredStringWithDefault": "required string with default",
            "RequiredNullableIntegerWithDefault": None,
            "RequiredNullableNumberWithDefault": None,
            "RequiredNullableStringWithDefault": None,
            "DateString": datetime.date.today().isoformat(),
            "DatetimeString": datetime.datetime.now().isoformat(),
            "DatetimeNumber": datetime.datetime.now().timestamp(),
            "DatetimeInteger": int(datetime.datetime.now().timestamp()),
            "StringPattern": "0123",
            "StringPatternWithDefault": "4567",
        }
        status, result, errmsg = Sanitizer.validate(
            obj, "Dummy", self.spec, with_default=False, with_typesafe=False
        )
        self.assertEqual(status, False)
        self.assertIsNotNone(errmsg)
        self.assertNotIn("Integer", result.keys())
        self.assertNotIn("Number", result.keys())
        self.assertNotIn("String", result.keys())
        self.assertNotIn("NullableInteger", result.keys())
        self.assertNotIn("NullableNumber", result.keys())
        self.assertNotIn("NullableString", result.keys())
        self.assertNotIn("IntegerWithDefault", result.keys())
        self.assertNotIn("NumberWithDefault", result.keys())
        self.assertNotIn("StringWithDefault", result.keys())
        self.assertNotIn("NullableIntegerWithDefault", result.keys())
        self.assertNotIn("NullableNumberWithDefault", result.keys())
        self.assertNotIn("NullableStringWithDefault", result.keys())

        obj = {
            "RequiredInteger": 1,
            "RequiredNumber": "1.5",
            "RequiredString": "required string",
            "RequiredIntegerWithDefault": 1,
            "RequiredNumberWithDefault": 1.5,
            "RequiredStringWithDefault": "required string with default",
            "RequiredNullableInteger": None,
            "RequiredNullableNumber": None,
            "RequiredNullableString": None,
            "RequiredNullableIntegerWithDefault": None,
            "RequiredNullableNumberWithDefault": None,
            "RequiredNullableStringWithDefault": None,
            "DateString": datetime.date.today().isoformat(),
            "DatetimeString": datetime.datetime.now().isoformat(),
            "DatetimeNumber": datetime.datetime.now().timestamp(),
            "DatetimeInteger": int(datetime.datetime.now().timestamp()),
            "StringPattern": "0123",
            "StringPatternWithDefault": "4567",
        }
        status, result, errmsg = Sanitizer.validate(
            obj, "Dummy", self.spec, with_default=False, with_typesafe=False
        )
        self.assertEqual(status, False)
        self.assertIsNotNone(errmsg)
        self.assertNotIn("Integer", result.keys())
        self.assertNotIn("Number", result.keys())
        self.assertNotIn("String", result.keys())
        self.assertNotIn("NullableInteger", result.keys())
        self.assertNotIn("NullableNumber", result.keys())
        self.assertNotIn("NullableString", result.keys())
        self.assertNotIn("IntegerWithDefault", result.keys())
        self.assertNotIn("NumberWithDefault", result.keys())
        self.assertNotIn("StringWithDefault", result.keys())
        self.assertNotIn("NullableIntegerWithDefault", result.keys())
        self.assertNotIn("NullableNumberWithDefault", result.keys())
        self.assertNotIn("NullableStringWithDefault", result.keys())

        obj = {
            "RequiredInteger": 1,
            "RequiredNumber": 1.5,
            "RequiredString": 12345,
            "RequiredIntegerWithDefault": 1,
            "RequiredNumberWithDefault": 1.5,
            "RequiredStringWithDefault": "required string with default",
            "RequiredNullableInteger": None,
            "RequiredNullableNumber": None,
            "RequiredNullableString": None,
            "RequiredNullableIntegerWithDefault": None,
            "RequiredNullableNumberWithDefault": None,
            "RequiredNullableStringWithDefault": None,
            "DateString": datetime.date.today().isoformat(),
            "DatetimeString": datetime.datetime.now().isoformat(),
            "DatetimeNumber": datetime.datetime.now().timestamp(),
            "DatetimeInteger": int(datetime.datetime.now().timestamp()),
            "StringPattern": "0123",
            "StringPatternWithDefault": "4567",
        }
        status, result, errmsg = Sanitizer.validate(
            obj, "Dummy", self.spec, with_default=False, with_typesafe=False
        )
        self.assertEqual(status, False)
        self.assertIsNotNone(errmsg)
        self.assertNotIn("Integer", result.keys())
        self.assertNotIn("Number", result.keys())
        self.assertNotIn("String", result.keys())
        self.assertNotIn("NullableInteger", result.keys())
        self.assertNotIn("NullableNumber", result.keys())
        self.assertNotIn("NullableString", result.keys())
        self.assertNotIn("IntegerWithDefault", result.keys())
        self.assertNotIn("NumberWithDefault", result.keys())
        self.assertNotIn("StringWithDefault", result.keys())
        self.assertNotIn("NullableIntegerWithDefault", result.keys())
        self.assertNotIn("NullableNumberWithDefault", result.keys())
        self.assertNotIn("NullableStringWithDefault", result.keys())

        obj = {
            "RequiredInteger": 1,
            "RequiredNumber": 1.5,
            "RequiredString": "required string",
            "RequiredIntegerWithDefault": 1.5,
            "RequiredNumberWithDefault": 1.5,
            "RequiredStringWithDefault": "required string with default",
            "RequiredNullableInteger": None,
            "RequiredNullableNumber": None,
            "RequiredNullableString": None,
            "RequiredNullableIntegerWithDefault": None,
            "RequiredNullableNumberWithDefault": None,
            "RequiredNullableStringWithDefault": None,
            "DateString": datetime.date.today().isoformat(),
            "DatetimeString": datetime.datetime.now().isoformat(),
            "DatetimeNumber": datetime.datetime.now().timestamp(),
            "DatetimeInteger": int(datetime.datetime.now().timestamp()),
            "StringPattern": "0123",
            "StringPatternWithDefault": "4567",
        }
        status, result, errmsg = Sanitizer.validate(
            obj, "Dummy", self.spec, with_default=False, with_typesafe=False
        )
        self.assertEqual(status, False)
        self.assertIsNotNone(errmsg)
        self.assertNotIn("Integer", result.keys())
        self.assertNotIn("Number", result.keys())
        self.assertNotIn("String", result.keys())
        self.assertNotIn("NullableInteger", result.keys())
        self.assertNotIn("NullableNumber", result.keys())
        self.assertNotIn("NullableString", result.keys())
        self.assertNotIn("IntegerWithDefault", result.keys())
        self.assertNotIn("NumberWithDefault", result.keys())
        self.assertNotIn("StringWithDefault", result.keys())
        self.assertNotIn("NullableIntegerWithDefault", result.keys())
        self.assertNotIn("NullableNumberWithDefault", result.keys())
        self.assertNotIn("NullableStringWithDefault", result.keys())

        obj = {
            "RequiredInteger": 1,
            "RequiredNumber": 1.5,
            "RequiredString": "required string",
            "RequiredIntegerWithDefault": 1,
            "RequiredNumberWithDefault": "1.5",
            "RequiredStringWithDefault": "required string with default",
            "RequiredNullableInteger": None,
            "RequiredNullableNumber": None,
            "RequiredNullableString": None,
            "RequiredNullableIntegerWithDefault": None,
            "RequiredNullableNumberWithDefault": None,
            "RequiredNullableStringWithDefault": None,
            "DateString": datetime.date.today().isoformat(),
            "DatetimeString": datetime.datetime.now().isoformat(),
            "DatetimeNumber": datetime.datetime.now().timestamp(),
            "DatetimeInteger": int(datetime.datetime.now().timestamp()),
            "StringPattern": "0123",
            "StringPatternWithDefault": "4567",
        }
        status, result, errmsg = Sanitizer.validate(
            obj, "Dummy", self.spec, with_default=False, with_typesafe=False
        )
        self.assertEqual(status, False)
        self.assertIsNotNone(errmsg)
        self.assertNotIn("Integer", result.keys())
        self.assertNotIn("Number", result.keys())
        self.assertNotIn("String", result.keys())
        self.assertNotIn("NullableInteger", result.keys())
        self.assertNotIn("NullableNumber", result.keys())
        self.assertNotIn("NullableString", result.keys())
        self.assertNotIn("IntegerWithDefault", result.keys())
        self.assertNotIn("NumberWithDefault", result.keys())
        self.assertNotIn("StringWithDefault", result.keys())
        self.assertNotIn("NullableIntegerWithDefault", result.keys())
        self.assertNotIn("NullableNumberWithDefault", result.keys())
        self.assertNotIn("NullableStringWithDefault", result.keys())

        obj = {
            "RequiredInteger": 1,
            "RequiredNumber": 1.5,
            "RequiredString": "required string",
            "RequiredIntegerWithDefault": 1,
            "RequiredNumberWithDefault": 1.5,
            "RequiredStringWithDefault": 12345,
            "RequiredNullableInteger": None,
            "RequiredNullableNumber": None,
            "RequiredNullableString": None,
            "RequiredNullableIntegerWithDefault": None,
            "RequiredNullableNumberWithDefault": None,
            "RequiredNullableStringWithDefault": None,
            "DateString": datetime.date.today().isoformat(),
            "DatetimeString": datetime.datetime.now().isoformat(),
            "DatetimeNumber": datetime.datetime.now().timestamp(),
            "DatetimeInteger": int(datetime.datetime.now().timestamp()),
            "StringPattern": "0123",
            "StringPatternWithDefault": "4567",
        }
        status, result, errmsg = Sanitizer.validate(
            obj, "Dummy", self.spec, with_default=False, with_typesafe=False
        )
        self.assertEqual(status, False)
        self.assertIsNotNone(errmsg)
        self.assertNotIn("Integer", result.keys())
        self.assertNotIn("Number", result.keys())
        self.assertNotIn("String", result.keys())
        self.assertNotIn("NullableInteger", result.keys())
        self.assertNotIn("NullableNumber", result.keys())
        self.assertNotIn("NullableString", result.keys())
        self.assertNotIn("IntegerWithDefault", result.keys())
        self.assertNotIn("NumberWithDefault", result.keys())
        self.assertNotIn("StringWithDefault", result.keys())
        self.assertNotIn("NullableIntegerWithDefault", result.keys())
        self.assertNotIn("NullableNumberWithDefault", result.keys())
        self.assertNotIn("NullableStringWithDefault", result.keys())

        obj = {
            "RequiredInteger": 1,
            "RequiredNumber": 1.5,
            "RequiredString": "required string",
            "RequiredIntegerWithDefault": 1,
            "RequiredNumberWithDefault": 1.5,
            "RequiredStringWithDefault": "required string with default",
            "RequiredNullableNumber": None,
            "RequiredNullableString": None,
            "RequiredNullableIntegerWithDefault": None,
            "RequiredNullableNumberWithDefault": None,
            "RequiredNullableStringWithDefault": None,
            "DateString": datetime.date.today().isoformat(),
            "DatetimeString": datetime.datetime.now().isoformat(),
            "DatetimeNumber": datetime.datetime.now().timestamp(),
            "DatetimeInteger": int(datetime.datetime.now().timestamp()),
            "StringPattern": "0123",
            "StringPatternWithDefault": "4567",
        }
        status, result, errmsg = Sanitizer.validate(
            obj, "Dummy", self.spec, with_default=False, with_typesafe=False
        )
        self.assertEqual(status, False)
        self.assertIsNotNone(errmsg)
        self.assertNotIn("Integer", result.keys())
        self.assertNotIn("Number", result.keys())
        self.assertNotIn("String", result.keys())
        self.assertNotIn("NullableInteger", result.keys())
        self.assertNotIn("NullableNumber", result.keys())
        self.assertNotIn("NullableString", result.keys())
        self.assertNotIn("IntegerWithDefault", result.keys())
        self.assertNotIn("NumberWithDefault", result.keys())
        self.assertNotIn("StringWithDefault", result.keys())
        self.assertNotIn("NullableIntegerWithDefault", result.keys())
        self.assertNotIn("NullableNumberWithDefault", result.keys())
        self.assertNotIn("NullableStringWithDefault", result.keys())

        obj = {
            "RequiredInteger": 1,
            "RequiredNumber": 1.5,
            "RequiredString": "required string",
            "RequiredIntegerWithDefault": 1,
            "RequiredNumberWithDefault": 1.5,
            "RequiredStringWithDefault": "required string with default",
            "RequiredNullableInteger": None,
            "RequiredNullableString": None,
            "RequiredNullableIntegerWithDefault": None,
            "RequiredNullableNumberWithDefault": None,
            "RequiredNullableStringWithDefault": None,
            "DateString": datetime.date.today().isoformat(),
            "DatetimeString": datetime.datetime.now().isoformat(),
            "DatetimeNumber": datetime.datetime.now().timestamp(),
            "DatetimeInteger": int(datetime.datetime.now().timestamp()),
            "StringPattern": "0123",
            "StringPatternWithDefault": "4567",
        }
        status, result, errmsg = Sanitizer.validate(
            obj, "Dummy", self.spec, with_default=False, with_typesafe=False
        )
        self.assertEqual(status, False)
        self.assertIsNotNone(errmsg)
        self.assertNotIn("Integer", result.keys())
        self.assertNotIn("Number", result.keys())
        self.assertNotIn("String", result.keys())
        self.assertNotIn("NullableInteger", result.keys())
        self.assertNotIn("NullableNumber", result.keys())
        self.assertNotIn("NullableString", result.keys())
        self.assertNotIn("IntegerWithDefault", result.keys())
        self.assertNotIn("NumberWithDefault", result.keys())
        self.assertNotIn("StringWithDefault", result.keys())
        self.assertNotIn("NullableIntegerWithDefault", result.keys())
        self.assertNotIn("NullableNumberWithDefault", result.keys())
        self.assertNotIn("NullableStringWithDefault", result.keys())

        obj = {
            "RequiredInteger": 1,
            "RequiredNumber": 1.5,
            "RequiredString": "required string",
            "RequiredIntegerWithDefault": 1,
            "RequiredNumberWithDefault": 1.5,
            "RequiredStringWithDefault": "required string with default",
            "RequiredNullableInteger": None,
            "RequiredNullableNumber": None,
            "RequiredNullableIntegerWithDefault": None,
            "RequiredNullableNumberWithDefault": None,
            "RequiredNullableStringWithDefault": None,
            "DateString": datetime.date.today().isoformat(),
            "DatetimeString": datetime.datetime.now().isoformat(),
            "DatetimeNumber": datetime.datetime.now().timestamp(),
            "DatetimeInteger": int(datetime.datetime.now().timestamp()),
            "StringPattern": "0123",
            "StringPatternWithDefault": "4567",
        }
        status, result, errmsg = Sanitizer.validate(
            obj, "Dummy", self.spec, with_default=False, with_typesafe=False
        )
        self.assertEqual(status, False)
        self.assertIsNotNone(errmsg)
        self.assertNotIn("Integer", result.keys())
        self.assertNotIn("Number", result.keys())
        self.assertNotIn("String", result.keys())
        self.assertNotIn("NullableInteger", result.keys())
        self.assertNotIn("NullableNumber", result.keys())
        self.assertNotIn("NullableString", result.keys())
        self.assertNotIn("IntegerWithDefault", result.keys())
        self.assertNotIn("NumberWithDefault", result.keys())
        self.assertNotIn("StringWithDefault", result.keys())
        self.assertNotIn("NullableIntegerWithDefault", result.keys())
        self.assertNotIn("NullableNumberWithDefault", result.keys())
        self.assertNotIn("NullableStringWithDefault", result.keys())

        obj = {
            "RequiredInteger": 1,
            "RequiredNumber": 1.5,
            "RequiredString": "required string",
            "RequiredIntegerWithDefault": 1,
            "RequiredNumberWithDefault": 1.5,
            "RequiredStringWithDefault": "required string with default",
            "RequiredNullableInteger": None,
            "RequiredNullableNumber": None,
            "RequiredNullableString": None,
            "RequiredNullableNumberWithDefault": None,
            "RequiredNullableStringWithDefault": None,
            "DateString": datetime.date.today().isoformat(),
            "DatetimeString": datetime.datetime.now().isoformat(),
            "DatetimeNumber": datetime.datetime.now().timestamp(),
            "DatetimeInteger": int(datetime.datetime.now().timestamp()),
            "StringPattern": "0123",
            "StringPatternWithDefault": "4567",
        }
        status, result, errmsg = Sanitizer.validate(
            obj, "Dummy", self.spec, with_default=False, with_typesafe=False
        )
        self.assertEqual(status, False)
        self.assertIsNotNone(errmsg)
        self.assertNotIn("Integer", result.keys())
        self.assertNotIn("Number", result.keys())
        self.assertNotIn("String", result.keys())
        self.assertNotIn("NullableInteger", result.keys())
        self.assertNotIn("NullableNumber", result.keys())
        self.assertNotIn("NullableString", result.keys())
        self.assertNotIn("IntegerWithDefault", result.keys())
        self.assertNotIn("NumberWithDefault", result.keys())
        self.assertNotIn("StringWithDefault", result.keys())
        self.assertNotIn("NullableIntegerWithDefault", result.keys())
        self.assertNotIn("NullableNumberWithDefault", result.keys())
        self.assertNotIn("NullableStringWithDefault", result.keys())

        obj = {
            "RequiredInteger": 1,
            "RequiredNumber": 1.5,
            "RequiredString": "required string",
            "RequiredIntegerWithDefault": 1,
            "RequiredNumberWithDefault": 1.5,
            "RequiredStringWithDefault": "required string with default",
            "RequiredNullableInteger": None,
            "RequiredNullableNumber": None,
            "RequiredNullableString": None,
            "RequiredNullableIntegerWithDefault": None,
            "RequiredNullableStringWithDefault": None,
            "DateString": datetime.date.today().isoformat(),
            "DatetimeString": datetime.datetime.now().isoformat(),
            "DatetimeNumber": datetime.datetime.now().timestamp(),
            "DatetimeInteger": int(datetime.datetime.now().timestamp()),
            "StringPattern": "0123",
            "StringPatternWithDefault": "4567",
        }
        status, result, errmsg = Sanitizer.validate(
            obj, "Dummy", self.spec, with_default=False, with_typesafe=False
        )
        self.assertEqual(status, False)
        self.assertIsNotNone(errmsg)
        self.assertNotIn("Integer", result.keys())
        self.assertNotIn("Number", result.keys())
        self.assertNotIn("String", result.keys())
        self.assertNotIn("NullableInteger", result.keys())
        self.assertNotIn("NullableNumber", result.keys())
        self.assertNotIn("NullableString", result.keys())
        self.assertNotIn("IntegerWithDefault", result.keys())
        self.assertNotIn("NumberWithDefault", result.keys())
        self.assertNotIn("StringWithDefault", result.keys())
        self.assertNotIn("NullableIntegerWithDefault", result.keys())
        self.assertNotIn("NullableNumberWithDefault", result.keys())
        self.assertNotIn("NullableStringWithDefault", result.keys())

        obj = {
            "RequiredInteger": 1,
            "RequiredNumber": 1.5,
            "RequiredString": "required string",
            "RequiredIntegerWithDefault": 1,
            "RequiredNumberWithDefault": 1.5,
            "RequiredStringWithDefault": "required string with default",
            "RequiredNullableInteger": None,
            "RequiredNullableNumber": None,
            "RequiredNullableString": None,
            "RequiredNullableIntegerWithDefault": None,
            "RequiredNullableNumberWithDefault": None,
            "DateString": datetime.date.today().isoformat(),
            "DatetimeString": datetime.datetime.now().isoformat(),
            "DatetimeNumber": datetime.datetime.now().timestamp(),
            "DatetimeInteger": int(datetime.datetime.now().timestamp()),
            "StringPattern": "0123",
            "StringPatternWithDefault": "4567",
        }
        status, result, errmsg = Sanitizer.validate(
            obj, "Dummy", self.spec, with_default=False, with_typesafe=False
        )
        self.assertEqual(status, False)
        self.assertIsNotNone(errmsg)
        self.assertNotIn("Integer", result.keys())
        self.assertNotIn("Number", result.keys())
        self.assertNotIn("String", result.keys())
        self.assertNotIn("NullableInteger", result.keys())
        self.assertNotIn("NullableNumber", result.keys())
        self.assertNotIn("NullableString", result.keys())
        self.assertNotIn("IntegerWithDefault", result.keys())
        self.assertNotIn("NumberWithDefault", result.keys())
        self.assertNotIn("StringWithDefault", result.keys())
        self.assertNotIn("NullableIntegerWithDefault", result.keys())
        self.assertNotIn("NullableNumberWithDefault", result.keys())
        self.assertNotIn("NullableStringWithDefault", result.keys())

        obj = {
            "RequiredInteger": 1,
            "RequiredNumber": 1.5,
            "RequiredString": "required string",
            "RequiredIntegerWithDefault": 1,
            "RequiredNumberWithDefault": 1.5,
            "RequiredStringWithDefault": "required string with default",
            "RequiredNullableInteger": None,
            "RequiredNullableNumber": None,
            "RequiredNullableString": None,
            "RequiredNullableIntegerWithDefault": None,
            "RequiredNullableNumberWithDefault": None,
            "RequiredNullableStringWithDefault": None,
            "DateString": datetime.date.today(),
            "DatetimeString": datetime.datetime.now().isoformat(),
            "DatetimeNumber": datetime.datetime.now().timestamp(),
            "DatetimeInteger": int(datetime.datetime.now().timestamp()),
            "StringPattern": "0123",
            "StringPatternWithDefault": "4567",
        }
        status, result, errmsg = Sanitizer.validate(
            obj, "Dummy", self.spec, with_default=False, with_typesafe=False
        )
        self.assertEqual(status, False)
        self.assertIsNotNone(errmsg)
        self.assertNotIn("Integer", result.keys())
        self.assertNotIn("Number", result.keys())
        self.assertNotIn("String", result.keys())
        self.assertNotIn("NullableInteger", result.keys())
        self.assertNotIn("NullableNumber", result.keys())
        self.assertNotIn("NullableString", result.keys())
        self.assertNotIn("IntegerWithDefault", result.keys())
        self.assertNotIn("NumberWithDefault", result.keys())
        self.assertNotIn("StringWithDefault", result.keys())
        self.assertNotIn("NullableIntegerWithDefault", result.keys())
        self.assertNotIn("NullableNumberWithDefault", result.keys())
        self.assertNotIn("NullableStringWithDefault", result.keys())

        obj = {
            "RequiredInteger": 1,
            "RequiredNumber": 1.5,
            "RequiredString": "required string",
            "RequiredIntegerWithDefault": 1,
            "RequiredNumberWithDefault": 1.5,
            "RequiredStringWithDefault": "required string with default",
            "RequiredNullableInteger": None,
            "RequiredNullableNumber": None,
            "RequiredNullableString": None,
            "RequiredNullableIntegerWithDefault": None,
            "RequiredNullableNumberWithDefault": None,
            "RequiredNullableStringWithDefault": None,
            "DateString": datetime.date.today().isoformat(),
            "DatetimeString": datetime.datetime.now(),
            "DatetimeNumber": datetime.datetime.now().timestamp(),
            "DatetimeInteger": int(datetime.datetime.now().timestamp()),
            "StringPattern": "0123",
            "StringPatternWithDefault": "4567",
        }
        status, result, errmsg = Sanitizer.validate(
            obj, "Dummy", self.spec, with_default=False, with_typesafe=False
        )
        self.assertEqual(status, False)
        self.assertIsNotNone(errmsg)
        self.assertNotIn("Integer", result.keys())
        self.assertNotIn("Number", result.keys())
        self.assertNotIn("String", result.keys())
        self.assertNotIn("NullableInteger", result.keys())
        self.assertNotIn("NullableNumber", result.keys())
        self.assertNotIn("NullableString", result.keys())
        self.assertNotIn("IntegerWithDefault", result.keys())
        self.assertNotIn("NumberWithDefault", result.keys())
        self.assertNotIn("StringWithDefault", result.keys())
        self.assertNotIn("NullableIntegerWithDefault", result.keys())
        self.assertNotIn("NullableNumberWithDefault", result.keys())
        self.assertNotIn("NullableStringWithDefault", result.keys())

        obj = {
            "RequiredInteger": 1,
            "RequiredNumber": 1.5,
            "RequiredString": "required string",
            "RequiredIntegerWithDefault": 1,
            "RequiredNumberWithDefault": 1.5,
            "RequiredStringWithDefault": "required string with default",
            "RequiredNullableInteger": None,
            "RequiredNullableNumber": None,
            "RequiredNullableString": None,
            "RequiredNullableIntegerWithDefault": None,
            "RequiredNullableNumberWithDefault": None,
            "RequiredNullableStringWithDefault": None,
            "DateString": datetime.date.today().isoformat(),
            "DatetimeString": datetime.datetime.now().isoformat(),
            "DatetimeNumber": datetime.datetime.now(),
            "DatetimeInteger": int(datetime.datetime.now().timestamp()),
            "StringPattern": "0123",
            "StringPatternWithDefault": "4567",
        }
        status, result, errmsg = Sanitizer.validate(
            obj, "Dummy", self.spec, with_default=False, with_typesafe=False
        )
        self.assertEqual(status, False)
        self.assertIsNotNone(errmsg)
        self.assertNotIn("Integer", result.keys())
        self.assertNotIn("Number", result.keys())
        self.assertNotIn("String", result.keys())
        self.assertNotIn("NullableInteger", result.keys())
        self.assertNotIn("NullableNumber", result.keys())
        self.assertNotIn("NullableString", result.keys())
        self.assertNotIn("IntegerWithDefault", result.keys())
        self.assertNotIn("NumberWithDefault", result.keys())
        self.assertNotIn("StringWithDefault", result.keys())
        self.assertNotIn("NullableIntegerWithDefault", result.keys())
        self.assertNotIn("NullableNumberWithDefault", result.keys())
        self.assertNotIn("NullableStringWithDefault", result.keys())

        obj = {
            "RequiredInteger": 1,
            "RequiredNumber": 1.5,
            "RequiredString": "required string",
            "RequiredIntegerWithDefault": 1,
            "RequiredNumberWithDefault": 1.5,
            "RequiredStringWithDefault": "required string with default",
            "RequiredNullableInteger": None,
            "RequiredNullableNumber": None,
            "RequiredNullableString": None,
            "RequiredNullableIntegerWithDefault": None,
            "RequiredNullableNumberWithDefault": None,
            "RequiredNullableStringWithDefault": None,
            "DateString": datetime.date.today().isoformat(),
            "DatetimeString": datetime.datetime.now().isoformat(),
            "DatetimeNumber": datetime.datetime.now().timestamp(),
            "DatetimeInteger": datetime.datetime.now(),
            "StringPattern": "0123",
            "StringPatternWithDefault": "4567",
        }
        status, result, errmsg = Sanitizer.validate(
            obj, "Dummy", self.spec, with_default=False, with_typesafe=False
        )
        self.assertEqual(status, False)
        self.assertIsNotNone(errmsg)
        self.assertNotIn("Integer", result.keys())
        self.assertNotIn("Number", result.keys())
        self.assertNotIn("String", result.keys())
        self.assertNotIn("NullableInteger", result.keys())
        self.assertNotIn("NullableNumber", result.keys())
        self.assertNotIn("NullableString", result.keys())
        self.assertNotIn("IntegerWithDefault", result.keys())
        self.assertNotIn("NumberWithDefault", result.keys())
        self.assertNotIn("StringWithDefault", result.keys())
        self.assertNotIn("NullableIntegerWithDefault", result.keys())
        self.assertNotIn("NullableNumberWithDefault", result.keys())
        self.assertNotIn("NullableStringWithDefault", result.keys())

        obj = {
            "RequiredInteger": 1,
            "RequiredNumber": 1.5,
            "RequiredString": "required string",
            "RequiredIntegerWithDefault": 1,
            "RequiredNumberWithDefault": 1.5,
            "RequiredStringWithDefault": "required string with default",
            "RequiredNullableInteger": None,
            "RequiredNullableNumber": None,
            "RequiredNullableString": None,
            "RequiredNullableIntegerWithDefault": None,
            "RequiredNullableNumberWithDefault": None,
            "RequiredNullableStringWithDefault": None,
            "DateString": datetime.date.today().isoformat(),
            "DatetimeString": datetime.datetime.now().isoformat(),
            "DatetimeNumber": datetime.datetime.now().timestamp(),
            "DatetimeInteger": datetime.datetime.now().timestamp(),
            "StringPattern": "01234",
            "StringPatternWithDefault": "4567",
        }
        status, result, errmsg = Sanitizer.validate(
            obj, "Dummy", self.spec, with_default=False, with_typesafe=False
        )
        self.assertEqual(status, False)
        self.assertIsNotNone(errmsg)
        self.assertNotIn("Integer", result.keys())
        self.assertNotIn("Number", result.keys())
        self.assertNotIn("String", result.keys())
        self.assertNotIn("NullableInteger", result.keys())
        self.assertNotIn("NullableNumber", result.keys())
        self.assertNotIn("NullableString", result.keys())
        self.assertNotIn("IntegerWithDefault", result.keys())
        self.assertNotIn("NumberWithDefault", result.keys())
        self.assertNotIn("StringWithDefault", result.keys())
        self.assertNotIn("NullableIntegerWithDefault", result.keys())
        self.assertNotIn("NullableNumberWithDefault", result.keys())
        self.assertNotIn("NullableStringWithDefault", result.keys())

        obj = {
            "RequiredInteger": 1,
            "RequiredNumber": 1.5,
            "RequiredString": "required string",
            "RequiredIntegerWithDefault": 1,
            "RequiredNumberWithDefault": 1.5,
            "RequiredStringWithDefault": "required string with default",
            "RequiredNullableInteger": None,
            "RequiredNullableNumber": None,
            "RequiredNullableString": None,
            "RequiredNullableIntegerWithDefault": None,
            "RequiredNullableNumberWithDefault": None,
            "RequiredNullableStringWithDefault": None,
            "DateString": datetime.date.today().isoformat(),
            "DatetimeString": datetime.datetime.now().isoformat(),
            "DatetimeNumber": datetime.datetime.now().timestamp(),
            "DatetimeInteger": datetime.datetime.now().timestamp(),
            "StringPattern": "0123",
            "StringPatternWithDefault": "45678",
        }
        status, result, errmsg = Sanitizer.validate(
            obj, "Dummy", self.spec, with_default=False, with_typesafe=False
        )
        self.assertEqual(status, False)
        self.assertIsNotNone(errmsg)
        self.assertNotIn("Integer", result.keys())
        self.assertNotIn("Number", result.keys())
        self.assertNotIn("String", result.keys())
        self.assertNotIn("NullableInteger", result.keys())
        self.assertNotIn("NullableNumber", result.keys())
        self.assertNotIn("NullableString", result.keys())
        self.assertNotIn("IntegerWithDefault", result.keys())
        self.assertNotIn("NumberWithDefault", result.keys())
        self.assertNotIn("StringWithDefault", result.keys())
        self.assertNotIn("NullableIntegerWithDefault", result.keys())
        self.assertNotIn("NullableNumberWithDefault", result.keys())
        self.assertNotIn("NullableStringWithDefault", result.keys())

    def test_002_validate_with_default(self):
        obj = {
            "RequiredInteger": 1,
            "RequiredNumber": 1.5,
            "RequiredString": "required string",
            "RequiredIntegerWithDefault": 1,
            "RequiredNumberWithDefault": 1.5,
            "RequiredStringWithDefault": "required string with default",
            "RequiredNullableInteger": None,
            "RequiredNullableNumber": None,
            "RequiredNullableString": None,
            "RequiredNullableIntegerWithDefault": None,
            "RequiredNullableNumberWithDefault": None,
            "RequiredNullableStringWithDefault": None,
            "DateString": datetime.date.today().isoformat(),
            "DatetimeString": datetime.datetime.now().isoformat(),
            "DatetimeNumber": datetime.datetime.now().timestamp(),
            "DatetimeInteger": int(datetime.datetime.now().timestamp()),
            "StringPattern": "0123",
            "StringPatternWithDefault": "4567",
        }
        status, result, errmsg = Sanitizer.validate(
            obj, "Dummy", self.spec, with_default=True, with_typesafe=False
        )
        self.assertEqual(status, True)
        self.assertIsNone(errmsg)
        self.assertNotIn("Integer", result.keys())
        self.assertNotIn("Number", result.keys())
        self.assertNotIn("String", result.keys())
        self.assertNotIn("NullableInteger", result.keys())
        self.assertNotIn("NullableNumber", result.keys())
        self.assertNotIn("NullableString", result.keys())
        self.assertIn("IntegerWithDefault", result.keys())
        self.assertIn("NumberWithDefault", result.keys())
        self.assertIn("StringWithDefault", result.keys())
        self.assertIn("NullableIntegerWithDefault", result.keys())
        self.assertIn("NullableNumberWithDefault", result.keys())
        self.assertIn("NullableStringWithDefault", result.keys())

        obj = {
            "RequiredInteger": "1",
            "RequiredNumber": 1.5,
            "RequiredString": "required string",
            "RequiredIntegerWithDefault": 1,
            "RequiredNumberWithDefault": 1.5,
            "RequiredStringWithDefault": "required string with default",
            "RequiredNullableInteger": None,
            "RequiredNullableNumber": None,
            "RequiredNullableString": None,
            "RequiredNullableIntegerWithDefault": None,
            "RequiredNullableNumberWithDefault": None,
            "RequiredNullableStringWithDefault": None,
            "DateString": datetime.date.today().isoformat(),
            "DatetimeString": datetime.datetime.now().isoformat(),
            "DatetimeNumber": datetime.datetime.now().timestamp(),
            "DatetimeInteger": int(datetime.datetime.now().timestamp()),
            "StringPattern": "0123",
            "StringPatternWithDefault": "4567",
        }
        status, result, errmsg = Sanitizer.validate(
            obj, "Dummy", self.spec, with_default=True, with_typesafe=False
        )
        self.assertEqual(status, False)
        self.assertIsNotNone(errmsg)
        self.assertNotIn("Integer", result.keys())
        self.assertNotIn("Number", result.keys())
        self.assertNotIn("String", result.keys())
        self.assertNotIn("NullableInteger", result.keys())
        self.assertNotIn("NullableNumber", result.keys())
        self.assertNotIn("NullableString", result.keys())
        self.assertIn("IntegerWithDefault", result.keys())
        self.assertIn("NumberWithDefault", result.keys())
        self.assertIn("StringWithDefault", result.keys())
        self.assertIn("NullableIntegerWithDefault", result.keys())
        self.assertIn("NullableNumberWithDefault", result.keys())
        self.assertIn("NullableStringWithDefault", result.keys())

        obj = {
            "RequiredInteger": 1,
            "RequiredNumber": "1.5",
            "RequiredString": "required string",
            "RequiredIntegerWithDefault": 1,
            "RequiredNumberWithDefault": 1.5,
            "RequiredStringWithDefault": "required string with default",
            "RequiredNullableInteger": None,
            "RequiredNullableNumber": None,
            "RequiredNullableString": None,
            "RequiredNullableIntegerWithDefault": None,
            "RequiredNullableNumberWithDefault": None,
            "RequiredNullableStringWithDefault": None,
            "DateString": datetime.date.today().isoformat(),
            "DatetimeString": datetime.datetime.now().isoformat(),
            "DatetimeNumber": datetime.datetime.now().timestamp(),
            "DatetimeInteger": int(datetime.datetime.now().timestamp()),
            "StringPattern": "0123",
            "StringPatternWithDefault": "4567",
        }
        status, result, errmsg = Sanitizer.validate(
            obj, "Dummy", self.spec, with_default=True, with_typesafe=False
        )
        self.assertEqual(status, False)
        self.assertIsNotNone(errmsg)
        self.assertNotIn("Integer", result.keys())
        self.assertNotIn("Number", result.keys())
        self.assertNotIn("String", result.keys())
        self.assertNotIn("NullableInteger", result.keys())
        self.assertNotIn("NullableNumber", result.keys())
        self.assertNotIn("NullableString", result.keys())
        self.assertIn("IntegerWithDefault", result.keys())
        self.assertIn("NumberWithDefault", result.keys())
        self.assertIn("StringWithDefault", result.keys())
        self.assertIn("NullableIntegerWithDefault", result.keys())
        self.assertIn("NullableNumberWithDefault", result.keys())
        self.assertIn("NullableStringWithDefault", result.keys())

        obj = {
            "RequiredInteger": 1,
            "RequiredNumber": 1.5,
            "RequiredString": 12345,
            "RequiredIntegerWithDefault": 1,
            "RequiredNumberWithDefault": 1.5,
            "RequiredStringWithDefault": "required string with default",
            "RequiredNullableInteger": None,
            "RequiredNullableNumber": None,
            "RequiredNullableString": None,
            "RequiredNullableIntegerWithDefault": None,
            "RequiredNullableNumberWithDefault": None,
            "RequiredNullableStringWithDefault": None,
            "DateString": datetime.date.today().isoformat(),
            "DatetimeString": datetime.datetime.now().isoformat(),
            "DatetimeNumber": datetime.datetime.now().timestamp(),
            "DatetimeInteger": int(datetime.datetime.now().timestamp()),
            "StringPattern": "0123",
            "StringPatternWithDefault": "4567",
        }
        status, result, errmsg = Sanitizer.validate(
            obj, "Dummy", self.spec, with_default=True, with_typesafe=False
        )
        self.assertEqual(status, False)
        self.assertIsNotNone(errmsg)
        self.assertNotIn("Integer", result.keys())
        self.assertNotIn("Number", result.keys())
        self.assertNotIn("String", result.keys())
        self.assertNotIn("NullableInteger", result.keys())
        self.assertNotIn("NullableNumber", result.keys())
        self.assertNotIn("NullableString", result.keys())
        self.assertIn("IntegerWithDefault", result.keys())
        self.assertIn("NumberWithDefault", result.keys())
        self.assertIn("StringWithDefault", result.keys())
        self.assertIn("NullableIntegerWithDefault", result.keys())
        self.assertIn("NullableNumberWithDefault", result.keys())
        self.assertIn("NullableStringWithDefault", result.keys())

        obj = {
            "RequiredInteger": 1,
            "RequiredNumber": 1.5,
            "RequiredString": "required string",
            "RequiredIntegerWithDefault": 1.5,
            "RequiredNumberWithDefault": 1.5,
            "RequiredStringWithDefault": "required string with default",
            "RequiredNullableInteger": None,
            "RequiredNullableNumber": None,
            "RequiredNullableString": None,
            "RequiredNullableIntegerWithDefault": None,
            "RequiredNullableNumberWithDefault": None,
            "RequiredNullableStringWithDefault": None,
            "DateString": datetime.date.today().isoformat(),
            "DatetimeString": datetime.datetime.now().isoformat(),
            "DatetimeNumber": datetime.datetime.now().timestamp(),
            "DatetimeInteger": int(datetime.datetime.now().timestamp()),
            "StringPattern": "0123",
            "StringPatternWithDefault": "4567",
        }
        status, result, errmsg = Sanitizer.validate(
            obj, "Dummy", self.spec, with_default=True, with_typesafe=False
        )
        self.assertEqual(status, False)
        self.assertIsNotNone(errmsg)
        self.assertNotIn("Integer", result.keys())
        self.assertNotIn("Number", result.keys())
        self.assertNotIn("String", result.keys())
        self.assertNotIn("NullableInteger", result.keys())
        self.assertNotIn("NullableNumber", result.keys())
        self.assertNotIn("NullableString", result.keys())
        self.assertIn("IntegerWithDefault", result.keys())
        self.assertIn("NumberWithDefault", result.keys())
        self.assertIn("StringWithDefault", result.keys())
        self.assertIn("NullableIntegerWithDefault", result.keys())
        self.assertIn("NullableNumberWithDefault", result.keys())
        self.assertIn("NullableStringWithDefault", result.keys())

        obj = {
            "RequiredInteger": 1,
            "RequiredNumber": 1.5,
            "RequiredString": "required string",
            "RequiredIntegerWithDefault": 1,
            "RequiredNumberWithDefault": "1.5",
            "RequiredStringWithDefault": "required string with default",
            "RequiredNullableInteger": None,
            "RequiredNullableNumber": None,
            "RequiredNullableString": None,
            "RequiredNullableIntegerWithDefault": None,
            "RequiredNullableNumberWithDefault": None,
            "RequiredNullableStringWithDefault": None,
            "DateString": datetime.date.today().isoformat(),
            "DatetimeString": datetime.datetime.now().isoformat(),
            "DatetimeNumber": datetime.datetime.now().timestamp(),
            "DatetimeInteger": int(datetime.datetime.now().timestamp()),
            "StringPattern": "0123",
            "StringPatternWithDefault": "4567",
        }
        status, result, errmsg = Sanitizer.validate(
            obj, "Dummy", self.spec, with_default=True, with_typesafe=False
        )
        self.assertEqual(status, False)
        self.assertIsNotNone(errmsg)
        self.assertNotIn("Integer", result.keys())
        self.assertNotIn("Number", result.keys())
        self.assertNotIn("String", result.keys())
        self.assertNotIn("NullableInteger", result.keys())
        self.assertNotIn("NullableNumber", result.keys())
        self.assertNotIn("NullableString", result.keys())
        self.assertIn("IntegerWithDefault", result.keys())
        self.assertIn("NumberWithDefault", result.keys())
        self.assertIn("StringWithDefault", result.keys())
        self.assertIn("NullableIntegerWithDefault", result.keys())
        self.assertIn("NullableNumberWithDefault", result.keys())
        self.assertIn("NullableStringWithDefault", result.keys())

        obj = {
            "RequiredInteger": 1,
            "RequiredNumber": 1.5,
            "RequiredString": "required string",
            "RequiredIntegerWithDefault": 1,
            "RequiredNumberWithDefault": 1.5,
            "RequiredStringWithDefault": 12345,
            "RequiredNullableInteger": None,
            "RequiredNullableNumber": None,
            "RequiredNullableString": None,
            "RequiredNullableIntegerWithDefault": None,
            "RequiredNullableNumberWithDefault": None,
            "RequiredNullableStringWithDefault": None,
            "DateString": datetime.date.today().isoformat(),
            "DatetimeString": datetime.datetime.now().isoformat(),
            "DatetimeNumber": datetime.datetime.now().timestamp(),
            "DatetimeInteger": int(datetime.datetime.now().timestamp()),
            "StringPattern": "0123",
            "StringPatternWithDefault": "4567",
        }
        status, result, errmsg = Sanitizer.validate(
            obj, "Dummy", self.spec, with_default=True, with_typesafe=False
        )
        self.assertEqual(status, False)
        self.assertIsNotNone(errmsg)
        self.assertNotIn("Integer", result.keys())
        self.assertNotIn("Number", result.keys())
        self.assertNotIn("String", result.keys())
        self.assertNotIn("NullableInteger", result.keys())
        self.assertNotIn("NullableNumber", result.keys())
        self.assertNotIn("NullableString", result.keys())
        self.assertIn("IntegerWithDefault", result.keys())
        self.assertIn("NumberWithDefault", result.keys())
        self.assertIn("StringWithDefault", result.keys())
        self.assertIn("NullableIntegerWithDefault", result.keys())
        self.assertIn("NullableNumberWithDefault", result.keys())
        self.assertIn("NullableStringWithDefault", result.keys())

        obj = {
            "RequiredInteger": 1,
            "RequiredNumber": 1.5,
            "RequiredString": "required string",
            "RequiredIntegerWithDefault": 1,
            "RequiredNumberWithDefault": 1.5,
            "RequiredStringWithDefault": "required string with default",
            "RequiredNullableNumber": None,
            "RequiredNullableString": None,
            "RequiredNullableIntegerWithDefault": None,
            "RequiredNullableNumberWithDefault": None,
            "RequiredNullableStringWithDefault": None,
            "DateString": datetime.date.today().isoformat(),
            "DatetimeString": datetime.datetime.now().isoformat(),
            "DatetimeNumber": datetime.datetime.now().timestamp(),
            "DatetimeInteger": int(datetime.datetime.now().timestamp()),
            "StringPattern": "0123",
            "StringPatternWithDefault": "4567",
        }
        status, result, errmsg = Sanitizer.validate(
            obj, "Dummy", self.spec, with_default=True, with_typesafe=False
        )
        self.assertEqual(status, False)
        self.assertIsNotNone(errmsg)
        self.assertNotIn("Integer", result.keys())
        self.assertNotIn("Number", result.keys())
        self.assertNotIn("String", result.keys())
        self.assertNotIn("NullableInteger", result.keys())
        self.assertNotIn("NullableNumber", result.keys())
        self.assertNotIn("NullableString", result.keys())
        self.assertIn("IntegerWithDefault", result.keys())
        self.assertIn("NumberWithDefault", result.keys())
        self.assertIn("StringWithDefault", result.keys())
        self.assertIn("NullableIntegerWithDefault", result.keys())
        self.assertIn("NullableNumberWithDefault", result.keys())
        self.assertIn("NullableStringWithDefault", result.keys())

        obj = {
            "RequiredInteger": 1,
            "RequiredNumber": 1.5,
            "RequiredString": "required string",
            "RequiredIntegerWithDefault": 1,
            "RequiredNumberWithDefault": 1.5,
            "RequiredStringWithDefault": "required string with default",
            "RequiredNullableInteger": None,
            "RequiredNullableString": None,
            "RequiredNullableIntegerWithDefault": None,
            "RequiredNullableNumberWithDefault": None,
            "RequiredNullableStringWithDefault": None,
            "DateString": datetime.date.today().isoformat(),
            "DatetimeString": datetime.datetime.now().isoformat(),
            "DatetimeNumber": datetime.datetime.now().timestamp(),
            "DatetimeInteger": int(datetime.datetime.now().timestamp()),
            "StringPattern": "0123",
            "StringPatternWithDefault": "4567",
        }
        status, result, errmsg = Sanitizer.validate(
            obj, "Dummy", self.spec, with_default=True, with_typesafe=False
        )
        self.assertEqual(status, False)
        self.assertIsNotNone(errmsg)
        self.assertNotIn("Integer", result.keys())
        self.assertNotIn("Number", result.keys())
        self.assertNotIn("String", result.keys())
        self.assertNotIn("NullableInteger", result.keys())
        self.assertNotIn("NullableNumber", result.keys())
        self.assertNotIn("NullableString", result.keys())
        self.assertIn("IntegerWithDefault", result.keys())
        self.assertIn("NumberWithDefault", result.keys())
        self.assertIn("StringWithDefault", result.keys())
        self.assertIn("NullableIntegerWithDefault", result.keys())
        self.assertIn("NullableNumberWithDefault", result.keys())
        self.assertIn("NullableStringWithDefault", result.keys())

        obj = {
            "RequiredInteger": 1,
            "RequiredNumber": 1.5,
            "RequiredString": "required string",
            "RequiredIntegerWithDefault": 1,
            "RequiredNumberWithDefault": 1.5,
            "RequiredStringWithDefault": "required string with default",
            "RequiredNullableInteger": None,
            "RequiredNullableNumber": None,
            "RequiredNullableIntegerWithDefault": None,
            "RequiredNullableNumberWithDefault": None,
            "RequiredNullableStringWithDefault": None,
            "DateString": datetime.date.today().isoformat(),
            "DatetimeString": datetime.datetime.now().isoformat(),
            "DatetimeNumber": datetime.datetime.now().timestamp(),
            "DatetimeInteger": int(datetime.datetime.now().timestamp()),
            "StringPattern": "0123",
            "StringPatternWithDefault": "4567",
        }
        status, result, errmsg = Sanitizer.validate(
            obj, "Dummy", self.spec, with_default=True, with_typesafe=False
        )
        self.assertEqual(status, False)
        self.assertIsNotNone(errmsg)
        self.assertNotIn("Integer", result.keys())
        self.assertNotIn("Number", result.keys())
        self.assertNotIn("String", result.keys())
        self.assertNotIn("NullableInteger", result.keys())
        self.assertNotIn("NullableNumber", result.keys())
        self.assertNotIn("NullableString", result.keys())
        self.assertIn("IntegerWithDefault", result.keys())
        self.assertIn("NumberWithDefault", result.keys())
        self.assertIn("StringWithDefault", result.keys())
        self.assertIn("NullableIntegerWithDefault", result.keys())
        self.assertIn("NullableNumberWithDefault", result.keys())
        self.assertIn("NullableStringWithDefault", result.keys())

        obj = {
            "RequiredInteger": 1,
            "RequiredNumber": 1.5,
            "RequiredString": "required string",
            "RequiredIntegerWithDefault": 1,
            "RequiredNumberWithDefault": 1.5,
            "RequiredStringWithDefault": "required string with default",
            "RequiredNullableInteger": None,
            "RequiredNullableNumber": None,
            "RequiredNullableString": None,
            "RequiredNullableNumberWithDefault": None,
            "RequiredNullableStringWithDefault": None,
            "DateString": datetime.date.today().isoformat(),
            "DatetimeString": datetime.datetime.now().isoformat(),
            "DatetimeNumber": datetime.datetime.now().timestamp(),
            "DatetimeInteger": int(datetime.datetime.now().timestamp()),
            "StringPattern": "0123",
            "StringPatternWithDefault": "4567",
        }
        status, result, errmsg = Sanitizer.validate(
            obj, "Dummy", self.spec, with_default=True, with_typesafe=False
        )
        self.assertEqual(status, False)
        self.assertIsNotNone(errmsg)
        self.assertNotIn("Integer", result.keys())
        self.assertNotIn("Number", result.keys())
        self.assertNotIn("String", result.keys())
        self.assertNotIn("NullableInteger", result.keys())
        self.assertNotIn("NullableNumber", result.keys())
        self.assertNotIn("NullableString", result.keys())
        self.assertIn("IntegerWithDefault", result.keys())
        self.assertIn("NumberWithDefault", result.keys())
        self.assertIn("StringWithDefault", result.keys())
        self.assertIn("NullableIntegerWithDefault", result.keys())
        self.assertIn("NullableNumberWithDefault", result.keys())
        self.assertIn("NullableStringWithDefault", result.keys())

        obj = {
            "RequiredInteger": 1,
            "RequiredNumber": 1.5,
            "RequiredString": "required string",
            "RequiredIntegerWithDefault": 1,
            "RequiredNumberWithDefault": 1.5,
            "RequiredStringWithDefault": "required string with default",
            "RequiredNullableInteger": None,
            "RequiredNullableNumber": None,
            "RequiredNullableString": None,
            "RequiredNullableIntegerWithDefault": None,
            "RequiredNullableStringWithDefault": None,
            "DateString": datetime.date.today().isoformat(),
            "DatetimeString": datetime.datetime.now().isoformat(),
            "DatetimeNumber": datetime.datetime.now().timestamp(),
            "DatetimeInteger": int(datetime.datetime.now().timestamp()),
            "StringPattern": "0123",
            "StringPatternWithDefault": "4567",
        }
        status, result, errmsg = Sanitizer.validate(
            obj, "Dummy", self.spec, with_default=True, with_typesafe=False
        )
        self.assertEqual(status, False)
        self.assertIsNotNone(errmsg)
        self.assertNotIn("Integer", result.keys())
        self.assertNotIn("Number", result.keys())
        self.assertNotIn("String", result.keys())
        self.assertNotIn("NullableInteger", result.keys())
        self.assertNotIn("NullableNumber", result.keys())
        self.assertNotIn("NullableString", result.keys())
        self.assertIn("IntegerWithDefault", result.keys())
        self.assertIn("NumberWithDefault", result.keys())
        self.assertIn("StringWithDefault", result.keys())
        self.assertIn("NullableIntegerWithDefault", result.keys())
        self.assertIn("NullableNumberWithDefault", result.keys())
        self.assertIn("NullableStringWithDefault", result.keys())

        obj = {
            "RequiredInteger": 1,
            "RequiredNumber": 1.5,
            "RequiredString": "required string",
            "RequiredIntegerWithDefault": 1,
            "RequiredNumberWithDefault": 1.5,
            "RequiredStringWithDefault": "required string with default",
            "RequiredNullableInteger": None,
            "RequiredNullableNumber": None,
            "RequiredNullableString": None,
            "RequiredNullableIntegerWithDefault": None,
            "RequiredNullableNumberWithDefault": None,
            "DateString": datetime.date.today().isoformat(),
            "DatetimeString": datetime.datetime.now().isoformat(),
            "DatetimeNumber": datetime.datetime.now().timestamp(),
            "DatetimeInteger": int(datetime.datetime.now().timestamp()),
            "StringPattern": "0123",
            "StringPatternWithDefault": "4567",
        }
        status, result, errmsg = Sanitizer.validate(
            obj, "Dummy", self.spec, with_default=True, with_typesafe=False
        )
        self.assertEqual(status, False)
        self.assertIsNotNone(errmsg)
        self.assertNotIn("Integer", result.keys())
        self.assertNotIn("Number", result.keys())
        self.assertNotIn("String", result.keys())
        self.assertNotIn("NullableInteger", result.keys())
        self.assertNotIn("NullableNumber", result.keys())
        self.assertNotIn("NullableString", result.keys())
        self.assertIn("IntegerWithDefault", result.keys())
        self.assertIn("NumberWithDefault", result.keys())
        self.assertIn("StringWithDefault", result.keys())
        self.assertIn("NullableIntegerWithDefault", result.keys())
        self.assertIn("NullableNumberWithDefault", result.keys())
        self.assertIn("NullableStringWithDefault", result.keys())

        obj = {
            "RequiredInteger": 1,
            "RequiredNumber": 1.5,
            "RequiredString": "required string",
            "RequiredIntegerWithDefault": 1,
            "RequiredNumberWithDefault": 1.5,
            "RequiredStringWithDefault": "required string with default",
            "RequiredNullableInteger": None,
            "RequiredNullableNumber": None,
            "RequiredNullableString": None,
            "RequiredNullableIntegerWithDefault": None,
            "RequiredNullableNumberWithDefault": None,
            "RequiredNullableStringWithDefault": None,
            "DateString": datetime.date.today(),
            "DatetimeString": datetime.datetime.now().isoformat(),
            "DatetimeNumber": datetime.datetime.now().timestamp(),
            "DatetimeInteger": int(datetime.datetime.now().timestamp()),
            "StringPattern": "0123",
            "StringPatternWithDefault": "4567",
        }
        status, result, errmsg = Sanitizer.validate(
            obj, "Dummy", self.spec, with_default=True, with_typesafe=False
        )
        self.assertEqual(status, False)
        self.assertIsNotNone(errmsg)
        self.assertNotIn("Integer", result.keys())
        self.assertNotIn("Number", result.keys())
        self.assertNotIn("String", result.keys())
        self.assertNotIn("NullableInteger", result.keys())
        self.assertNotIn("NullableNumber", result.keys())
        self.assertNotIn("NullableString", result.keys())
        self.assertIn("IntegerWithDefault", result.keys())
        self.assertIn("NumberWithDefault", result.keys())
        self.assertIn("StringWithDefault", result.keys())
        self.assertIn("NullableIntegerWithDefault", result.keys())
        self.assertIn("NullableNumberWithDefault", result.keys())
        self.assertIn("NullableStringWithDefault", result.keys())

        obj = {
            "RequiredInteger": 1,
            "RequiredNumber": 1.5,
            "RequiredString": "required string",
            "RequiredIntegerWithDefault": 1,
            "RequiredNumberWithDefault": 1.5,
            "RequiredStringWithDefault": "required string with default",
            "RequiredNullableInteger": None,
            "RequiredNullableNumber": None,
            "RequiredNullableString": None,
            "RequiredNullableIntegerWithDefault": None,
            "RequiredNullableNumberWithDefault": None,
            "RequiredNullableStringWithDefault": None,
            "DateString": datetime.date.today().isoformat(),
            "DatetimeString": datetime.datetime.now(),
            "DatetimeNumber": datetime.datetime.now().timestamp(),
            "DatetimeInteger": int(datetime.datetime.now().timestamp()),
            "StringPattern": "0123",
            "StringPatternWithDefault": "4567",
        }
        status, result, errmsg = Sanitizer.validate(
            obj, "Dummy", self.spec, with_default=True, with_typesafe=False
        )
        self.assertEqual(status, False)
        self.assertIsNotNone(errmsg)
        self.assertNotIn("Integer", result.keys())
        self.assertNotIn("Number", result.keys())
        self.assertNotIn("String", result.keys())
        self.assertNotIn("NullableInteger", result.keys())
        self.assertNotIn("NullableNumber", result.keys())
        self.assertNotIn("NullableString", result.keys())
        self.assertIn("IntegerWithDefault", result.keys())
        self.assertIn("NumberWithDefault", result.keys())
        self.assertIn("StringWithDefault", result.keys())
        self.assertIn("NullableIntegerWithDefault", result.keys())
        self.assertIn("NullableNumberWithDefault", result.keys())
        self.assertIn("NullableStringWithDefault", result.keys())

        obj = {
            "RequiredInteger": 1,
            "RequiredNumber": 1.5,
            "RequiredString": "required string",
            "RequiredIntegerWithDefault": 1,
            "RequiredNumberWithDefault": 1.5,
            "RequiredStringWithDefault": "required string with default",
            "RequiredNullableInteger": None,
            "RequiredNullableNumber": None,
            "RequiredNullableString": None,
            "RequiredNullableIntegerWithDefault": None,
            "RequiredNullableNumberWithDefault": None,
            "RequiredNullableStringWithDefault": None,
            "DateString": datetime.date.today().isoformat(),
            "DatetimeString": datetime.datetime.now().isoformat(),
            "DatetimeNumber": datetime.datetime.now(),
            "DatetimeInteger": int(datetime.datetime.now().timestamp()),
            "StringPattern": "0123",
            "StringPatternWithDefault": "4567",
        }
        status, result, errmsg = Sanitizer.validate(
            obj, "Dummy", self.spec, with_default=True, with_typesafe=False
        )
        self.assertEqual(status, False)
        self.assertIsNotNone(errmsg)
        self.assertNotIn("Integer", result.keys())
        self.assertNotIn("Number", result.keys())
        self.assertNotIn("String", result.keys())
        self.assertNotIn("NullableInteger", result.keys())
        self.assertNotIn("NullableNumber", result.keys())
        self.assertNotIn("NullableString", result.keys())
        self.assertIn("IntegerWithDefault", result.keys())
        self.assertIn("NumberWithDefault", result.keys())
        self.assertIn("StringWithDefault", result.keys())
        self.assertIn("NullableIntegerWithDefault", result.keys())
        self.assertIn("NullableNumberWithDefault", result.keys())
        self.assertIn("NullableStringWithDefault", result.keys())

        obj = {
            "RequiredInteger": 1,
            "RequiredNumber": 1.5,
            "RequiredString": "required string",
            "RequiredIntegerWithDefault": 1,
            "RequiredNumberWithDefault": 1.5,
            "RequiredStringWithDefault": "required string with default",
            "RequiredNullableInteger": None,
            "RequiredNullableNumber": None,
            "RequiredNullableString": None,
            "RequiredNullableIntegerWithDefault": None,
            "RequiredNullableNumberWithDefault": None,
            "RequiredNullableStringWithDefault": None,
            "DateString": datetime.date.today().isoformat(),
            "DatetimeString": datetime.datetime.now().isoformat(),
            "DatetimeNumber": datetime.datetime.now().timestamp(),
            "DatetimeInteger": datetime.datetime.now(),
            "StringPattern": "0123",
            "StringPatternWithDefault": "4567",
        }
        status, result, errmsg = Sanitizer.validate(
            obj, "Dummy", self.spec, with_default=True, with_typesafe=False
        )
        self.assertEqual(status, False)
        self.assertIsNotNone(errmsg)
        self.assertNotIn("Integer", result.keys())
        self.assertNotIn("Number", result.keys())
        self.assertNotIn("String", result.keys())
        self.assertNotIn("NullableInteger", result.keys())
        self.assertNotIn("NullableNumber", result.keys())
        self.assertNotIn("NullableString", result.keys())
        self.assertIn("IntegerWithDefault", result.keys())
        self.assertIn("NumberWithDefault", result.keys())
        self.assertIn("StringWithDefault", result.keys())
        self.assertIn("NullableIntegerWithDefault", result.keys())
        self.assertIn("NullableNumberWithDefault", result.keys())
        self.assertIn("NullableStringWithDefault", result.keys())

        obj = {
            "RequiredInteger": 1,
            "RequiredNumber": 1.5,
            "RequiredString": "required string",
            "RequiredIntegerWithDefault": 1,
            "RequiredNumberWithDefault": 1.5,
            "RequiredStringWithDefault": "required string with default",
            "RequiredNullableInteger": None,
            "RequiredNullableNumber": None,
            "RequiredNullableString": None,
            "RequiredNullableIntegerWithDefault": None,
            "RequiredNullableNumberWithDefault": None,
            "RequiredNullableStringWithDefault": None,
            "DateString": datetime.date.today().isoformat(),
            "DatetimeString": datetime.datetime.now().isoformat(),
            "DatetimeNumber": datetime.datetime.now().timestamp(),
            "DatetimeInteger": datetime.datetime.now().timestamp(),
            "StringPattern": "01234",
            "StringPatternWithDefault": "4567",
        }
        status, result, errmsg = Sanitizer.validate(
            obj, "Dummy", self.spec, with_default=True, with_typesafe=False
        )
        self.assertEqual(status, False)
        self.assertIsNotNone(errmsg)
        self.assertNotIn("Integer", result.keys())
        self.assertNotIn("Number", result.keys())
        self.assertNotIn("String", result.keys())
        self.assertNotIn("NullableInteger", result.keys())
        self.assertNotIn("NullableNumber", result.keys())
        self.assertNotIn("NullableString", result.keys())
        self.assertIn("IntegerWithDefault", result.keys())
        self.assertIn("NumberWithDefault", result.keys())
        self.assertIn("StringWithDefault", result.keys())
        self.assertIn("NullableIntegerWithDefault", result.keys())
        self.assertIn("NullableNumberWithDefault", result.keys())
        self.assertIn("NullableStringWithDefault", result.keys())

        obj = {
            "RequiredInteger": 1,
            "RequiredNumber": 1.5,
            "RequiredString": "required string",
            "RequiredIntegerWithDefault": 1,
            "RequiredNumberWithDefault": 1.5,
            "RequiredStringWithDefault": "required string with default",
            "RequiredNullableInteger": None,
            "RequiredNullableNumber": None,
            "RequiredNullableString": None,
            "RequiredNullableIntegerWithDefault": None,
            "RequiredNullableNumberWithDefault": None,
            "RequiredNullableStringWithDefault": None,
            "DateString": datetime.date.today().isoformat(),
            "DatetimeString": datetime.datetime.now().isoformat(),
            "DatetimeNumber": datetime.datetime.now().timestamp(),
            "DatetimeInteger": datetime.datetime.now().timestamp(),
            "StringPattern": "0123",
            "StringPatternWithDefault": "45678",
        }
        status, result, errmsg = Sanitizer.validate(
            obj, "Dummy", self.spec, with_default=True, with_typesafe=False
        )
        self.assertEqual(status, False)
        self.assertIsNotNone(errmsg)
        self.assertNotIn("Integer", result.keys())
        self.assertNotIn("Number", result.keys())
        self.assertNotIn("String", result.keys())
        self.assertNotIn("NullableInteger", result.keys())
        self.assertNotIn("NullableNumber", result.keys())
        self.assertNotIn("NullableString", result.keys())
        self.assertIn("IntegerWithDefault", result.keys())
        self.assertIn("NumberWithDefault", result.keys())
        self.assertIn("StringWithDefault", result.keys())
        self.assertIn("NullableIntegerWithDefault", result.keys())
        self.assertIn("NullableNumberWithDefault", result.keys())
        self.assertIn("NullableStringWithDefault", result.keys())

    def test_003_validate_with_typesafe(self):
        obj = {
            "RequiredInteger": 1,
            "RequiredNumber": 1.5,
            "RequiredString": "required string",
            "RequiredIntegerWithDefault": 1,
            "RequiredNumberWithDefault": 1.5,
            "RequiredStringWithDefault": "required string with default",
            "RequiredNullableInteger": None,
            "RequiredNullableNumber": None,
            "RequiredNullableString": None,
            "RequiredNullableIntegerWithDefault": None,
            "RequiredNullableNumberWithDefault": None,
            "RequiredNullableStringWithDefault": None,
            "DateString": datetime.date.today().isoformat(),
            "DatetimeString": datetime.datetime.now().isoformat(),
            "DatetimeNumber": datetime.datetime.now().timestamp(),
            "DatetimeInteger": int(datetime.datetime.now().timestamp()),
            "StringPattern": "0123",
            "StringPatternWithDefault": "4567",
        }
        status, result, errmsg = Sanitizer.validate(
            obj, "Dummy", self.spec, with_default=False, with_typesafe=True
        )
        self.assertEqual(status, True)
        self.assertIsNone(errmsg)
        self.assertNotIn("Integer", result.keys())
        self.assertNotIn("Number", result.keys())
        self.assertNotIn("String", result.keys())
        self.assertNotIn("NullableInteger", result.keys())
        self.assertNotIn("NullableNumber", result.keys())
        self.assertNotIn("NullableString", result.keys())
        self.assertNotIn("IntegerWithDefault", result.keys())
        self.assertNotIn("NumberWithDefault", result.keys())
        self.assertNotIn("StringWithDefault", result.keys())
        self.assertNotIn("NullableIntegerWithDefault", result.keys())
        self.assertNotIn("NullableNumberWithDefault", result.keys())
        self.assertNotIn("NullableStringWithDefault", result.keys())

        obj = {
            "RequiredInteger": "1",
            "RequiredNumber": 1.5,
            "RequiredString": "required string",
            "RequiredIntegerWithDefault": 1,
            "RequiredNumberWithDefault": 1.5,
            "RequiredStringWithDefault": "required string with default",
            "RequiredNullableInteger": None,
            "RequiredNullableNumber": None,
            "RequiredNullableString": None,
            "RequiredNullableIntegerWithDefault": None,
            "RequiredNullableNumberWithDefault": None,
            "RequiredNullableStringWithDefault": None,
            "DateString": datetime.date.today().isoformat(),
            "DatetimeString": datetime.datetime.now().isoformat(),
            "DatetimeNumber": datetime.datetime.now().timestamp(),
            "DatetimeInteger": int(datetime.datetime.now().timestamp()),
            "StringPattern": "0123",
            "StringPatternWithDefault": "4567",
        }
        status, result, errmsg = Sanitizer.validate(
            obj, "Dummy", self.spec, with_default=False, with_typesafe=True
        )
        self.assertEqual(status, True)
        self.assertIsNone(errmsg)
        self.assertNotIn("Integer", result.keys())
        self.assertNotIn("Number", result.keys())
        self.assertNotIn("String", result.keys())
        self.assertNotIn("NullableInteger", result.keys())
        self.assertNotIn("NullableNumber", result.keys())
        self.assertNotIn("NullableString", result.keys())
        self.assertNotIn("IntegerWithDefault", result.keys())
        self.assertNotIn("NumberWithDefault", result.keys())
        self.assertNotIn("StringWithDefault", result.keys())
        self.assertNotIn("NullableIntegerWithDefault", result.keys())
        self.assertNotIn("NullableNumberWithDefault", result.keys())
        self.assertNotIn("NullableStringWithDefault", result.keys())

        obj = {
            "RequiredInteger": 1,
            "RequiredNumber": "1.5",
            "RequiredString": "required string",
            "RequiredIntegerWithDefault": 1,
            "RequiredNumberWithDefault": 1.5,
            "RequiredStringWithDefault": "required string with default",
            "RequiredNullableInteger": None,
            "RequiredNullableNumber": None,
            "RequiredNullableString": None,
            "RequiredNullableIntegerWithDefault": None,
            "RequiredNullableNumberWithDefault": None,
            "RequiredNullableStringWithDefault": None,
            "DateString": datetime.date.today().isoformat(),
            "DatetimeString": datetime.datetime.now().isoformat(),
            "DatetimeNumber": datetime.datetime.now().timestamp(),
            "DatetimeInteger": int(datetime.datetime.now().timestamp()),
            "StringPattern": "0123",
            "StringPatternWithDefault": "4567",
        }
        status, result, errmsg = Sanitizer.validate(
            obj, "Dummy", self.spec, with_default=False, with_typesafe=True
        )
        self.assertEqual(status, True)
        self.assertIsNone(errmsg)
        self.assertNotIn("Integer", result.keys())
        self.assertNotIn("Number", result.keys())
        self.assertNotIn("String", result.keys())
        self.assertNotIn("NullableInteger", result.keys())
        self.assertNotIn("NullableNumber", result.keys())
        self.assertNotIn("NullableString", result.keys())
        self.assertNotIn("IntegerWithDefault", result.keys())
        self.assertNotIn("NumberWithDefault", result.keys())
        self.assertNotIn("StringWithDefault", result.keys())
        self.assertNotIn("NullableIntegerWithDefault", result.keys())
        self.assertNotIn("NullableNumberWithDefault", result.keys())
        self.assertNotIn("NullableStringWithDefault", result.keys())

        obj = {
            "RequiredInteger": 1,
            "RequiredNumber": 1.5,
            "RequiredString": 12345,
            "RequiredIntegerWithDefault": 1,
            "RequiredNumberWithDefault": 1.5,
            "RequiredStringWithDefault": "required string with default",
            "RequiredNullableInteger": None,
            "RequiredNullableNumber": None,
            "RequiredNullableString": None,
            "RequiredNullableIntegerWithDefault": None,
            "RequiredNullableNumberWithDefault": None,
            "RequiredNullableStringWithDefault": None,
            "DateString": datetime.date.today().isoformat(),
            "DatetimeString": datetime.datetime.now().isoformat(),
            "DatetimeNumber": datetime.datetime.now().timestamp(),
            "DatetimeInteger": int(datetime.datetime.now().timestamp()),
            "StringPattern": "0123",
            "StringPatternWithDefault": "4567",
        }
        status, result, errmsg = Sanitizer.validate(
            obj, "Dummy", self.spec, with_default=False, with_typesafe=True
        )
        self.assertEqual(status, True)
        self.assertIsNone(errmsg)
        self.assertNotIn("Integer", result.keys())
        self.assertNotIn("Number", result.keys())
        self.assertNotIn("String", result.keys())
        self.assertNotIn("NullableInteger", result.keys())
        self.assertNotIn("NullableNumber", result.keys())
        self.assertNotIn("NullableString", result.keys())
        self.assertNotIn("IntegerWithDefault", result.keys())
        self.assertNotIn("NumberWithDefault", result.keys())
        self.assertNotIn("StringWithDefault", result.keys())
        self.assertNotIn("NullableIntegerWithDefault", result.keys())
        self.assertNotIn("NullableNumberWithDefault", result.keys())
        self.assertNotIn("NullableStringWithDefault", result.keys())

        obj = {
            "RequiredInteger": 1,
            "RequiredNumber": 1.5,
            "RequiredString": "required string",
            "RequiredIntegerWithDefault": 1.5,
            "RequiredNumberWithDefault": 1.5,
            "RequiredStringWithDefault": "required string with default",
            "RequiredNullableInteger": None,
            "RequiredNullableNumber": None,
            "RequiredNullableString": None,
            "RequiredNullableIntegerWithDefault": None,
            "RequiredNullableNumberWithDefault": None,
            "RequiredNullableStringWithDefault": None,
            "DateString": datetime.date.today().isoformat(),
            "DatetimeString": datetime.datetime.now().isoformat(),
            "DatetimeNumber": datetime.datetime.now().timestamp(),
            "DatetimeInteger": int(datetime.datetime.now().timestamp()),
            "StringPattern": "0123",
            "StringPatternWithDefault": "4567",
        }
        status, result, errmsg = Sanitizer.validate(
            obj, "Dummy", self.spec, with_default=False, with_typesafe=True
        )
        self.assertEqual(status, True)
        self.assertIsNone(errmsg)
        self.assertNotIn("Integer", result.keys())
        self.assertNotIn("Number", result.keys())
        self.assertNotIn("String", result.keys())
        self.assertNotIn("NullableInteger", result.keys())
        self.assertNotIn("NullableNumber", result.keys())
        self.assertNotIn("NullableString", result.keys())
        self.assertNotIn("IntegerWithDefault", result.keys())
        self.assertNotIn("NumberWithDefault", result.keys())
        self.assertNotIn("StringWithDefault", result.keys())
        self.assertNotIn("NullableIntegerWithDefault", result.keys())
        self.assertNotIn("NullableNumberWithDefault", result.keys())
        self.assertNotIn("NullableStringWithDefault", result.keys())

        obj = {
            "RequiredInteger": 1,
            "RequiredNumber": 1.5,
            "RequiredString": "required string",
            "RequiredIntegerWithDefault": 1,
            "RequiredNumberWithDefault": "1.5",
            "RequiredStringWithDefault": "required string with default",
            "RequiredNullableInteger": None,
            "RequiredNullableNumber": None,
            "RequiredNullableString": None,
            "RequiredNullableIntegerWithDefault": None,
            "RequiredNullableNumberWithDefault": None,
            "RequiredNullableStringWithDefault": None,
            "DateString": datetime.date.today().isoformat(),
            "DatetimeString": datetime.datetime.now().isoformat(),
            "DatetimeNumber": datetime.datetime.now().timestamp(),
            "DatetimeInteger": int(datetime.datetime.now().timestamp()),
            "StringPattern": "0123",
            "StringPatternWithDefault": "4567",
        }
        status, result, errmsg = Sanitizer.validate(
            obj, "Dummy", self.spec, with_default=False, with_typesafe=True
        )
        self.assertEqual(status, True)
        self.assertIsNone(errmsg)
        self.assertNotIn("Integer", result.keys())
        self.assertNotIn("Number", result.keys())
        self.assertNotIn("String", result.keys())
        self.assertNotIn("NullableInteger", result.keys())
        self.assertNotIn("NullableNumber", result.keys())
        self.assertNotIn("NullableString", result.keys())
        self.assertNotIn("IntegerWithDefault", result.keys())
        self.assertNotIn("NumberWithDefault", result.keys())
        self.assertNotIn("StringWithDefault", result.keys())
        self.assertNotIn("NullableIntegerWithDefault", result.keys())
        self.assertNotIn("NullableNumberWithDefault", result.keys())
        self.assertNotIn("NullableStringWithDefault", result.keys())

        obj = {
            "RequiredInteger": 1,
            "RequiredNumber": 1.5,
            "RequiredString": "required string",
            "RequiredIntegerWithDefault": 1,
            "RequiredNumberWithDefault": 1.5,
            "RequiredStringWithDefault": 12345,
            "RequiredNullableInteger": None,
            "RequiredNullableNumber": None,
            "RequiredNullableString": None,
            "RequiredNullableIntegerWithDefault": None,
            "RequiredNullableNumberWithDefault": None,
            "RequiredNullableStringWithDefault": None,
            "DateString": datetime.date.today().isoformat(),
            "DatetimeString": datetime.datetime.now().isoformat(),
            "DatetimeNumber": datetime.datetime.now().timestamp(),
            "DatetimeInteger": int(datetime.datetime.now().timestamp()),
            "StringPattern": "0123",
            "StringPatternWithDefault": "4567",
        }
        status, result, errmsg = Sanitizer.validate(
            obj, "Dummy", self.spec, with_default=False, with_typesafe=True
        )
        self.assertEqual(status, True)
        self.assertIsNone(errmsg)
        self.assertNotIn("Integer", result.keys())
        self.assertNotIn("Number", result.keys())
        self.assertNotIn("String", result.keys())
        self.assertNotIn("NullableInteger", result.keys())
        self.assertNotIn("NullableNumber", result.keys())
        self.assertNotIn("NullableString", result.keys())
        self.assertNotIn("IntegerWithDefault", result.keys())
        self.assertNotIn("NumberWithDefault", result.keys())
        self.assertNotIn("StringWithDefault", result.keys())
        self.assertNotIn("NullableIntegerWithDefault", result.keys())
        self.assertNotIn("NullableNumberWithDefault", result.keys())
        self.assertNotIn("NullableStringWithDefault", result.keys())

        obj = {
            "RequiredInteger": 1,
            "RequiredNumber": 1.5,
            "RequiredString": "required string",
            "RequiredIntegerWithDefault": 1,
            "RequiredNumberWithDefault": 1.5,
            "RequiredStringWithDefault": "required string with default",
            "RequiredNullableNumber": None,
            "RequiredNullableString": None,
            "RequiredNullableIntegerWithDefault": None,
            "RequiredNullableNumberWithDefault": None,
            "RequiredNullableStringWithDefault": None,
            "DateString": datetime.date.today().isoformat(),
            "DatetimeString": datetime.datetime.now().isoformat(),
            "DatetimeNumber": datetime.datetime.now().timestamp(),
            "DatetimeInteger": int(datetime.datetime.now().timestamp()),
            "StringPattern": "0123",
            "StringPatternWithDefault": "4567",
        }
        status, result, errmsg = Sanitizer.validate(
            obj, "Dummy", self.spec, with_default=False, with_typesafe=True
        )
        self.assertEqual(status, False)
        self.assertIsNotNone(errmsg)
        self.assertNotIn("Integer", result.keys())
        self.assertNotIn("Number", result.keys())
        self.assertNotIn("String", result.keys())
        self.assertNotIn("NullableInteger", result.keys())
        self.assertNotIn("NullableNumber", result.keys())
        self.assertNotIn("NullableString", result.keys())
        self.assertNotIn("IntegerWithDefault", result.keys())
        self.assertNotIn("NumberWithDefault", result.keys())
        self.assertNotIn("StringWithDefault", result.keys())
        self.assertNotIn("NullableIntegerWithDefault", result.keys())
        self.assertNotIn("NullableNumberWithDefault", result.keys())
        self.assertNotIn("NullableStringWithDefault", result.keys())

        obj = {
            "RequiredInteger": 1,
            "RequiredNumber": 1.5,
            "RequiredString": "required string",
            "RequiredIntegerWithDefault": 1,
            "RequiredNumberWithDefault": 1.5,
            "RequiredStringWithDefault": "required string with default",
            "RequiredNullableInteger": None,
            "RequiredNullableString": None,
            "RequiredNullableIntegerWithDefault": None,
            "RequiredNullableNumberWithDefault": None,
            "RequiredNullableStringWithDefault": None,
            "DateString": datetime.date.today().isoformat(),
            "DatetimeString": datetime.datetime.now().isoformat(),
            "DatetimeNumber": datetime.datetime.now().timestamp(),
            "DatetimeInteger": int(datetime.datetime.now().timestamp()),
            "StringPattern": "0123",
            "StringPatternWithDefault": "4567",
        }
        status, result, errmsg = Sanitizer.validate(
            obj, "Dummy", self.spec, with_default=False, with_typesafe=True
        )
        self.assertEqual(status, False)
        self.assertIsNotNone(errmsg)
        self.assertNotIn("Integer", result.keys())
        self.assertNotIn("Number", result.keys())
        self.assertNotIn("String", result.keys())
        self.assertNotIn("NullableInteger", result.keys())
        self.assertNotIn("NullableNumber", result.keys())
        self.assertNotIn("NullableString", result.keys())
        self.assertNotIn("IntegerWithDefault", result.keys())
        self.assertNotIn("NumberWithDefault", result.keys())
        self.assertNotIn("StringWithDefault", result.keys())
        self.assertNotIn("NullableIntegerWithDefault", result.keys())
        self.assertNotIn("NullableNumberWithDefault", result.keys())
        self.assertNotIn("NullableStringWithDefault", result.keys())

        obj = {
            "RequiredInteger": 1,
            "RequiredNumber": 1.5,
            "RequiredString": "required string",
            "RequiredIntegerWithDefault": 1,
            "RequiredNumberWithDefault": 1.5,
            "RequiredStringWithDefault": "required string with default",
            "RequiredNullableInteger": None,
            "RequiredNullableNumber": None,
            "RequiredNullableIntegerWithDefault": None,
            "RequiredNullableNumberWithDefault": None,
            "RequiredNullableStringWithDefault": None,
            "DateString": datetime.date.today().isoformat(),
            "DatetimeString": datetime.datetime.now().isoformat(),
            "DatetimeNumber": datetime.datetime.now().timestamp(),
            "DatetimeInteger": int(datetime.datetime.now().timestamp()),
            "StringPattern": "0123",
            "StringPatternWithDefault": "4567",
        }
        status, result, errmsg = Sanitizer.validate(
            obj, "Dummy", self.spec, with_default=False, with_typesafe=True
        )
        self.assertEqual(status, False)
        self.assertIsNotNone(errmsg)
        self.assertNotIn("Integer", result.keys())
        self.assertNotIn("Number", result.keys())
        self.assertNotIn("String", result.keys())
        self.assertNotIn("NullableInteger", result.keys())
        self.assertNotIn("NullableNumber", result.keys())
        self.assertNotIn("NullableString", result.keys())
        self.assertNotIn("IntegerWithDefault", result.keys())
        self.assertNotIn("NumberWithDefault", result.keys())
        self.assertNotIn("StringWithDefault", result.keys())
        self.assertNotIn("NullableIntegerWithDefault", result.keys())
        self.assertNotIn("NullableNumberWithDefault", result.keys())
        self.assertNotIn("NullableStringWithDefault", result.keys())

        obj = {
            "RequiredInteger": 1,
            "RequiredNumber": 1.5,
            "RequiredString": "required string",
            "RequiredIntegerWithDefault": 1,
            "RequiredNumberWithDefault": 1.5,
            "RequiredStringWithDefault": "required string with default",
            "RequiredNullableInteger": None,
            "RequiredNullableNumber": None,
            "RequiredNullableString": None,
            "RequiredNullableNumberWithDefault": None,
            "RequiredNullableStringWithDefault": None,
            "DateString": datetime.date.today().isoformat(),
            "DatetimeString": datetime.datetime.now().isoformat(),
            "DatetimeNumber": datetime.datetime.now().timestamp(),
            "DatetimeInteger": int(datetime.datetime.now().timestamp()),
            "StringPattern": "0123",
            "StringPatternWithDefault": "4567",
        }
        status, result, errmsg = Sanitizer.validate(
            obj, "Dummy", self.spec, with_default=False, with_typesafe=True
        )
        self.assertEqual(status, False)
        self.assertIsNotNone(errmsg)
        self.assertNotIn("Integer", result.keys())
        self.assertNotIn("Number", result.keys())
        self.assertNotIn("String", result.keys())
        self.assertNotIn("NullableInteger", result.keys())
        self.assertNotIn("NullableNumber", result.keys())
        self.assertNotIn("NullableString", result.keys())
        self.assertNotIn("IntegerWithDefault", result.keys())
        self.assertNotIn("NumberWithDefault", result.keys())
        self.assertNotIn("StringWithDefault", result.keys())
        self.assertNotIn("NullableIntegerWithDefault", result.keys())
        self.assertNotIn("NullableNumberWithDefault", result.keys())
        self.assertNotIn("NullableStringWithDefault", result.keys())

        obj = {
            "RequiredInteger": 1,
            "RequiredNumber": 1.5,
            "RequiredString": "required string",
            "RequiredIntegerWithDefault": 1,
            "RequiredNumberWithDefault": 1.5,
            "RequiredStringWithDefault": "required string with default",
            "RequiredNullableInteger": None,
            "RequiredNullableNumber": None,
            "RequiredNullableString": None,
            "RequiredNullableIntegerWithDefault": None,
            "RequiredNullableStringWithDefault": None,
            "DateString": datetime.date.today().isoformat(),
            "DatetimeString": datetime.datetime.now().isoformat(),
            "DatetimeNumber": datetime.datetime.now().timestamp(),
            "DatetimeInteger": int(datetime.datetime.now().timestamp()),
            "StringPattern": "0123",
            "StringPatternWithDefault": "4567",
        }
        status, result, errmsg = Sanitizer.validate(
            obj, "Dummy", self.spec, with_default=False, with_typesafe=True
        )
        self.assertEqual(status, False)
        self.assertIsNotNone(errmsg)
        self.assertNotIn("Integer", result.keys())
        self.assertNotIn("Number", result.keys())
        self.assertNotIn("String", result.keys())
        self.assertNotIn("NullableInteger", result.keys())
        self.assertNotIn("NullableNumber", result.keys())
        self.assertNotIn("NullableString", result.keys())
        self.assertNotIn("IntegerWithDefault", result.keys())
        self.assertNotIn("NumberWithDefault", result.keys())
        self.assertNotIn("StringWithDefault", result.keys())
        self.assertNotIn("NullableIntegerWithDefault", result.keys())
        self.assertNotIn("NullableNumberWithDefault", result.keys())
        self.assertNotIn("NullableStringWithDefault", result.keys())

        obj = {
            "RequiredInteger": 1,
            "RequiredNumber": 1.5,
            "RequiredString": "required string",
            "RequiredIntegerWithDefault": 1,
            "RequiredNumberWithDefault": 1.5,
            "RequiredStringWithDefault": "required string with default",
            "RequiredNullableInteger": None,
            "RequiredNullableNumber": None,
            "RequiredNullableString": None,
            "RequiredNullableIntegerWithDefault": None,
            "RequiredNullableNumberWithDefault": None,
            "DateString": datetime.date.today().isoformat(),
            "DatetimeString": datetime.datetime.now().isoformat(),
            "DatetimeNumber": datetime.datetime.now().timestamp(),
            "DatetimeInteger": int(datetime.datetime.now().timestamp()),
            "StringPattern": "0123",
            "StringPatternWithDefault": "4567",
        }
        status, result, errmsg = Sanitizer.validate(
            obj, "Dummy", self.spec, with_default=False, with_typesafe=True
        )
        self.assertEqual(status, False)
        self.assertIsNotNone(errmsg)
        self.assertNotIn("Integer", result.keys())
        self.assertNotIn("Number", result.keys())
        self.assertNotIn("String", result.keys())
        self.assertNotIn("NullableInteger", result.keys())
        self.assertNotIn("NullableNumber", result.keys())
        self.assertNotIn("NullableString", result.keys())
        self.assertNotIn("IntegerWithDefault", result.keys())
        self.assertNotIn("NumberWithDefault", result.keys())
        self.assertNotIn("StringWithDefault", result.keys())
        self.assertNotIn("NullableIntegerWithDefault", result.keys())
        self.assertNotIn("NullableNumberWithDefault", result.keys())
        self.assertNotIn("NullableStringWithDefault", result.keys())

        obj = {
            "RequiredInteger": 1,
            "RequiredNumber": 1.5,
            "RequiredString": "required string",
            "RequiredIntegerWithDefault": 1,
            "RequiredNumberWithDefault": 1.5,
            "RequiredStringWithDefault": "required string with default",
            "RequiredNullableInteger": None,
            "RequiredNullableNumber": None,
            "RequiredNullableString": None,
            "RequiredNullableIntegerWithDefault": None,
            "RequiredNullableNumberWithDefault": None,
            "RequiredNullableStringWithDefault": None,
            "DateString": datetime.date.today(),
            "DatetimeString": datetime.datetime.now().isoformat(),
            "DatetimeNumber": datetime.datetime.now().timestamp(),
            "DatetimeInteger": int(datetime.datetime.now().timestamp()),
            "StringPattern": "0123",
            "StringPatternWithDefault": "4567",
        }
        status, result, errmsg = Sanitizer.validate(
            obj, "Dummy", self.spec, with_default=False, with_typesafe=True
        )
        self.assertEqual(status, True)
        self.assertIsNone(errmsg)
        self.assertNotIn("Integer", result.keys())
        self.assertNotIn("Number", result.keys())
        self.assertNotIn("String", result.keys())
        self.assertNotIn("NullableInteger", result.keys())
        self.assertNotIn("NullableNumber", result.keys())
        self.assertNotIn("NullableString", result.keys())
        self.assertNotIn("IntegerWithDefault", result.keys())
        self.assertNotIn("NumberWithDefault", result.keys())
        self.assertNotIn("StringWithDefault", result.keys())
        self.assertNotIn("NullableIntegerWithDefault", result.keys())
        self.assertNotIn("NullableNumberWithDefault", result.keys())
        self.assertNotIn("NullableStringWithDefault", result.keys())

        obj = {
            "RequiredInteger": 1,
            "RequiredNumber": 1.5,
            "RequiredString": "required string",
            "RequiredIntegerWithDefault": 1,
            "RequiredNumberWithDefault": 1.5,
            "RequiredStringWithDefault": "required string with default",
            "RequiredNullableInteger": None,
            "RequiredNullableNumber": None,
            "RequiredNullableString": None,
            "RequiredNullableIntegerWithDefault": None,
            "RequiredNullableNumberWithDefault": None,
            "RequiredNullableStringWithDefault": None,
            "DateString": datetime.date.today().isoformat(),
            "DatetimeString": datetime.datetime.now(),
            "DatetimeNumber": datetime.datetime.now().timestamp(),
            "DatetimeInteger": int(datetime.datetime.now().timestamp()),
            "StringPattern": "0123",
            "StringPatternWithDefault": "4567",
        }
        status, result, errmsg = Sanitizer.validate(
            obj, "Dummy", self.spec, with_default=False, with_typesafe=True
        )
        self.assertEqual(status, True)
        self.assertIsNone(errmsg)
        self.assertNotIn("Integer", result.keys())
        self.assertNotIn("Number", result.keys())
        self.assertNotIn("String", result.keys())
        self.assertNotIn("NullableInteger", result.keys())
        self.assertNotIn("NullableNumber", result.keys())
        self.assertNotIn("NullableString", result.keys())
        self.assertNotIn("IntegerWithDefault", result.keys())
        self.assertNotIn("NumberWithDefault", result.keys())
        self.assertNotIn("StringWithDefault", result.keys())
        self.assertNotIn("NullableIntegerWithDefault", result.keys())
        self.assertNotIn("NullableNumberWithDefault", result.keys())
        self.assertNotIn("NullableStringWithDefault", result.keys())

        obj = {
            "RequiredInteger": 1,
            "RequiredNumber": 1.5,
            "RequiredString": "required string",
            "RequiredIntegerWithDefault": 1,
            "RequiredNumberWithDefault": 1.5,
            "RequiredStringWithDefault": "required string with default",
            "RequiredNullableInteger": None,
            "RequiredNullableNumber": None,
            "RequiredNullableString": None,
            "RequiredNullableIntegerWithDefault": None,
            "RequiredNullableNumberWithDefault": None,
            "RequiredNullableStringWithDefault": None,
            "DateString": datetime.date.today().isoformat(),
            "DatetimeString": datetime.datetime.now().isoformat(),
            "DatetimeNumber": datetime.datetime.now(),
            "DatetimeInteger": int(datetime.datetime.now().timestamp()),
            "StringPattern": "0123",
            "StringPatternWithDefault": "4567",
        }
        status, result, errmsg = Sanitizer.validate(
            obj, "Dummy", self.spec, with_default=False, with_typesafe=True
        )
        self.assertEqual(status, True)
        self.assertIsNone(errmsg)
        self.assertNotIn("Integer", result.keys())
        self.assertNotIn("Number", result.keys())
        self.assertNotIn("String", result.keys())
        self.assertNotIn("NullableInteger", result.keys())
        self.assertNotIn("NullableNumber", result.keys())
        self.assertNotIn("NullableString", result.keys())
        self.assertNotIn("IntegerWithDefault", result.keys())
        self.assertNotIn("NumberWithDefault", result.keys())
        self.assertNotIn("StringWithDefault", result.keys())
        self.assertNotIn("NullableIntegerWithDefault", result.keys())
        self.assertNotIn("NullableNumberWithDefault", result.keys())
        self.assertNotIn("NullableStringWithDefault", result.keys())

        obj = {
            "RequiredInteger": 1,
            "RequiredNumber": 1.5,
            "RequiredString": "required string",
            "RequiredIntegerWithDefault": 1,
            "RequiredNumberWithDefault": 1.5,
            "RequiredStringWithDefault": "required string with default",
            "RequiredNullableInteger": None,
            "RequiredNullableNumber": None,
            "RequiredNullableString": None,
            "RequiredNullableIntegerWithDefault": None,
            "RequiredNullableNumberWithDefault": None,
            "RequiredNullableStringWithDefault": None,
            "DateString": datetime.date.today().isoformat(),
            "DatetimeString": datetime.datetime.now().isoformat(),
            "DatetimeNumber": datetime.datetime.now().timestamp(),
            "DatetimeInteger": datetime.datetime.now(),
            "StringPattern": "0123",
            "StringPatternWithDefault": "4567",
        }
        status, result, errmsg = Sanitizer.validate(
            obj, "Dummy", self.spec, with_default=False, with_typesafe=True
        )
        self.assertEqual(status, True)
        self.assertIsNone(errmsg)
        self.assertNotIn("Integer", result.keys())
        self.assertNotIn("Number", result.keys())
        self.assertNotIn("String", result.keys())
        self.assertNotIn("NullableInteger", result.keys())
        self.assertNotIn("NullableNumber", result.keys())
        self.assertNotIn("NullableString", result.keys())
        self.assertNotIn("IntegerWithDefault", result.keys())
        self.assertNotIn("NumberWithDefault", result.keys())
        self.assertNotIn("StringWithDefault", result.keys())
        self.assertNotIn("NullableIntegerWithDefault", result.keys())
        self.assertNotIn("NullableNumberWithDefault", result.keys())
        self.assertNotIn("NullableStringWithDefault", result.keys())

        obj = {
            "RequiredInteger": 1,
            "RequiredNumber": 1.5,
            "RequiredString": "required string",
            "RequiredIntegerWithDefault": 1,
            "RequiredNumberWithDefault": 1.5,
            "RequiredStringWithDefault": "required string with default",
            "RequiredNullableInteger": None,
            "RequiredNullableNumber": None,
            "RequiredNullableString": None,
            "RequiredNullableIntegerWithDefault": None,
            "RequiredNullableNumberWithDefault": None,
            "RequiredNullableStringWithDefault": None,
            "DateString": datetime.date.today().isoformat(),
            "DatetimeString": datetime.datetime.now().isoformat(),
            "DatetimeNumber": datetime.datetime.now().timestamp(),
            "DatetimeInteger": datetime.datetime.now().timestamp(),
            "StringPattern": "01234",
            "StringPatternWithDefault": "4567",
        }
        status, result, errmsg = Sanitizer.validate(
            obj, "Dummy", self.spec, with_default=False, with_typesafe=True
        )
        self.assertEqual(status, False)
        self.assertIsNotNone(errmsg)
        self.assertNotIn("Integer", result.keys())
        self.assertNotIn("Number", result.keys())
        self.assertNotIn("String", result.keys())
        self.assertNotIn("NullableInteger", result.keys())
        self.assertNotIn("NullableNumber", result.keys())
        self.assertNotIn("NullableString", result.keys())
        self.assertNotIn("IntegerWithDefault", result.keys())
        self.assertNotIn("NumberWithDefault", result.keys())
        self.assertNotIn("StringWithDefault", result.keys())
        self.assertNotIn("NullableIntegerWithDefault", result.keys())
        self.assertNotIn("NullableNumberWithDefault", result.keys())
        self.assertNotIn("NullableStringWithDefault", result.keys())

        obj = {
            "RequiredInteger": 1,
            "RequiredNumber": 1.5,
            "RequiredString": "required string",
            "RequiredIntegerWithDefault": 1,
            "RequiredNumberWithDefault": 1.5,
            "RequiredStringWithDefault": "required string with default",
            "RequiredNullableInteger": None,
            "RequiredNullableNumber": None,
            "RequiredNullableString": None,
            "RequiredNullableIntegerWithDefault": None,
            "RequiredNullableNumberWithDefault": None,
            "RequiredNullableStringWithDefault": None,
            "DateString": datetime.date.today().isoformat(),
            "DatetimeString": datetime.datetime.now().isoformat(),
            "DatetimeNumber": datetime.datetime.now().timestamp(),
            "DatetimeInteger": datetime.datetime.now().timestamp(),
            "StringPattern": "0123",
            "StringPatternWithDefault": "45678",
        }
        status, result, errmsg = Sanitizer.validate(
            obj, "Dummy", self.spec, with_default=False, with_typesafe=True
        )
        self.assertEqual(status, True)
        self.assertIsNone(errmsg)
        self.assertNotIn("Integer", result.keys())
        self.assertNotIn("Number", result.keys())
        self.assertNotIn("String", result.keys())
        self.assertNotIn("NullableInteger", result.keys())
        self.assertNotIn("NullableNumber", result.keys())
        self.assertNotIn("NullableString", result.keys())
        self.assertNotIn("IntegerWithDefault", result.keys())
        self.assertNotIn("NumberWithDefault", result.keys())
        self.assertNotIn("StringWithDefault", result.keys())
        self.assertNotIn("NullableIntegerWithDefault", result.keys())
        self.assertNotIn("NullableNumberWithDefault", result.keys())
        self.assertNotIn("NullableStringWithDefault", result.keys())

    def test_004_validate_with_default_and_typesafe(self):
        obj = {
            "RequiredInteger": 1,
            "RequiredNumber": 1.5,
            "RequiredString": "required string",
            "RequiredIntegerWithDefault": 1,
            "RequiredNumberWithDefault": 1.5,
            "RequiredStringWithDefault": "required string with default",
            "RequiredNullableInteger": None,
            "RequiredNullableNumber": None,
            "RequiredNullableString": None,
            "RequiredNullableIntegerWithDefault": None,
            "RequiredNullableNumberWithDefault": None,
            "RequiredNullableStringWithDefault": None,
            "DateString": datetime.date.today().isoformat(),
            "DatetimeString": datetime.datetime.now().isoformat(),
            "DatetimeNumber": datetime.datetime.now().timestamp(),
            "DatetimeInteger": int(datetime.datetime.now().timestamp()),
            "StringPattern": "0123",
            "StringPatternWithDefault": "4567",
        }
        status, result, errmsg = Sanitizer.validate(
            obj, "Dummy", self.spec, with_default=True, with_typesafe=True
        )
        self.assertEqual(status, True)
        self.assertIsNone(errmsg)
        self.assertNotIn("Integer", result.keys())
        self.assertNotIn("Number", result.keys())
        self.assertNotIn("String", result.keys())
        self.assertNotIn("NullableInteger", result.keys())
        self.assertNotIn("NullableNumber", result.keys())
        self.assertNotIn("NullableString", result.keys())
        self.assertIn("IntegerWithDefault", result.keys())
        self.assertIn("NumberWithDefault", result.keys())
        self.assertIn("StringWithDefault", result.keys())
        self.assertIn("NullableIntegerWithDefault", result.keys())
        self.assertIn("NullableNumberWithDefault", result.keys())
        self.assertIn("NullableStringWithDefault", result.keys())

        obj = {
            "RequiredInteger": "1",
            "RequiredNumber": 1.5,
            "RequiredString": "required string",
            "RequiredIntegerWithDefault": 1,
            "RequiredNumberWithDefault": 1.5,
            "RequiredStringWithDefault": "required string with default",
            "RequiredNullableInteger": None,
            "RequiredNullableNumber": None,
            "RequiredNullableString": None,
            "RequiredNullableIntegerWithDefault": None,
            "RequiredNullableNumberWithDefault": None,
            "RequiredNullableStringWithDefault": None,
            "DateString": datetime.date.today().isoformat(),
            "DatetimeString": datetime.datetime.now().isoformat(),
            "DatetimeNumber": datetime.datetime.now().timestamp(),
            "DatetimeInteger": int(datetime.datetime.now().timestamp()),
            "StringPattern": "0123",
            "StringPatternWithDefault": "4567",
        }
        status, result, errmsg = Sanitizer.validate(
            obj, "Dummy", self.spec, with_default=True, with_typesafe=True
        )
        self.assertEqual(status, True)
        self.assertIsNone(errmsg)
        self.assertNotIn("Integer", result.keys())
        self.assertNotIn("Number", result.keys())
        self.assertNotIn("String", result.keys())
        self.assertNotIn("NullableInteger", result.keys())
        self.assertNotIn("NullableNumber", result.keys())
        self.assertNotIn("NullableString", result.keys())
        self.assertIn("IntegerWithDefault", result.keys())
        self.assertIn("NumberWithDefault", result.keys())
        self.assertIn("StringWithDefault", result.keys())
        self.assertIn("NullableIntegerWithDefault", result.keys())
        self.assertIn("NullableNumberWithDefault", result.keys())
        self.assertIn("NullableStringWithDefault", result.keys())

        obj = {
            "RequiredInteger": 1,
            "RequiredNumber": "1.5",
            "RequiredString": "required string",
            "RequiredIntegerWithDefault": 1,
            "RequiredNumberWithDefault": 1.5,
            "RequiredStringWithDefault": "required string with default",
            "RequiredNullableInteger": None,
            "RequiredNullableNumber": None,
            "RequiredNullableString": None,
            "RequiredNullableIntegerWithDefault": None,
            "RequiredNullableNumberWithDefault": None,
            "RequiredNullableStringWithDefault": None,
            "DateString": datetime.date.today().isoformat(),
            "DatetimeString": datetime.datetime.now().isoformat(),
            "DatetimeNumber": datetime.datetime.now().timestamp(),
            "DatetimeInteger": int(datetime.datetime.now().timestamp()),
            "StringPattern": "0123",
            "StringPatternWithDefault": "4567",
        }
        status, result, errmsg = Sanitizer.validate(
            obj, "Dummy", self.spec, with_default=True, with_typesafe=True
        )
        self.assertEqual(status, True)
        self.assertIsNone(errmsg)
        self.assertNotIn("Integer", result.keys())
        self.assertNotIn("Number", result.keys())
        self.assertNotIn("String", result.keys())
        self.assertNotIn("NullableInteger", result.keys())
        self.assertNotIn("NullableNumber", result.keys())
        self.assertNotIn("NullableString", result.keys())
        self.assertIn("IntegerWithDefault", result.keys())
        self.assertIn("NumberWithDefault", result.keys())
        self.assertIn("StringWithDefault", result.keys())
        self.assertIn("NullableIntegerWithDefault", result.keys())
        self.assertIn("NullableNumberWithDefault", result.keys())
        self.assertIn("NullableStringWithDefault", result.keys())

        obj = {
            "RequiredInteger": 1,
            "RequiredNumber": 1.5,
            "RequiredString": 12345,
            "RequiredIntegerWithDefault": 1,
            "RequiredNumberWithDefault": 1.5,
            "RequiredStringWithDefault": "required string with default",
            "RequiredNullableInteger": None,
            "RequiredNullableNumber": None,
            "RequiredNullableString": None,
            "RequiredNullableIntegerWithDefault": None,
            "RequiredNullableNumberWithDefault": None,
            "RequiredNullableStringWithDefault": None,
            "DateString": datetime.date.today().isoformat(),
            "DatetimeString": datetime.datetime.now().isoformat(),
            "DatetimeNumber": datetime.datetime.now().timestamp(),
            "DatetimeInteger": int(datetime.datetime.now().timestamp()),
            "StringPattern": "0123",
            "StringPatternWithDefault": "4567",
        }
        status, result, errmsg = Sanitizer.validate(
            obj, "Dummy", self.spec, with_default=True, with_typesafe=True
        )
        self.assertEqual(status, True)
        self.assertIsNone(errmsg)
        self.assertNotIn("Integer", result.keys())
        self.assertNotIn("Number", result.keys())
        self.assertNotIn("String", result.keys())
        self.assertNotIn("NullableInteger", result.keys())
        self.assertNotIn("NullableNumber", result.keys())
        self.assertNotIn("NullableString", result.keys())
        self.assertIn("IntegerWithDefault", result.keys())
        self.assertIn("NumberWithDefault", result.keys())
        self.assertIn("StringWithDefault", result.keys())
        self.assertIn("NullableIntegerWithDefault", result.keys())
        self.assertIn("NullableNumberWithDefault", result.keys())
        self.assertIn("NullableStringWithDefault", result.keys())

        obj = {
            "RequiredInteger": 1,
            "RequiredNumber": 1.5,
            "RequiredString": "required string",
            "RequiredIntegerWithDefault": 1.5,
            "RequiredNumberWithDefault": 1.5,
            "RequiredStringWithDefault": "required string with default",
            "RequiredNullableInteger": None,
            "RequiredNullableNumber": None,
            "RequiredNullableString": None,
            "RequiredNullableIntegerWithDefault": None,
            "RequiredNullableNumberWithDefault": None,
            "RequiredNullableStringWithDefault": None,
            "DateString": datetime.date.today().isoformat(),
            "DatetimeString": datetime.datetime.now().isoformat(),
            "DatetimeNumber": datetime.datetime.now().timestamp(),
            "DatetimeInteger": int(datetime.datetime.now().timestamp()),
            "StringPattern": "0123",
            "StringPatternWithDefault": "4567",
        }
        status, result, errmsg = Sanitizer.validate(
            obj, "Dummy", self.spec, with_default=True, with_typesafe=True
        )
        self.assertEqual(status, True)
        self.assertIsNone(errmsg)
        self.assertNotIn("Integer", result.keys())
        self.assertNotIn("Number", result.keys())
        self.assertNotIn("String", result.keys())
        self.assertNotIn("NullableInteger", result.keys())
        self.assertNotIn("NullableNumber", result.keys())
        self.assertNotIn("NullableString", result.keys())
        self.assertIn("IntegerWithDefault", result.keys())
        self.assertIn("NumberWithDefault", result.keys())
        self.assertIn("StringWithDefault", result.keys())
        self.assertIn("NullableIntegerWithDefault", result.keys())
        self.assertIn("NullableNumberWithDefault", result.keys())
        self.assertIn("NullableStringWithDefault", result.keys())

        obj = {
            "RequiredInteger": 1,
            "RequiredNumber": 1.5,
            "RequiredString": "required string",
            "RequiredIntegerWithDefault": 1,
            "RequiredNumberWithDefault": "1.5",
            "RequiredStringWithDefault": "required string with default",
            "RequiredNullableInteger": None,
            "RequiredNullableNumber": None,
            "RequiredNullableString": None,
            "RequiredNullableIntegerWithDefault": None,
            "RequiredNullableNumberWithDefault": None,
            "RequiredNullableStringWithDefault": None,
            "DateString": datetime.date.today().isoformat(),
            "DatetimeString": datetime.datetime.now().isoformat(),
            "DatetimeNumber": datetime.datetime.now().timestamp(),
            "DatetimeInteger": int(datetime.datetime.now().timestamp()),
            "StringPattern": "0123",
            "StringPatternWithDefault": "4567",
        }
        status, result, errmsg = Sanitizer.validate(
            obj, "Dummy", self.spec, with_default=True, with_typesafe=True
        )
        self.assertEqual(status, True)
        self.assertIsNone(errmsg)
        self.assertNotIn("Integer", result.keys())
        self.assertNotIn("Number", result.keys())
        self.assertNotIn("String", result.keys())
        self.assertNotIn("NullableInteger", result.keys())
        self.assertNotIn("NullableNumber", result.keys())
        self.assertNotIn("NullableString", result.keys())
        self.assertIn("IntegerWithDefault", result.keys())
        self.assertIn("NumberWithDefault", result.keys())
        self.assertIn("StringWithDefault", result.keys())
        self.assertIn("NullableIntegerWithDefault", result.keys())
        self.assertIn("NullableNumberWithDefault", result.keys())
        self.assertIn("NullableStringWithDefault", result.keys())

        obj = {
            "RequiredInteger": 1,
            "RequiredNumber": 1.5,
            "RequiredString": "required string",
            "RequiredIntegerWithDefault": 1,
            "RequiredNumberWithDefault": 1.5,
            "RequiredStringWithDefault": 12345,
            "RequiredNullableInteger": None,
            "RequiredNullableNumber": None,
            "RequiredNullableString": None,
            "RequiredNullableIntegerWithDefault": None,
            "RequiredNullableNumberWithDefault": None,
            "RequiredNullableStringWithDefault": None,
            "DateString": datetime.date.today().isoformat(),
            "DatetimeString": datetime.datetime.now().isoformat(),
            "DatetimeNumber": datetime.datetime.now().timestamp(),
            "DatetimeInteger": int(datetime.datetime.now().timestamp()),
            "StringPattern": "0123",
            "StringPatternWithDefault": "4567",
        }
        status, result, errmsg = Sanitizer.validate(
            obj, "Dummy", self.spec, with_default=True, with_typesafe=True
        )
        self.assertEqual(status, True)
        self.assertIsNone(errmsg)
        self.assertNotIn("Integer", result.keys())
        self.assertNotIn("Number", result.keys())
        self.assertNotIn("String", result.keys())
        self.assertNotIn("NullableInteger", result.keys())
        self.assertNotIn("NullableNumber", result.keys())
        self.assertNotIn("NullableString", result.keys())
        self.assertIn("IntegerWithDefault", result.keys())
        self.assertIn("NumberWithDefault", result.keys())
        self.assertIn("StringWithDefault", result.keys())
        self.assertIn("NullableIntegerWithDefault", result.keys())
        self.assertIn("NullableNumberWithDefault", result.keys())
        self.assertIn("NullableStringWithDefault", result.keys())

        obj = {
            "RequiredInteger": 1,
            "RequiredNumber": 1.5,
            "RequiredString": "required string",
            "RequiredIntegerWithDefault": 1,
            "RequiredNumberWithDefault": 1.5,
            "RequiredStringWithDefault": "required string with default",
            "RequiredNullableNumber": None,
            "RequiredNullableString": None,
            "RequiredNullableIntegerWithDefault": None,
            "RequiredNullableNumberWithDefault": None,
            "RequiredNullableStringWithDefault": None,
            "DateString": datetime.date.today().isoformat(),
            "DatetimeString": datetime.datetime.now().isoformat(),
            "DatetimeNumber": datetime.datetime.now().timestamp(),
            "DatetimeInteger": int(datetime.datetime.now().timestamp()),
            "StringPattern": "0123",
            "StringPatternWithDefault": "4567",
        }
        status, result, errmsg = Sanitizer.validate(
            obj, "Dummy", self.spec, with_default=True, with_typesafe=True
        )
        self.assertEqual(status, False)
        self.assertIsNotNone(errmsg)
        self.assertNotIn("Integer", result.keys())
        self.assertNotIn("Number", result.keys())
        self.assertNotIn("String", result.keys())
        self.assertNotIn("NullableInteger", result.keys())
        self.assertNotIn("NullableNumber", result.keys())
        self.assertNotIn("NullableString", result.keys())
        self.assertIn("IntegerWithDefault", result.keys())
        self.assertIn("NumberWithDefault", result.keys())
        self.assertIn("StringWithDefault", result.keys())
        self.assertIn("NullableIntegerWithDefault", result.keys())
        self.assertIn("NullableNumberWithDefault", result.keys())
        self.assertIn("NullableStringWithDefault", result.keys())

        obj = {
            "RequiredInteger": 1,
            "RequiredNumber": 1.5,
            "RequiredString": "required string",
            "RequiredIntegerWithDefault": 1,
            "RequiredNumberWithDefault": 1.5,
            "RequiredStringWithDefault": "required string with default",
            "RequiredNullableInteger": None,
            "RequiredNullableString": None,
            "RequiredNullableIntegerWithDefault": None,
            "RequiredNullableNumberWithDefault": None,
            "RequiredNullableStringWithDefault": None,
            "DateString": datetime.date.today().isoformat(),
            "DatetimeString": datetime.datetime.now().isoformat(),
            "DatetimeNumber": datetime.datetime.now().timestamp(),
            "DatetimeInteger": int(datetime.datetime.now().timestamp()),
            "StringPattern": "0123",
            "StringPatternWithDefault": "4567",
        }
        status, result, errmsg = Sanitizer.validate(
            obj, "Dummy", self.spec, with_default=True, with_typesafe=True
        )
        self.assertEqual(status, False)
        self.assertIsNotNone(errmsg)
        self.assertNotIn("Integer", result.keys())
        self.assertNotIn("Number", result.keys())
        self.assertNotIn("String", result.keys())
        self.assertNotIn("NullableInteger", result.keys())
        self.assertNotIn("NullableNumber", result.keys())
        self.assertNotIn("NullableString", result.keys())
        self.assertIn("IntegerWithDefault", result.keys())
        self.assertIn("NumberWithDefault", result.keys())
        self.assertIn("StringWithDefault", result.keys())
        self.assertIn("NullableIntegerWithDefault", result.keys())
        self.assertIn("NullableNumberWithDefault", result.keys())
        self.assertIn("NullableStringWithDefault", result.keys())

        obj = {
            "RequiredInteger": 1,
            "RequiredNumber": 1.5,
            "RequiredString": "required string",
            "RequiredIntegerWithDefault": 1,
            "RequiredNumberWithDefault": 1.5,
            "RequiredStringWithDefault": "required string with default",
            "RequiredNullableInteger": None,
            "RequiredNullableNumber": None,
            "RequiredNullableIntegerWithDefault": None,
            "RequiredNullableNumberWithDefault": None,
            "RequiredNullableStringWithDefault": None,
            "DateString": datetime.date.today().isoformat(),
            "DatetimeString": datetime.datetime.now().isoformat(),
            "DatetimeNumber": datetime.datetime.now().timestamp(),
            "DatetimeInteger": int(datetime.datetime.now().timestamp()),
            "StringPattern": "0123",
            "StringPatternWithDefault": "4567",
        }
        status, result, errmsg = Sanitizer.validate(
            obj, "Dummy", self.spec, with_default=True, with_typesafe=True
        )
        self.assertEqual(status, False)
        self.assertIsNotNone(errmsg)
        self.assertNotIn("Integer", result.keys())
        self.assertNotIn("Number", result.keys())
        self.assertNotIn("String", result.keys())
        self.assertNotIn("NullableInteger", result.keys())
        self.assertNotIn("NullableNumber", result.keys())
        self.assertNotIn("NullableString", result.keys())
        self.assertIn("IntegerWithDefault", result.keys())
        self.assertIn("NumberWithDefault", result.keys())
        self.assertIn("StringWithDefault", result.keys())
        self.assertIn("NullableIntegerWithDefault", result.keys())
        self.assertIn("NullableNumberWithDefault", result.keys())
        self.assertIn("NullableStringWithDefault", result.keys())

        obj = {
            "RequiredInteger": 1,
            "RequiredNumber": 1.5,
            "RequiredString": "required string",
            "RequiredIntegerWithDefault": 1,
            "RequiredNumberWithDefault": 1.5,
            "RequiredStringWithDefault": "required string with default",
            "RequiredNullableInteger": None,
            "RequiredNullableNumber": None,
            "RequiredNullableString": None,
            "RequiredNullableNumberWithDefault": None,
            "RequiredNullableStringWithDefault": None,
            "DateString": datetime.date.today().isoformat(),
            "DatetimeString": datetime.datetime.now().isoformat(),
            "DatetimeNumber": datetime.datetime.now().timestamp(),
            "DatetimeInteger": int(datetime.datetime.now().timestamp()),
            "StringPattern": "0123",
            "StringPatternWithDefault": "4567",
        }
        status, result, errmsg = Sanitizer.validate(
            obj, "Dummy", self.spec, with_default=True, with_typesafe=True
        )
        self.assertEqual(status, False)
        self.assertIsNotNone(errmsg)
        self.assertNotIn("Integer", result.keys())
        self.assertNotIn("Number", result.keys())
        self.assertNotIn("String", result.keys())
        self.assertNotIn("NullableInteger", result.keys())
        self.assertNotIn("NullableNumber", result.keys())
        self.assertNotIn("NullableString", result.keys())
        self.assertIn("IntegerWithDefault", result.keys())
        self.assertIn("NumberWithDefault", result.keys())
        self.assertIn("StringWithDefault", result.keys())
        self.assertIn("NullableIntegerWithDefault", result.keys())
        self.assertIn("NullableNumberWithDefault", result.keys())
        self.assertIn("NullableStringWithDefault", result.keys())

        obj = {
            "RequiredInteger": 1,
            "RequiredNumber": 1.5,
            "RequiredString": "required string",
            "RequiredIntegerWithDefault": 1,
            "RequiredNumberWithDefault": 1.5,
            "RequiredStringWithDefault": "required string with default",
            "RequiredNullableInteger": None,
            "RequiredNullableNumber": None,
            "RequiredNullableString": None,
            "RequiredNullableIntegerWithDefault": None,
            "RequiredNullableStringWithDefault": None,
            "DateString": datetime.date.today().isoformat(),
            "DatetimeString": datetime.datetime.now().isoformat(),
            "DatetimeNumber": datetime.datetime.now().timestamp(),
            "DatetimeInteger": int(datetime.datetime.now().timestamp()),
            "StringPattern": "0123",
            "StringPatternWithDefault": "4567",
        }
        status, result, errmsg = Sanitizer.validate(
            obj, "Dummy", self.spec, with_default=True, with_typesafe=True
        )
        self.assertEqual(status, False)
        self.assertIsNotNone(errmsg)
        self.assertNotIn("Integer", result.keys())
        self.assertNotIn("Number", result.keys())
        self.assertNotIn("String", result.keys())
        self.assertNotIn("NullableInteger", result.keys())
        self.assertNotIn("NullableNumber", result.keys())
        self.assertNotIn("NullableString", result.keys())
        self.assertIn("IntegerWithDefault", result.keys())
        self.assertIn("NumberWithDefault", result.keys())
        self.assertIn("StringWithDefault", result.keys())
        self.assertIn("NullableIntegerWithDefault", result.keys())
        self.assertIn("NullableNumberWithDefault", result.keys())
        self.assertIn("NullableStringWithDefault", result.keys())

        obj = {
            "RequiredInteger": 1,
            "RequiredNumber": 1.5,
            "RequiredString": "required string",
            "RequiredIntegerWithDefault": 1,
            "RequiredNumberWithDefault": 1.5,
            "RequiredStringWithDefault": "required string with default",
            "RequiredNullableInteger": None,
            "RequiredNullableNumber": None,
            "RequiredNullableString": None,
            "RequiredNullableIntegerWithDefault": None,
            "RequiredNullableNumberWithDefault": None,
            "DateString": datetime.date.today().isoformat(),
            "DatetimeString": datetime.datetime.now().isoformat(),
            "DatetimeNumber": datetime.datetime.now().timestamp(),
            "DatetimeInteger": int(datetime.datetime.now().timestamp()),
            "StringPattern": "0123",
            "StringPatternWithDefault": "4567",
        }
        status, result, errmsg = Sanitizer.validate(
            obj, "Dummy", self.spec, with_default=True, with_typesafe=True
        )
        self.assertEqual(status, False)
        self.assertIsNotNone(errmsg)
        self.assertNotIn("Integer", result.keys())
        self.assertNotIn("Number", result.keys())
        self.assertNotIn("String", result.keys())
        self.assertNotIn("NullableInteger", result.keys())
        self.assertNotIn("NullableNumber", result.keys())
        self.assertNotIn("NullableString", result.keys())
        self.assertIn("IntegerWithDefault", result.keys())
        self.assertIn("NumberWithDefault", result.keys())
        self.assertIn("StringWithDefault", result.keys())
        self.assertIn("NullableIntegerWithDefault", result.keys())
        self.assertIn("NullableNumberWithDefault", result.keys())
        self.assertIn("NullableStringWithDefault", result.keys())

        obj = {
            "RequiredInteger": 1,
            "RequiredNumber": 1.5,
            "RequiredString": "required string",
            "RequiredIntegerWithDefault": 1,
            "RequiredNumberWithDefault": 1.5,
            "RequiredStringWithDefault": "required string with default",
            "RequiredNullableInteger": None,
            "RequiredNullableNumber": None,
            "RequiredNullableString": None,
            "RequiredNullableIntegerWithDefault": None,
            "RequiredNullableNumberWithDefault": None,
            "RequiredNullableStringWithDefault": None,
            "DateString": datetime.date.today(),
            "DatetimeString": datetime.datetime.now().isoformat(),
            "DatetimeNumber": datetime.datetime.now().timestamp(),
            "DatetimeInteger": int(datetime.datetime.now().timestamp()),
            "StringPattern": "0123",
            "StringPatternWithDefault": "4567",
        }
        status, result, errmsg = Sanitizer.validate(
            obj, "Dummy", self.spec, with_default=True, with_typesafe=True
        )
        self.assertEqual(status, True)
        self.assertIsNone(errmsg)
        self.assertNotIn("Integer", result.keys())
        self.assertNotIn("Number", result.keys())
        self.assertNotIn("String", result.keys())
        self.assertNotIn("NullableInteger", result.keys())
        self.assertNotIn("NullableNumber", result.keys())
        self.assertNotIn("NullableString", result.keys())
        self.assertIn("IntegerWithDefault", result.keys())
        self.assertIn("NumberWithDefault", result.keys())
        self.assertIn("StringWithDefault", result.keys())
        self.assertIn("NullableIntegerWithDefault", result.keys())
        self.assertIn("NullableNumberWithDefault", result.keys())
        self.assertIn("NullableStringWithDefault", result.keys())

        obj = {
            "RequiredInteger": 1,
            "RequiredNumber": 1.5,
            "RequiredString": "required string",
            "RequiredIntegerWithDefault": 1,
            "RequiredNumberWithDefault": 1.5,
            "RequiredStringWithDefault": "required string with default",
            "RequiredNullableInteger": None,
            "RequiredNullableNumber": None,
            "RequiredNullableString": None,
            "RequiredNullableIntegerWithDefault": None,
            "RequiredNullableNumberWithDefault": None,
            "RequiredNullableStringWithDefault": None,
            "DateString": datetime.date.today().isoformat(),
            "DatetimeString": datetime.datetime.now(),
            "DatetimeNumber": datetime.datetime.now().timestamp(),
            "DatetimeInteger": int(datetime.datetime.now().timestamp()),
            "StringPattern": "0123",
            "StringPatternWithDefault": "4567",
        }
        status, result, errmsg = Sanitizer.validate(
            obj, "Dummy", self.spec, with_default=True, with_typesafe=True
        )
        self.assertEqual(status, True)
        self.assertIsNone(errmsg)
        self.assertNotIn("Integer", result.keys())
        self.assertNotIn("Number", result.keys())
        self.assertNotIn("String", result.keys())
        self.assertNotIn("NullableInteger", result.keys())
        self.assertNotIn("NullableNumber", result.keys())
        self.assertNotIn("NullableString", result.keys())
        self.assertIn("IntegerWithDefault", result.keys())
        self.assertIn("NumberWithDefault", result.keys())
        self.assertIn("StringWithDefault", result.keys())
        self.assertIn("NullableIntegerWithDefault", result.keys())
        self.assertIn("NullableNumberWithDefault", result.keys())
        self.assertIn("NullableStringWithDefault", result.keys())

        obj = {
            "RequiredInteger": 1,
            "RequiredNumber": 1.5,
            "RequiredString": "required string",
            "RequiredIntegerWithDefault": 1,
            "RequiredNumberWithDefault": 1.5,
            "RequiredStringWithDefault": "required string with default",
            "RequiredNullableInteger": None,
            "RequiredNullableNumber": None,
            "RequiredNullableString": None,
            "RequiredNullableIntegerWithDefault": None,
            "RequiredNullableNumberWithDefault": None,
            "RequiredNullableStringWithDefault": None,
            "DateString": datetime.date.today().isoformat(),
            "DatetimeString": datetime.datetime.now().isoformat(),
            "DatetimeNumber": datetime.datetime.now(),
            "DatetimeInteger": int(datetime.datetime.now().timestamp()),
            "StringPattern": "0123",
            "StringPatternWithDefault": "4567",
        }
        status, result, errmsg = Sanitizer.validate(
            obj, "Dummy", self.spec, with_default=True, with_typesafe=True
        )
        self.assertEqual(status, True)
        self.assertIsNone(errmsg)
        self.assertNotIn("Integer", result.keys())
        self.assertNotIn("Number", result.keys())
        self.assertNotIn("String", result.keys())
        self.assertNotIn("NullableInteger", result.keys())
        self.assertNotIn("NullableNumber", result.keys())
        self.assertNotIn("NullableString", result.keys())
        self.assertIn("IntegerWithDefault", result.keys())
        self.assertIn("NumberWithDefault", result.keys())
        self.assertIn("StringWithDefault", result.keys())
        self.assertIn("NullableIntegerWithDefault", result.keys())
        self.assertIn("NullableNumberWithDefault", result.keys())
        self.assertIn("NullableStringWithDefault", result.keys())

        obj = {
            "RequiredInteger": 1,
            "RequiredNumber": 1.5,
            "RequiredString": "required string",
            "RequiredIntegerWithDefault": 1,
            "RequiredNumberWithDefault": 1.5,
            "RequiredStringWithDefault": "required string with default",
            "RequiredNullableInteger": None,
            "RequiredNullableNumber": None,
            "RequiredNullableString": None,
            "RequiredNullableIntegerWithDefault": None,
            "RequiredNullableNumberWithDefault": None,
            "RequiredNullableStringWithDefault": None,
            "DateString": datetime.date.today().isoformat(),
            "DatetimeString": datetime.datetime.now().isoformat(),
            "DatetimeNumber": datetime.datetime.now().timestamp(),
            "DatetimeInteger": datetime.datetime.now(),
            "StringPattern": "0123",
            "StringPatternWithDefault": "4567",
        }
        status, result, errmsg = Sanitizer.validate(
            obj, "Dummy", self.spec, with_default=True, with_typesafe=True
        )
        self.assertEqual(status, True)
        self.assertIsNone(errmsg)
        self.assertNotIn("Integer", result.keys())
        self.assertNotIn("Number", result.keys())
        self.assertNotIn("String", result.keys())
        self.assertNotIn("NullableInteger", result.keys())
        self.assertNotIn("NullableNumber", result.keys())
        self.assertNotIn("NullableString", result.keys())
        self.assertIn("IntegerWithDefault", result.keys())
        self.assertIn("NumberWithDefault", result.keys())
        self.assertIn("StringWithDefault", result.keys())
        self.assertIn("NullableIntegerWithDefault", result.keys())
        self.assertIn("NullableNumberWithDefault", result.keys())
        self.assertIn("NullableStringWithDefault", result.keys())

        obj = {
            "RequiredInteger": 1,
            "RequiredNumber": 1.5,
            "RequiredString": "required string",
            "RequiredIntegerWithDefault": 1,
            "RequiredNumberWithDefault": 1.5,
            "RequiredStringWithDefault": "required string with default",
            "RequiredNullableInteger": None,
            "RequiredNullableNumber": None,
            "RequiredNullableString": None,
            "RequiredNullableIntegerWithDefault": None,
            "RequiredNullableNumberWithDefault": None,
            "RequiredNullableStringWithDefault": None,
            "DateString": datetime.date.today().isoformat(),
            "DatetimeString": datetime.datetime.now().isoformat(),
            "DatetimeNumber": datetime.datetime.now().timestamp(),
            "DatetimeInteger": datetime.datetime.now().timestamp(),
            "StringPattern": "01234",
            "StringPatternWithDefault": "4567",
        }
        status, result, errmsg = Sanitizer.validate(
            obj, "Dummy", self.spec, with_default=True, with_typesafe=True
        )
        self.assertEqual(status, False)
        self.assertIsNotNone(errmsg)
        self.assertNotIn("Integer", result.keys())
        self.assertNotIn("Number", result.keys())
        self.assertNotIn("String", result.keys())
        self.assertNotIn("NullableInteger", result.keys())
        self.assertNotIn("NullableNumber", result.keys())
        self.assertNotIn("NullableString", result.keys())
        self.assertIn("IntegerWithDefault", result.keys())
        self.assertIn("NumberWithDefault", result.keys())
        self.assertIn("StringWithDefault", result.keys())
        self.assertIn("NullableIntegerWithDefault", result.keys())
        self.assertIn("NullableNumberWithDefault", result.keys())
        self.assertIn("NullableStringWithDefault", result.keys())

        obj = {
            "RequiredInteger": 1,
            "RequiredNumber": 1.5,
            "RequiredString": "required string",
            "RequiredIntegerWithDefault": 1,
            "RequiredNumberWithDefault": 1.5,
            "RequiredStringWithDefault": "required string with default",
            "RequiredNullableInteger": None,
            "RequiredNullableNumber": None,
            "RequiredNullableString": None,
            "RequiredNullableIntegerWithDefault": None,
            "RequiredNullableNumberWithDefault": None,
            "RequiredNullableStringWithDefault": None,
            "DateString": datetime.date.today().isoformat(),
            "DatetimeString": datetime.datetime.now().isoformat(),
            "DatetimeNumber": datetime.datetime.now().timestamp(),
            "DatetimeInteger": datetime.datetime.now().timestamp(),
            "StringPattern": "0123",
            "StringPatternWithDefault": "45678",
        }
        status, result, errmsg = Sanitizer.validate(
            obj, "Dummy", self.spec, with_default=True, with_typesafe=True
        )
        self.assertEqual(status, True)
        self.assertIsNone(errmsg)
        self.assertNotIn("Integer", result.keys())
        self.assertNotIn("Number", result.keys())
        self.assertNotIn("String", result.keys())
        self.assertNotIn("NullableInteger", result.keys())
        self.assertNotIn("NullableNumber", result.keys())
        self.assertNotIn("NullableString", result.keys())
        self.assertIn("IntegerWithDefault", result.keys())
        self.assertIn("NumberWithDefault", result.keys())
        self.assertIn("StringWithDefault", result.keys())
        self.assertIn("NullableIntegerWithDefault", result.keys())
        self.assertIn("NullableNumberWithDefault", result.keys())
        self.assertIn("NullableStringWithDefault", result.keys())
