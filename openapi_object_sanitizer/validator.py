import datetime
import copy
import re
from typing import Tuple, Any
from openapi_core.spec import Spec
from openapi_schema_validator import validate as _validate
from openapi_schema_validator import OAS30Validator
from jsonschema import validators


class Validator:
    @classmethod
    def extend_with_default(cls, validator_class):
        validate_properties = validator_class.VALIDATORS["properties"]

        def set_defaults(validator, properties, instance, schema):
            for property, subschema in properties.items():
                if "default" in subschema:
                    instance.setdefault(property, subschema["default"])
                    if (
                        ("nullable" in subschema and not subschema["nullable"])
                        or ("nullable" not in subschema)
                    ) and instance.get(property) is None:
                        instance[property] = subschema["default"]

            for error in validate_properties(
                validator,
                properties,
                instance,
                schema,
            ):
                yield error

        return validators.extend(
            validator_class,
            {"properties": set_defaults},
        )

    @classmethod
    def extend_with_typesafe(cls, validator_class):
        validate_properties = validator_class.VALIDATORS["properties"]

        def typesafe(validator, properties, instance, schema):
            for property, subschema in properties.items():
                if property in instance and "type" in subschema:
                    if type(instance[property]) is str:
                        if subschema["type"] == "integer":
                            instance[property] = int(float(instance[property]))
                        elif subschema["type"] == "number":
                            instance[property] = float(instance[property])
                        elif subschema["type"] == "string":
                            if subschema.get("pattern"):
                                match = re.match(
                                    subschema["pattern"], instance[property]
                                )
                                if not match:
                                    if subschema.get("default"):
                                        instance[property] = subschema["default"]
                                    else:
                                        instance[property] = ""
                    elif type(instance[property]) is float:
                        if subschema["type"] == "integer":
                            instance[property] = int(instance[property])
                        elif subschema["type"] == "string":
                            instance[property] = str(instance[property])
                    elif type(instance[property]) is int:
                        if subschema["type"] == "number":
                            instance[property] = float(instance[property])
                        elif subschema["type"] == "string":
                            instance[property] = str(instance[property])
                    elif isinstance(instance[property], datetime.datetime):
                        if subschema["type"] == "string":
                            instance[property] = instance[property].isoformat()
                        elif subschema["type"] == "number":
                            instance[property] = instance[property].timestamp()
                        elif subschema["type"] == "integer":
                            instance[property] = int(instance[property].timestamp())
                    elif isinstance(instance[property], datetime.date):
                        if subschema["type"] == "string":
                            instance[property] = instance[property].isoformat()

            for error in validate_properties(
                validator,
                properties,
                instance,
                schema,
            ):
                yield error

        return validators.extend(
            validator_class,
            {"properties": typesafe},
        )

    @classmethod
    def read_spec_file(cls, filepath) -> Spec:
        return Spec.from_file_path(filepath)

    @classmethod
    def validate(
        cls,
        obj: Any,
        schema_name: str,
        spec: Spec | dict,
        with_default=False,
        with_typesafe=False,
    ) -> Tuple[bool, Any, str]:
        try:
            ref_resolver = validators.RefResolver.from_schema(spec)
            schema = spec["components"]["schemas"][schema_name]
            _obj = copy.deepcopy(obj)
            validator = OAS30Validator
            if with_default:
                validator = cls.extend_with_default(validator)
            if with_typesafe:
                validator = cls.extend_with_typesafe(validator)
            _validate(_obj, schema, resolver=ref_resolver, cls=validator)
        except Exception as e:
            return False, _obj, e.args[0]
        else:
            return True, _obj, None
