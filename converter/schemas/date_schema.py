from pydantic import BaseModel, validator, Field

class DateConvertSchema(BaseModel):
    year: int = 2000
    month: int = 6
    day: int = 15

    @validator("month")
    def validate_month(cls, value):
        if value > 12 or value <= 0:
            raise ValueError(f"Month should be 1 to 12. Month cannot be {value}") 

    @validator("day")
    def validate_day(cls, value):
        if value > 31 or value <= 0:
            raise ValueError(f"Day {value} cannot be possible please check the day")
        return value
    