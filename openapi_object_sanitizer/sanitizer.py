from typing import Tuple, Any
from openapi_core.spec import Spec
from .validator import Validator


class Sanitizer(Validator):
    @classmethod
    def sanitize(
        cls, obj: Any, schema_name: str, spec: Spec | dict
    ) -> Tuple[bool, Any, str]:
        return cls.validate(
            obj, schema_name, spec, with_default=True, with_typesafe=True
        )
