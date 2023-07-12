
UNASSIGNED = 0
ASSIGNED = 1
IN_PROGRESS = 2
COMPLETED = 3

TASK_STATES = (
    (UNASSIGNED, "Unassigned"),
    (ASSIGNED, "Assigned"),
    (IN_PROGRESS, "In Progress"),
    (COMPLETED, "Completed")
)

PROFICIENCY_MIN_RATING = 0.0
PROFICIENCY_MAX_RATING = 10.0
PROFICIENCY_NOT_WITHIN_RANGE = "Proficiency should be within {} and {}".format(PROFICIENCY_MIN_RATING, PROFICIENCY_MAX_RATING)