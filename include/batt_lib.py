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

# TODO: print all info about status
def print_status(batt_data: BatteryData):
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