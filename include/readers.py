from pathlib import Path
from include.internals import get_batt_field
from include.constants import BattFiles

def read_charge_interval():
    start_thr = int(get_batt_field(BattFiles.START_THRESHOLD))
    end_thr = int(get_batt_field(BattFiles.END_THRESHOLD))
