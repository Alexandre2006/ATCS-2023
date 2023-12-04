from Projects.Semester1Final.utils.fsm import *
import threading

# Crepe class
class Crepe():

    # Properties
    crepe_fsm = FSM("uncooked")
    toppings = []

    # FSM - COOK TIME
    def cook(self, side):
        if side == 1 and self.crepe_fsm.current_state == "cooking_side_1":
            self.crepe_fsm.run_transition("cooked_side_1")
            print("Cooked!")
        elif side == 2 and self.crepe_fsm.current_state == "cooking_side_2":
            self.crepe_fsm.run_transition("cooked_side_2")
            print("Cooked!")
    
    def burn(self, side):
        if side == 1 and self.crepe_fsm.current_state == "cooked_side_1":
            self.crepe_fsm.run_transition("burned")
            print("Burned!")
        elif side == 2 and self.crepe_fsm.current_state == "cooked_side_2":
            self.crepe_fsm.run_transition("burned")
            print("Burned!")

    def start_cooking(self, side):
        print("Cooking!")
        threading.Timer(5, self.cook, [side]).start()
        threading.Timer(10, self.cook, [side]).start()
    
    # Toppings
    def add_topping(self, topping):
        self.toppings.append(topping)

    # Constructor
    def __init__(self):
        # Cook Transitions
        self.crepe_fsm.register_transition("uncooked", "cook_side_1", self.start_cooking, [1], "cooking_side_1")
        self.crepe_fsm.register_transition("cooking_side_1", "cooked_side_1", self.start_cooking, [1], "cooked_side_1")
        self.crepe_fsm.register_transition("cooked_side_1", "cook_side_2", self.start_cooking, [2], "cooking_side_2")
        self.crepe_fsm.register_transition("cooking_side_2", "cooked_side_2", self.start_cooking, [2], "cooked_side_2")
        self.crepe_fsm.register_transition("cooked_side_2", "plate", self.start_cooking, [1], "plated")
        self.crepe_fsm.register_transition("plated", "server", self.start_cooking, [1], "served")

        # Burn Transitions
        self.crepe_fsm.register_transition("cooked_side_1", "burn_side_1", None, [1], "burned")
        self.crepe_fsm.register_transition("cooked_side_2", "burn_side_2", None, [2], "burned")

        # Throw Away (if not cooked or burned)
        self.crepe_fsm.register_transition("uncooked", "throw", None, [1], "thrown_away")
        self.crepe_fsm.register_transition("cooking_side_1", "throw", None, [1], "thrown_away")
        self.crepe_fsm.register_transition("cooking_side_2", "throw", None, [1], "thrown_away")
        self.crepe_fsm.register_transition("burned", "throw", None, [1], "thrown_away")
        
                



