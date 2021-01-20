
class FsmManager:
    def __init__(self):
        self.current_state = None

    def update(self):
        if (self.current_state != None):
            self.current_state.update()
    
    def change_state(self, new_state):
        if (self.current_state != None):
            self.current_state.exit()

        self.current_state = new_state
        self.current_state.enter()


class StateOne:
    def __init__(self, fsm):
        self.count = 5  
        self.fsm = fsm
        self.next_state = None

    def enter(self):
        print("Entering State of %s" % self.__class__)

    def exit(self):
        print("Exiting State of %s" % self.__class__)

    def update(self):
        print("Hello from %s!" % self.__class__.__name__)
        self.count -= 1
        if (self.count == 0):
            fsm.change_state(self.next_state)

class StateTwo:
    def __init__(self, fsm):
        self.count = 5  
        self.fsm = fsm
        self.next_state = None

    def enter(self):
        print("Entering State of %s" % self.__class__)

    def exit(self):
        print("Exiting State of %s" % self.__class__)

    def update(self):
        print("Hello from %s!" % self.__class__.__name__)
        self.count -= 1
        if (self.count == 0):
            fsm.change_state(self.next_state)

class StateQuit:
    def __init__(self, fsm):
        self.fsm = fsm

    def enter(self):
        print("Entering Quit")

    def exit(self):
        print("Exiting Quit")

    def update(self):
        print("Quiting...")
        exit()


if __name__ == "__main__":
    fsm = FsmManager()
    state_one = StateOne(fsm)
    state_two = StateTwo(fsm)
    state_quit = StateQuit(fsm)

    state_one.next_state = state_two
    state_two.next_state = state_quit

    fsm.change_state(state_one)

    while True:
        fsm.update()