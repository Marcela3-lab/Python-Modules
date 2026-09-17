from pydantic import BaseModel, model_validator, Field
from enum import Enum

class aliencontact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)0
    timestamp:datetime


if __name__ == "__main__":
    print("Alien Contact Log Validation")
    print("="*40)