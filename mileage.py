# import
from datetime import date

# define variables
mileage_to_date = "How many miles have you run this year? (please enter an integer) "
mileage_goal = "What is your goal for the year? "
not_an_integer = "That won't work. Please enter an integer. "
miles = None
goal = None

# prompt user for mileage to date and mileage goal for the year
while miles == None:
	try:
		miles = float(raw_input(mileage_to_date))
	except ValueError:
		print(not_an_integer)

while goal == None:
	try:
		goal = float(raw_input(mileage_goal))
	except ValueError:
		print(not_an_integer)

# calculate how many days are left in the year
f_date = date.today()
l_date = date(2018, 12, 31)
delta = l_date - f_date
days_left = delta.days

# calculate how many miles per day the user will need to average to achieve their yearly mileage goal
diff_mileage = goal - miles
if diff_mileage > 0:
	miles_day = float(diff_mileage) / float(delta.days)
	goal = int(goal)
	print("With %s days left in the year, you'll need to average %s miles per day to hit your %s mile goal.") % (days_left, miles_day, goal)
else:
	print("Congratulations! You hit your mileage goal with %s days left in the year.") % (days_left)