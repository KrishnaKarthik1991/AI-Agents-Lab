class ProductManager:
    def __init__(self, feature):
        self.feature = feature

    def prioritize(self):
        if self.feature == "Voice":
            return "Critical"
        elif self.feature == "Payments":
            return "High"
        elif self.feature == "login":
            return "Medium"
        else:
            return "Low"
feature = input("Enter a feature: ")
manager = ProductManager(feature)
priority = manager.prioritize()
print("Feature:", feature)
print("Priority:", priority) 