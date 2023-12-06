# Simple template class for an FSM

class FSM:
    # Private Variables
    transitions = {}
    current_state = None

    # Configuration
    def register_transition(self, initial_state, event, action, parameters, final_state):
        self.transitions[(initial_state, event)] = (action, parameters, final_state)
    
    # Execution
    def run_transition(self, event):
        try:
            (action, parameters, final_state) = self.transitions[(self.current_state, event)]
            if action != None:
                action(*parameters)
            self.current_state = final_state
        except KeyError:
            pass
    
    # Constructor
    def __init__(self, initial_state):
        self.current_state = initial_state
