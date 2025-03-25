def make_pizza(size, *toppings):
    """
    Summarize the pizza we are about to make.
    """    
    print(f"\n Making a {size}-inch pizza with the following toppings:")   
    for topping in toppings:        
        print("- " + topping)

def make_french_fries():
    print("Frozen fries going in the deep fryer")

def bake_breadsticks():
    print("Baked Breadsticks Yum")    


make_pizza(5, 'potato', 'ancovies', 'corn')