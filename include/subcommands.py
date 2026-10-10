from argparse import Namespace

from include.batt_lib import (
    get_batt_data, print_status, set_interval,
    CapacityInterval
)

def status(args: Namespace) -> None:
    print_status(get_batt_data())

def set(args: Namespace) -> None:
    interval: CapacityInterval = args.interval
    set_interval(interval)
    # TODO: give feedback to user