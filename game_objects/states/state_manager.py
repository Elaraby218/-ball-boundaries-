from typing import Dict, Type, TypedDict
from .base_state import BaseState


class StateManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(StateManager, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        self.states: Dict[str, BaseState] = {}
        self.current_state: BaseState | None = None
        self.next_state: BaseState | None = None


    def add_state(self, state_name: str, state: BaseState):
        self.states[state_name] = state

    def change_state(self, state_name: str):
        if state_name in self.states:
            self.next_state = self.states[state_name]

    def update(self, delta_time):
        if self.next_state:
            self.current_state = self.next_state
            self.current_state.enter()
            self.next_state = None

        if self.current_state:
            self.current_state.update(delta_time)

    def draw(self, screen):
        if self.current_state:
            self.current_state.draw(screen)

    def handle_event(self, event):
        if self.current_state:
            self.current_state.handle_events(event) 
