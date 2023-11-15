"""
This module implements a Finite State Machine (FSM).

You define an FSM by building a dictionary of transitions. For a given input symbol,
the process() method uses the dictionary to decide what action to call and what
the next state will be. The FSM has a dictionary of transitions that associate the tuples:

        (input_symbol, current_state) --> (action, next_state)

Where "action" is a function you define. The symbols and states can be any
objects. You use the add_transition() method to add to the transition table.

@author: Ms. Namasivayam
@version: 2022
"""


class FSM:
    def __init__(self, initial_state):
        # Dictionary (input_symbol, current_state) --> (action, next_state).
        self.state_transitions = {}
        self.current_state = initial_state

    def add_transition(self, input_symbol, state, action=None, next_state=None):
        """
        Adds a transition to the instance variable state_transitions
        that associates:
            (input_symbol, current_state) --> (action, next_state)

        The action may be set to None in which case the process() method will
        ignore the action and only set the next_state.

        The next_state may be set to None in which case the current state will be unchanged.
        
        Args:
            input_symbol (anything): The input received
            state (anything): The current state
            action (function, optional): The action to take/function to run. Defaults to None.
            next_state (anything, optional): The next state to transition to. Defaults to None.
        """
        self.state_transitions[(input_symbol, state)] = (action, next_state)

    def get_transition(self, input_symbol, state):
        """
        Returns tuple (action, next state) given an input_symbol and state.
        Normally you do not call this method directly. It is called by
        process().

        Args:
            input_symbol (anything): The given input symbol
            state (anything): The current state

        Returns:
            tuple: Returns the tuple (action, next_state)
        """
        return self.state_transitions[(input_symbol, state)]

    def process(self, input_symbol):
        """
        The main method that you call to process input. This may
        cause the FSM to change state and call an action. This method calls
        get_transition() to find the action and next_state associated with the
        input_symbol and current_state. If the action is None then the action
        is not called and only the current state is changed. This method
        processes one complete input symbol.
        Args:
            input_symbol (anything): The input to process
        """
        result = self.get_transition(input_symbol, self.current_state)
        action = result[0]()
        self.current_state = result[1]
