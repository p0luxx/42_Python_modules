from datetime import datetime
from enum import Enum
from typing import List

from pydantic import (  # type: ignore[import-not-found]
    BaseModel,
    Field,
    ValidationError,
    model_validator,
)


class Rank(str, Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validate_mission_rules(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")

        has_leadership = any(
            member.rank in (Rank.COMMANDER, Rank.CAPTAIN)
            for member in self.crew
        )

        if not has_leadership:
            raise ValueError("Mission must have at least one"
                             "Commander or Captain")

        if self.duration_days > 365:
            experienced_count = sum(
                1 for member in self.crew if member.years_experience >= 5
            )
            if experienced_count / len(self.crew) < 0.5:
                raise ValueError(
                    "Long missions (> 365 days) require at least "
                    "50% experienced crew (5+ years)"
                )

        if any(not member.is_active for member in self.crew):
            raise ValueError("All crew members must be active")

        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("=========================================")

    try:
        valid_mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date="2026-08-11T00:00:00",
            duration_days=900,
            budget_millions=2500.0,
            crew=[
                CrewMember(
                    member_id="C01",
                    name="Sarah Connor",
                    rank=Rank.COMMANDER,
                    age=42,
                    specialization="Mission Command",
                    years_experience=15,
                ),
                CrewMember(
                    member_id="C02",
                    name="John Smith",
                    rank=Rank.LIEUTENANT,
                    age=34,
                    specialization="Navigation",
                    years_experience=8,
                ),
                CrewMember(
                    member_id="C03",
                    name="Alice Johnson",
                    rank=Rank.OFFICER,
                    age=29,
                    specialization="Engineering",
                    years_experience=3,
                ),
            ],
        )

        print("Valid mission created:")
        print(f"Mission: {valid_mission.mission_name}")
        print(f"ID: {valid_mission.mission_id}")
        print(f"Destination: {valid_mission.destination}")
        print(f"Duration: {valid_mission.duration_days} days")
        print(f"Budget: ${valid_mission.budget_millions}M")
        print(f"Crew size: {len(valid_mission.crew)}")
        print("Crew members:")
        for member in valid_mission.crew:
            print(f"- {member.name} "
                  f"({member.rank.value}) - {member.specialization}")

    except ValidationError as e:
        print(f"Unexpected error: {e}")

    print("=========================================")
    print("Expected validation error:")

    try:
        SpaceMission(
            mission_id="M2024_MOON",
            mission_name="Lunar Scout Mission",
            destination="Moon",
            launch_date="2026-09-01T12:00:00",
            duration_days=30,
            budget_millions=150.0,
            crew=[
                CrewMember(
                    member_id="C04",
                    name="Bob Ross",
                    rank=Rank.LIEUTENANT,
                    age=30,
                    specialization="Piloting",
                    years_experience=4,
                ),
                CrewMember(
                    member_id="C05",
                    name="Eve Online",
                    rank=Rank.CADET,
                    age=22,
                    specialization="Communications",
                    years_experience=1,
                ),
            ],
        )
    except ValidationError as e:
        for error in e.errors():
            msg = error["msg"].replace("Value error, ", "")
            print(msg)


if __name__ == "__main__":
    main()
