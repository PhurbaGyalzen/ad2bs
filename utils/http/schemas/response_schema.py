from pydantic import BaseModel


class BaseResponse(BaseModel):
    status: bool
    result: str

class SuccessResponse(BaseResponse):
    status = True
    result: str

class FailureResponse(BaseResponse):
    status = False
    result: str