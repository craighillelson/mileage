"""__doc__"""

# import
import datetime
from datetime import date

RTN = lambda: "\n"

# figure out what year it is
NOW = datetime.datetime.now()
YEAR = NOW.year

# define variables
MILEAGE_TO_DATE = "How many miles have you run this year? " \
                  "(please enter an integer) "
MILEAGE_GOAL = "What is your goal for the year? "
NOT_AN_INTEGER = "That won't work. Please enter an integer. "
MILES = None
GOAL = None

print(RTN())

# prompt user for mileage to date and mileage goal for the year
while MILES is None:
    try:
        MILES = float(input(MILEAGE_TO_DATE))
    except ValueError:
        print(NOT_AN_INTEGER)

while GOAL is None:
    try:
        GOAL = float(input(MILEAGE_GOAL))
    except ValueError:
        print(NOT_AN_INTEGER)

# calculate how many days are left in the year
TODAY = date.today()
LAST_DAY_OF_THE_YEAR = date(YEAR, 12, 31)
DELTA = LAST_DAY_OF_THE_YEAR - TODAY
DAYS_LEFT = DELTA.days

# calculate how many miles per day the user will need to average
# to achieve their yearly mileage goal
DIFF_MILEAGE = GOAL - MILES
if DIFF_MILEAGE > 0:
    MILES_DAY = float(DIFF_MILEAGE) / float(DELTA.days)
    GOAL = int(GOAL)
    print(f"With {DAYS_LEFT} days left in the year, you'll need to" \
          f"average {'{0:.2}'.format(MILES_DAY)} miles per day to hit " \
          f"your {GOAL} mile goal.")
else:
    print(f"Congratulations! You hit your mileage goal with {DAYS_LEFT} days" \
          "left in the year.")

print(RTN())
