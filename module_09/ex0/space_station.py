from datetime import datetime
from typing import Optional
from pydantic import (  # type: ignore[import-not-found]
    BaseModel,
    Field,
    ValidationError,
)


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(default=None, max_length=200)


def main() -> None:
    print("Space Station Data Validation")
    print("========================================")
    try:
        print("Valid station created:")
        stats = SpaceStation(
            station_id="SS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime.now()
        )
        print(f"ID: {stats.station_id}")
        print(f"Name: {stats.name}")
        print(f"Crew: {stats.crew_size}")
        print(f"Power: {stats.power_level}%")
        print(f"Oxygen: {stats.oxygen_level}%")
        print(f"Time: {stats.last_maintenance}")
        if stats.is_operational:
            print("Status: Operational")
        else:
            print("Status: Closed")
    except ValidationError as e:
        print(e)

    print("========================================")
    print("Expected validation error:")
    try:
        stats = SpaceStation(
            station_id="SS001",
            name="International Space Station",
            crew_size=99,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime.now()
        )
    except ValidationError as e:
        for error in e.errors():
            print(error["msg"])


if __name__ == "__main__":
    main()
