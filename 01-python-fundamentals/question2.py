'''You are thinking about buying a home and want to get an idea of how much you will spend, based on the number of bedrooms and bathrooms. You are trying to decide between four different options:

    Option 1: house with two bedrooms and three bathrooms
    Option 2: house with three bedrooms and two bathrooms
    Option 3: house with three bedrooms and three bathrooms
    Option 4: house with three bedrooms and four bathrooms

Use the get_expected_cost() function you defined in question 1 to set option_1, option_2, option_3, and option_4 to the expected cost of each option.'''

def get_expected_cost(beds, baths):
    value = 80000 + (30000 * beds) + (10000 * baths) 
    return value

# Test the function
option_1 = get_expected_cost(2, 3)
option_2 = get_expected_cost(3, 2)
option_3 = get_expected_cost(3, 3)
option_4 = get_expected_cost(3, 4)
print("Option 1: ", option_1)
print("Option 2: ", option_2)
print("Option 3: ", option_3)       
print("Option 4: ", option_4)