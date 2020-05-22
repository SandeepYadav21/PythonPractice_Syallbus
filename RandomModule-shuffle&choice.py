>>> import random
>>> food = ["Raviolli","Pasta","Pizza","Cheesecake"]
>>> print(random.choice(food))
Raviolli
>>> print(random.choice(food))
Pasta
>>> print(random.choice(food))
Pizza
>>> print(random.choice(food))
Cheesecake
>>> print(random.choice(food))
Pizza
>>> print(random.choice(food))
Pizza
>>> 
>>> 
>>> 
>>> print(random.shuffle(food))
None
>>> food
['Pasta', 'Pizza', 'Cheesecake', 'Raviolli']
>>> random.shuffle(food)
>>> food
['Pizza', 'Pasta', 'Cheesecake', 'Raviolli']
>>> 
