class AIAgent:
    def __init__(self, name):
        self.name = name

    def save_goal(self, goal):
        with open("memory.txt", "w") as file:
            file.write(goal)
    def load_goal(self):
        try:
            with open("memory.txt", "r") as file:
                return file.read()
        except FileNotFoundError:
            print("File not found.")
            return "No goal found."
name = input("Enter your name: ")
agent = AIAgent(name)
goal = input("Enter your goal: ")
agent.save_goal(goal)
print("Hello,",name)
print("Your goal is:",agent.load_goal())