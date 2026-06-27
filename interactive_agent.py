class AIAgent:
    def __init__(self, name, goal):
        self.name = name
        self.goal = goal
    def think(self):
        print(self.name,"is thinking...")
    def act(self):
        print(self.name,"is working on:",self.goal)
name = input("Enter your name: ")
goal = input("Enter your goal: ")
agent = AIAgent(name, goal)
agent.think()
agent.act()