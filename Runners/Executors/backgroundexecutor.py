class Backgroundexec:
    def __init__(self, q_module):
        self.q_module = q_module

    def imagine_queue(self):
        total = []
        while not self.q_module.empty():
            total.append(self.q_module.get())
        return total

