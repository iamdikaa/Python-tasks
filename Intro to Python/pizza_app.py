print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bill = 0
small_pizza = 15
medium_pizza = 20
large_pizza = 25

pepperoni_small = 2
pepperoni_medium_large = 3
extra_cheese_price = 1

if size == 'S':
  if add_pepperoni == 'Y':
    if extra_cheese == 'Y':
      bill = small_pizza + pepperoni_small + extra_cheese_price
      print(f'your final bill is ${bill}')
  elif add_pepperoni == 'Y':
    if extra_cheese == 'N':
      bill = small_pizza + pepperoni_small
      print(f'Your final bill is ${bill}')
  elif add_pepperoni == 'N':
    if extra_cheese == 'N':
      bill += small_pizza
      print(f'Your final bill is ${bill}')
  elif add_pepperoni == 'N':
    if extra_cheese == 'Y':
      bill = small_pizza + extra_cheese_price
      print(f'Your final bill is ${bill}')
      
elif size == 'M':
  if add_pepperoni == 'Y':
    if extra_cheese == 'Y':
      bill = medium_pizza + pepperoni_medium_large + extra_cheese_price
      print(f'your final bill is ${bill}')
  elif add_pepperoni == 'Y':
    if extra_cheese == 'N':
      bill = medium_pizza + pepperoni_medium_large
      print(f'Your final bill is ${bill}')
  elif add_pepperoni == 'N':
    if extra_cheese == 'N':
      bill += medium_pizza
      print(f'Your final bill is ${bill}')
  elif add_pepperoni == 'N':
    if extra_cheese == 'Y':
      bill = medium_pizza + extra_cheese_price
      print(f'Your final bill is ${bill}')
      
elif size == 'L':
  if add_pepperoni == 'Y':
    if extra_cheese == 'Y':
      bill = large_pizza + pepperoni_medium_large + extra_cheese_price
      print(f'Your final bill is ${bill}')
  elif add_pepperoni == 'Y':
    if extra_cheese == 'N':
      bill = large_pizza + pepperoni_medium_large
      print(f'Your final bill is ${bill}')
  elif add_pepperoni == 'N':
    if extra_cheese == 'N':
      bill += large_pizza
      print(f'Your final bill is ${bill}')
  elif add_pepperoni == 'N':
    if extra_cheese == 'Y':
      bill = large_pizza = extra_cheese_price
      print(f'Your final bill is ${bill}')