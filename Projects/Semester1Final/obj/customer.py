from Projects.Semester1Final.utils.fsm import *
import threading
import globals
import random

# Crepe class
class Customer():

    # Properties
    order = ""
    position_x = 0
    position_y = 0
    customer_fsm = FSM("waiting_to_take_order")

    # Here are the different values of the FSM:
    # in_line
    # waiting for order - NOTE: will auto take order when first in line
    # eating
    # leaving/left

    def take_order(self):
        # Starting order timer
        threading.Timer(30, self.order_expired).start()
        print("Taking order!")
    
    def order_expired(self):
        # If the customer is still waiting for their order, leave
        if self.customer_fsm.current_state == "waiting_for_order":
            print("Order expired!")
            self.customer_fsm.run_transition("left")
    
    def recalculate_line(self):
        # Recalculate line position when customer leaves/receives food
        self.position_y = len(globals.customers) + 1
        self.position_x = 1

        # If the customer is first in line, take their order
        if self.position_y == 1:
            self.customer_fsm.run_transition("take_order")
    
    def receive_food(self):
        print("Received food!")
        self.customer_fsm.run_transition("eating")
        threading.Timer(15, self.leave).start()
    
    def leave(self):
        print("Leaving!")


    # Setup FSM tree
    def __init__(self):
        # Line / Recalculate Line
        self.customer_fsm.register_transition("in_line", "recalculate_line", self.recalculate_line, [], "in_line")

        # Take Order
        self.customer_fsm.register_transition("in_line", "take_order", self.take_order, [], "waiting_for_order")

        # Receive Food
        self.customer_fsm.register_transition("waiting_for_order", "receive_food", None, [], "eating")

        # Leaving
        self.customer_fsm.register_transition("waiting_for_order", "leave", self.leave, [], "left")
        self.customer_fsm.register_transition("eating", "leave", self.leave, [], "left")

        # Generate crepe type (savory or sweet)
        self.order = random.choice(["sweet", 
                                    #"savory",
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
        if self.order == "savory":
            for i in range(ingredient_count):
                self.order += random.choice(["Ha", "Ch", "Mu", "To", "Sp", "Ba"])
        elif self.order == "sweet":
            for i in range(ingredient_count):
                self.order += random.choice(["St", "Bn", "Co", "Wh", "Bl", "Ap"])
            

