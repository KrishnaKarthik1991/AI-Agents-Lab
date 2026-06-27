class Agent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, I am {self.name}"
agent1 = Agent("Krishna")
print(agent1.greet())