from pathlib import Path
from include.constants import BattFiles

# this function shouldn't be used directly as part of the API. it's only an internal helper. (it requires a wrapper function for meaningful type annotation)
def get_batt_field(field: Path) -> str:
    try:
        ret = field.read_text().strip()
    finally:
        # TODO: treat excpetions, low level errors
        pass

    return ret
