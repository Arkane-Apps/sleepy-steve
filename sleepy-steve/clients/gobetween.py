from pydantic import BaseModel, ConstrainedStr


class IntString(ConstrainedStr):
    strip_whitespace = True
    min_length = 1
    regex = r"^[0-9]+$"


class FloatString(ConstrainedStr):
    strip_whitespace = True
    min_length = 1
    regex = r"^[0-9]+(\.[0-9]+)?$"


class RoutesModel(BaseModel):
    host: str
    port: IntString
    weight: IntString
    priority: IntString
