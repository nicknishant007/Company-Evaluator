import json


def serialize(value):

    return json.dumps(value)


def deserialize(value):

    if value is None:
        return None

    return json.loads(value)