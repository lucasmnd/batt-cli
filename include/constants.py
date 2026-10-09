from pathlib import Path

BATTERY_DIR = Path('/sys/class/power_supply/BAT0')

class BattFiles:
    ALARM: Path = BATTERY_DIR / 'alarm'
    CAPACITY: Path = BATTERY_DIR / 'capacity'
    CAPACITY_LEVEL: Path = BATTERY_DIR / 'capacity_level'
    CHARGE_BEHAVIOUR: Path = BATTERY_DIR / 'charge_behaviour'
    CYCLE_COUNT: Path = BATTERY_DIR / 'cycle_count'
    END_THRESHOLD: Path = BATTERY_DIR / 'charge_control_end_threshold'
    ENERGY_FULL: Path = BATTERY_DIR / 'energy_full'
    ENERGY_FULL_DESIGN: Path = BATTERY_DIR / 'energy_full_design'
    ENERGY_NOW: Path = BATTERY_DIR / 'energy_now'
    MANUFACTURER: Path = BATTERY_DIR / 'manufacturer'
    MODEL_NAME: Path = BATTERY_DIR / 'model_name'
    POWER_NOW: Path = BATTERY_DIR / 'power_now'
    PRESENT: Path = BATTERY_DIR / 'present'
    SERIAL_NUMBER: Path = BATTERY_DIR / 'serial_number'
    START_THRESHOLD: Path = BATTERY_DIR / 'charge_control_start_threshold'
    STATUS: Path = BATTERY_DIR / 'status'
    TECHNOLOGY: Path = BATTERY_DIR / 'technology'
    TYPE: Path = BATTERY_DIR / 'type'
    VOLTAGE_MIN_DESIGN: Path = BATTERY_DIR / 'voltage_min_design'
    VOLTAGE_NOW: Path = BATTERY_DIR / 'voltage_now'

CHARGE_BEHAVIOUR_DESCRIPTION = {
    'auto' : 'Start charging when (capacity ≤ start threshold), stop charging when (capacity ≥ end threshold)',
    'inhibit-charge' : 'Do not charge while AC is attached',
    'inhibit-charge-awake' : 'Do not charge while AC is attached, but only when device is awake',
    'force-discharge' : 'Use battery as power supply even when AC is attached',
}
