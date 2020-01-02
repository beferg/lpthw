my_name = 'Byron Ferguson'
my_age = 39 # not a lie
my_height = 68 # inches
my_weight = 240 # pounds
my_eyes =  'Hazel'
my_teeth = 'White'
my_hair = 'Black'
weight_in_kg = my_weight * .454
height_in_cm = my_height * 2.54

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} pounds heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are {my_teeth}.")


# this line is tricky, try to get it exactly right
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")

print(f"Byron's weight in kilograms is {weight_in_kg}.")
print(f"Byron's height in centameters is {height_in_cm}.")
