from include.batt_lib import (
    get_batt_data, print_status
)

def status(args):
    print_status(get_batt_data())