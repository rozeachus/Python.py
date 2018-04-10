"""

This code is taken from the Python excercise 'Taking a Vacation' on CodeAcademy.
It will calculate how much a trip will cost, taking into account the hotel, car hire, flights and spending money.

"""
# First we define the cost of the hotel, which is $140 per night

def hotel_cost(nights):
  return 140 * nights

# Then we define the plane ride cost, which is dependent on the city you travel to

def plane_ride_cost(city):
  if city == "Charlotte":
    return 183
  elif city == "Tampa":
    return 220
  elif city == "Pittsburgh":
    return 222
  elif city == "Los Angeles":
    return 475
  
  # Then we define the rental car cost. Note - the price changes dependent on hiring days

def rental_car_cost(days):
  cost = days * 40
  if days >= 7:
    cost -= 50
  elif days >= 3:
    cost -= 20
  return cost

# We sum the three functions together

def trip_cost(city, days, spending_money):
  return rental_car_cost(days) + hotel_cost(days - 1) + plane_ride_cost(city) + spending_money

# Lastly, we print where we're staying, how many days for and how much spending money we have 

print trip_cost("Los Angeles", 5, 600)
