from utils.fsm import *
import threading
import globals
import random

# Crepe class
class Customer():

    # Properties
    order = ""
    customer_fsm = FSM("waiting_to_take_order")

    crepe_to_grade = {
        "ham": "Ha",
        "cheese": "Ch",
        "mushroom": "Mu",
        "tomato": "To",
        "spinach": "Sp",
        "bacon": "Ba",
        "strawberry": "St",
        "banana": "Bn",
        "chocolate": "Co",
        "whip": "Wh",
        "blueberry": "Bl",
        "apple": "Ap"
    }

    # Here are the different values of the FSM:
    # waiting for order - NOTE: will auto take order when first in line
    # eating
    # leaving/left

    def take_order(self):
        # Generate crepe type (savory or sweet)
        type = random.choice(["sweet", 
                                    "savory",
                                    ]) 

        # INGREDIENTS 
        # SAVORY INGREDIENTS (Top 6)
        # Ha = Ham
        # Ch = Cheese
        # Mu = Mushroom
        # To = Tomato
        # Sp = Spinach
        # Ba = Bacon

        # SWEET INGREDIENTS (Top 6)
        # St = Strawberry
        # Bn = Banana
        # Co = Chocolate
        # Wh = Whipped Cream
        # Bl = Blueberry
        # Ap = Apple

        # Generate crepe ingredients (2-4 ingredients)
        ingredient_count = random.randint(2, 4)
        choices = []
        if type == "savory":
            for i in range(ingredient_count):
               choices.append(random.choice(["Ha", "Ch", "Mu", "To", "Sp", "Ba"]))
        elif type == "sweet":
            for i in range(ingredient_count):
               choices.append(random.choice(["St", "Bn", "Co", "Wh", "Bl", "Ap"]))
        
        # Remove duplicates
        self.order = "".join(set(choices))
        
        # Starting order timer
        self.fail_timer = threading.Timer(15, self.order_expired)
        self.fail_timer.start()
    
    def order_expired(self):
        # If the customer is still waiting for their order, leave
        if self.customer_fsm.current_state == "waiting_for_order":
            self.customer_fsm.run_transition("order_expired")
    
    def grade(self, result):
        # Calculate grade
        earnings = 0
        toppings = result.toppings
        toppings_converted = []
        for topping in toppings:
            toppings_converted.append(self.crepe_to_grade[topping])
        requested_toppings = []
        for i in range(0, len(self.order), 2):
            requested_toppings.append(self.order[i:i+2])
        requested_toppings.sort()
        toppings_converted.sort()
        if requested_toppings == toppings_converted:
            earnings = 5
        else:
            earnings = 0
        globals.money += earnings
        self.customer_fsm.run_transition("order_ready")
    
    def reset(self):
        self.order = ""
        if self.fail_timer != None:
            self.fail_timer.cancel()

    # Setup FSM tree
    def __init__(self):
        # Waiting to take order
        self.customer_fsm.register_transition("waiting_to_take_order", "take_order", self.take_order, [], "waiting_for_order")
        # Success
        self.customer_fsm.register_transition("waiting_for_order", "order_ready", self.reset, [], "waiting_to_take_order")
        # Fail
        self.customer_fsm.register_transition("waiting_for_order", "order_expired", None, [], "fail")


