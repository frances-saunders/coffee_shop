# Define functions
def coffee_bot():
  print("Welcome to the cafe!")
  size = get_size()
  drink_type = get_drink_type()
  hot_or_cold = get_hot_or_cold()

  print('\nUnderstood. One {} {} {}'.format(size, hot_or_cold, drink_type))
  name = input('\nCan I get your name please? \n>> ')
  print('Thanks, {}! Your drink will be ready shortly.'.format(name))

def error_message():
  print("I'm sorry, I didn't understand your selection. Let's try again.\n")

def get_size():
  res = input('What size drink can I get for you? \n[S] Small \n[M] Medium \n[L] Large \n>> ')

  if res.lower() == 's':
    return 'Small'
  elif res.lower() == 'm':
    return 'Medium'
  elif res.lower() == 'l':
    return 'Large'
  else: 
    error_message()
    return get_size()

def get_hot_or_cold():
  res = input('Would you like your drink hot or cold? \n[H] Hot \n[C]Cold \n>> ')
  
  if res.lower() == 'h':
    return 'Hot'
  elif res.lower() == 'c':
    return 'Cold'
  else:
    error_message()
    return get_hot_or_cold()

def get_drink_type():
  res = input('What type of drink would you like? \n[A] Brewed Coffee \n[B] Frappuccino \n[C] Latte \n[D] Cappuccino \n>> ')

  if res.lower() == 'a':
    return order_coffee()
  elif res.lower() == 'b':
    return order_frappuccino()
  elif res.lower() == 'c':
    return order_latte()
  elif res.lower() == 'd':
    return order_cappuccino
  else:
    error_message()
    return get_drink_type()

def order_coffee():
  res = input('What kind of coffee would you like? \n[A] Black \n[B] Regular \n[C] Decaf \n[D] Irish \n>> ')
  if res.lower() == 'a':
    return 'Black Coffee'
  elif res.lower() == 'b':
    return 'Regular Coffee'
  elif res.lower() == 'c':
    return 'Decaf Coffee'
  elif res.lower() == 'd':
    return 'Irish Coffee'
  else:
    error_message()
    return order_coffee()

def order_frappuccino():
  res = input('What kind of frappuccino would you like? \n[A] Mocha Cookie Crumble Frappuccino \n[B] Caramel Ribbon Crunch Frappuccino \n[C] Espresso Frappuccino \n[D] White Chocolate Mocha Frappuccino \n[E] Java Chip Frappuccino \n[F] Mocha Frappuccino \n>> ')
  if res.lower() == 'a':
    return 'Mocha Cookie Crumble Frappuccino'
  elif res.lower() == 'b':
    return 'Caramel Ribbon Crunch Frappuccino'
  elif res.lower() == 'c':
    return 'Espresso Frappuccino'
  elif res.lower() == 'd':
    return 'White Chocolate Mocha Frappuccino'
  elif res.lower() == 'e':
    return 'Java Chip Frappuccino'
  elif res.lower() == 'f':
    return 'Mocha Frappuccino'
  else:
    error_message()
    return order_frappuccino()


def order_latte():
  res = input('And what kind of milk for your latte? \n[A] 2% milk \n[B] Non-fat milk \n[C] Soy milk \n>> ')
  
  if res.lower() == 'a':
    return 'Latte with 2% milk'
  elif res.lower() == 'b':
    return 'Latte with non-fat milk'
  elif res.lower() == 'c':
    return 'Latte with soy milk'
  else:
    error_message()
    return order_latte()

def order_cappuccino():
  res = input('What kind of cappuccino would you like? \n[A] Mocha \n[B] Vanilla \n[C] Hazelnut \n[D] Cinnamon Dulce \n[E] Classic \n>> ')

  if res.lower() == 'a':
    return 'Mocha capppucino'
  elif res.lower() == 'b':
    return 'Vanilla cappucino'
  elif res.lower() == 'c':
    return 'Hazelnut cappucino'
  elif res.lower() == 'd':
    return 'Cinnamon dulce cappucino'
  elif res.lower() == 'e':
    return 'Classic cappucino'
  else:
    error_message()
    return order_cappuccino()

# Call coffee_bot()
coffee_bot()
