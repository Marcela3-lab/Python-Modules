from pydantic import BaseModel, model_validator, Field, ValidationError
from enum import Enum
from datetime import datetime
from typing import Optional


class Contact_type (Enum):
    PHYSICAL = "Physical"
    TELEPHATIC = "Telephatic"
    RADIO = "Radio"


class AlienContactReport(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: Contact_type
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode="after")
    def validation_rules(self) -> "AlienContactReport":
        if not self.contact_id.startswith("AC"):
            raise ValueError(
                "Contact ID must start with AC (Alien Contact)"
            )
        if (
            self.contact_type == Contact_type.PHYSICAL
            and self.is_verified is True
        ):
            raise ValueError(
                "Physical contacts must be verified")
        if (
            self.contact_type == Contact_type.TELEPHATIC
            and self.witness_count < 3
        ):
            raise ValueError(
                "Telephatic contact requires at least 3 witnesses")

        if self.signal_strength >= 7.0 and not self.message_received:
            raise ValueError(
                "Strong signals (signal_strength > 7.0) must include"
                "message_received.")
        return self


if __name__ == "__main__":
    print("Alien Contact Log Validation")
    print("="*40)
    print("Valid cont report:")
    valid_report = AlienContactReport(
            contact_id="AC_2024_001",
            timestamp=datetime(2024, 1, 1, 12, 0),
            contact_type=Contact_type.RADIO,
            location="Area 51, Nevada",
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli",
            is_verified=True,
        )

    print(f"ID: {valid_report.contact_id}")
    print(f"Type: {valid_report.contact_type.value}")
    print(f"Location: {valid_report.location}")
    print(f"Signal: {valid_report.signal_strength}/10")
    print(f"Duration: {valid_report.duration_minutes} minutes")
    print(f"Witnesses: {valid_report.witness_count}")
    print(f"Message: '{valid_report.message_received}'")
    print()
    print("="*40)
    print("Expected validation error:")
    try:
        invalid_report = AlienContactReport(
            contact_id="AC_2024_001",
            timestamp=datetime(2024, 1, 1, 12, 0),
            contact_type=Contact_type.TELEPHATIC,
            location="Area 51, Nevada",
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=1,
            message_received="Greetings from Zeta Reticuli",
            is_verified=True,
        )
    except ValidationError as e:
        for erro in e.errors():
            print(erro['msg'].replace("Value error, ", ""))
