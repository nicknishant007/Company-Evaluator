import json

from pydantic import BaseModel


def serialize(value):

    if isinstance(value, BaseModel):

        return value.model_dump_json()

    return json.dumps(value)


def deserialize(value):

    if value is None:
        return None

    return json.loads(value)