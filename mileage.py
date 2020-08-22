"""
Calculate the average miles per day a user would have to run based on a user
provided yearly goal.
"""

import datetime
from datetime import date


def prompt_user(mileage, user_prompt):
    """
    Get user input, return an error if the user enters a value that is not an
    integer or a float.
    """
    while mileage is None:
        try:
            mileage = float(input(user_prompt))
        except ValueError:
            print(NOT_AN_INTEGER_OR_FLOAT)

    return mileage


def diff_mileage(mileage_goal, mileage_ytd):
    """
    Calculate the difference between mileage goal for the year and number of
    miles run to date.
    """
    return mileage_goal - mileage_ytd


NOW = datetime.datetime.now()
YEAR = NOW.year

NOT_AN_INTEGER_OR_FLOAT = "That won't work. Please enter an integer or a \
                          float. "
MILES = GOAL = None

MILES_RUN = prompt_user(MILES, "\nHow many miles have you run this year? "\
                        "(please enter an integer or float)\n> ")
YEARLY_GOAL = float(prompt_user(GOAL, 'What is your goal for the year?\n> '))

TODAY = date.today()
LAST_DAY_OF_THE_YEAR = date(YEAR, 12, 31)
DELTA = LAST_DAY_OF_THE_YEAR - TODAY
DAYS_LEFT = DELTA.days

MILEAGE_DIFF = diff_mileage(YEARLY_GOAL, MILES_RUN)
if MILEAGE_DIFF <= 0:
    print(f'Congratulations! You hit your mileage goal with {DAYS_LEFT} days '
          'left in the year.\n')
else:
    MILES_DAY = float(MILEAGE_DIFF) / float(DELTA.days)
    print(f'With {DAYS_LEFT} days left in the year, you\'ll need to '
          f'average {"{0:.2}".format(MILES_DAY)} miles per day to hit '
          f'your {YEARLY_GOAL} mile goal.\n')
