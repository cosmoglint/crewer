from datetime import datetime, timedelta
from .constants import MIN_PROFICIENCY, MAX_PROFICIENCY


def validate_within_min(value):
    return value >= MIN_PROFICIENCY

def validate_within_max(value):
    return value <= MAX_PROFICIENCY

def diff_time_calculator(start_date, effort_estimate):
    # gives the end date of project given the effort estimate and start
    # effort estimate is in days
    # improvement : include hour based estimate system
    return start_date + timedelta(days=effort_estimate)
