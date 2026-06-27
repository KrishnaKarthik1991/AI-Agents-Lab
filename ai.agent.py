class AIAgent:
    def __init__(self, name, goal):
        self.name = name
        self.goal = goal

    def think(self):
        print(self.name,"is thinking...")
    def act(self):
        print(self.name,"is working on:",self.goal)
agent = AIAgent("Krishna","Build an AI Agent")
agent.think()
agent.act()