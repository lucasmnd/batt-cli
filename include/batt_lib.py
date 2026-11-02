import argparse

from dataclasses import dataclass, fields
from include.constants import BattFiles, CHARGE_BEHAVIOUR_DESCRIPTION

@dataclass
class BatteryData:
    alarm: int
    capacity: int
    capacity_level: str
    charge_behaviour: str
    cycle_count: int
    end_threshold: int
    energy_full: int
    energy_full_design: int
    energy_now: int
    manufacturer: str
    model_name: str
    power_now: int
    present: int
    serial_number: str
    start_threshold: int
    status: str
    technology: str
    type: str
    voltage_min_design: int
    voltage_now: int

    @property
    def power_sign(self) -> str:
        return '+' if self.status == 'Charging' else '-' if self.status == 'Discharging' else ''

    @property
    def health_percentage(self) -> float:
        return round(100 * self.energy_full / self.energy_full_design, 2)

class CapacityInterval:
    # TODO: this constructor is doing too much at once. split it into smaller parts.
    def __init__(self, interval: str):
        self.start: int
        self.end: int
        
        if None in [self.start, self.end]:
            batt_data = get_batt_data()
            if self.start is None:
                self.start = batt_data.start_threshold
            if self.end is None:
                self.end = batt_data.end_threshold

        for val in [self.start, self.end]:
            # TODO: double check the valid range for start and end
            if val not in range(0, 101):
                # TODO: write error message
                raise argparse.ArgumentTypeError(f"placeholder3 (val={val})")

        if self.start >= self.end:
            # TODO: write error message
            raise argparse.ArgumentTypeError("placeholder4")
        
def get_batt_data() -> BatteryData:
    data_dict = {
        field.name: field.type(getattr(BattFiles, field.name.upper()).read_text().strip())
        for field in fields(BatteryData)
    }

    for entry in data_dict['charge_behaviour'].split():
        entry: str
        if entry.startswith('['):
            data_dict['charge_behaviour'] = entry[1:-1]
            break

    return BatteryData(**data_dict)

# TODO: check write operations ordering
def set_charge_interval(interval: CapacityInterval) -> None:
    try:
        BattFiles.START_THRESHOLD.write_text(str(interval.start))
        BattFiles.END_THRESHOLD.write_text(str(interval.end))
    # TODO: handle exceptions
    finally:
        pass
