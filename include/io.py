from include.batt_lib import BatteryData
from include.errors import BatteryError
from include.constants import CHARGE_BEHAVIOUR_DESCRIPTION

def print_status(batt_data: BatteryData) -> None:
    print(
        # Line 1
        f"Current capacity: {batt_data.capacity}%, {batt_data.status} "
        f"({batt_data.power_sign}{round(batt_data.power_now/(10**6), 1)}W)"
        "\n"

        # Line 2
        f"Target capacity interval: {batt_data.start_threshold}-{batt_data.end_threshold}%"
        "\n"

        # Line 3
        f"Current charge behavior: {batt_data.charge_behaviour} -> \"{CHARGE_BEHAVIOUR_DESCRIPTION[batt_data.charge_behaviour]}\""
        "\n"

        # Line 4
        f"Health: {batt_data.health_percentage}% ({batt_data.cycle_count} cycles)"
    )

def parse_capacity(expression: str):
    start: int | None = None
    end: int | None = None

    if expression.count('-') != 1:
        # TODO: write error message
        raise BatteryError("placeholder1")

    try:
        start, end = [(int(x) if x else None) for x in expression.split('-')]
    except ValueError:
        # TODO: write error message
        raise BatteryError("placeholder2")

    if start is not None and end is not None:
        if start >= end:
            raise BatteryError("placeholder3")

    return (start, end)
