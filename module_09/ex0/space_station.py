from enum import Enum
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, model_validator

class ContactType(str, Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSYCAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode="after")
    def validate_complex_rules(self) -> "AlienContact":
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID need start with 'AC'")
        if self.contact_type == ContactType.PHYSYCAL and not self.is_verified:
            raise ValueError("Physical contacts need to be verified")
        if self.contact_type == ContactType.TELEPATHIC and self.witness_count < 3:
            raise ValueError("Telepathic contact requires at least 3 witnesses")
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError(
                    "Signals with power greater than 7 must be include a recieved message"
                    )
        return self


def main():
    print("Alien Contact Log Validation")
    print("======================================")

    try:
        valid_report = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.now(),
            location="Area 51, Nevada",
            contact_type=ContactType.RADIO,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli",
            is_verified=True,
        )

        print("Valid contact report:")
        print(f"ID: {valid_report.contact_id}")
        print(f"Type: {valid_report.contact_type.value}")
        print(f"Location: {valid_report.location}")
        print(f"Signal: {valid_report.signal_strength}/10")
        print(f"Duration: {valid_report.duration_minutes} minutes")
        print(f"Witnesses: {valid_report.witness_count}")
        print(f"Message: '{valid_report.message_received}'")

    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()
