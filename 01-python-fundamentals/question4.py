'''Use the get_cost() function you defined in Question 3 to calculate the cost of applying one coat of paint to a room with:

    432 square feet of walls, and
    144 square feet of ceiling.

Assume that one gallon of paint covers 400 square feet and costs $15. As in Question 3, assume you can buy partial gallons of paint. Do not round your answer.'''

def get_cost(sqft_walls, sqft_ceiling, sqft_per_gallon, cost_per_gallon):
    total_sqft = sqft_walls + sqft_ceiling
    gallons_needed = total_sqft / sqft_per_gallon
    cost = cost_per_gallon * gallons_needed
    return cost

project_cost = get_cost(432, 144, 400, 15)
print(f"The cost of painting the room is: ${project_cost:.2f}")