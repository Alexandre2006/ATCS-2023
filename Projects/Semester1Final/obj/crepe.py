from utils.fsm import *
import threading

# Crepe class
class Crepe():

    # Properties
    crepe_fsm = FSM("uncooked")
    toppings = []
    cook_timer = None
    burn_timer = None

    # FSM - COOK TIME
    def cook(self):
        if self.crepe_fsm.current_state == "cooking":
            self.crepe_fsm.run_transition("cooked")
    
    def burn(self):
        if self.crepe_fsm.current_state == "cooked":
            self.crepe_fsm.run_transition("burn")

    def start_cooking(self):
        self.cook_timer = threading.Timer(5, self.cook)
        self.cook_timer.start()
        self.burn_timer = threading.Timer(10, self.burn)
        self.burn_timer.start()
    
    def cancel(self):
        if self.cook_timer != None:
            self.cook_timer.cancel()
        if self.burn_timer != None:
            self.burn_timer.cancel()
        self.toppings = []
    
    # Toppings
    def add_topping(self, topping):
        self.toppings.append(topping)

    # Constructor
    def __init__(self):
        # Cook Transitions
        self.crepe_fsm.register_transition("uncooked", "cook", self.start_cooking, [], "cooking")
        self.crepe_fsm.register_transition("cooking", "cooked", None, [], "cooked")
        self.crepe_fsm.register_transition("cooked", "plate", None, [], "plated")
        self.crepe_fsm.register_transition("plated", "serve", self.cancel, [], "uncooked")

        # Burn Transitions
        self.crepe_fsm.register_transition("cooked", "burn", self.cancel, [], "burned")

        # Throw Away Transitions
        self.crepe_fsm.register_transition("cooking", "throw", self.cancel, [], "uncooked")
        self.crepe_fsm.register_transition("cooked", "throw", self.cancel, [], "uncooked")
        self.crepe_fsm.register_transition("burned", "throw", self.cancel, [], "uncooked")
        self.crepe_fsm.register_transition("plated", "throw", self.cancel, [], "uncooked")
        
                



