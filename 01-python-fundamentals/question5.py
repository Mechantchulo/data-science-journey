""" ''''''# 🌶️ Question 5

Now say you can no longer buy fractions of a gallon.  (For instance, if you need 4.3 gallons to do a project, then you have to buy 5 gallons of paint.)

With this new scenario, you will create a new function `get_actual_cost` that uses the same inputs and calculates the cost of your project.

One function that you'll need to use to do this is `math.ceil()`.  We demonstrate usage of this function in the code cell below.  It takes as a number as input and rounds the number up to the nearest integer.  

Run the next code cell to test this function for yourself.  Feel free to change the value of `test_value` and make sure `math.ceil()` returns the number you expect.'''''' """

import math
def get_actual_cost(sqft_walls, sqft_ceiling, sqft_per_gallon, cost_per_gallon):
    
    total_sqft = sqft_walls + sqft_ceiling
    
    gallons_needed = total_sqft / sqft_per_gallon
    new_gallon_value = math.ceil(gallons_needed)
    cost = cost_per_gallon * new_gallon_value
    return cost

project_cost = get_actual_cost(432, 144, 400, 15)
print(f"The cost of painting the room is: ${project_cost:.2f}")