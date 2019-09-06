class Chapter:

    def __init__(self):
        self.definitions = []
        self.theorems = []
        self. laws = []
        self.exercises = []
        self.rules = []

    def addRule(self, rule):
        self.rules.append(rule)

class Definition:

    def __init__(self, name, discription):
        self.name = name
        self.discription = discription

class Theorems:

    def __init__(self, name, discription, proof):
        self.name = name
        self.discription = discription
        self.proof = proof

class Laws:

    def __init__(self, name, discription):
        self.name = name
        self.discription = discription

class Exercises:

    def __init__(self, name, discription, solution):
        self.name = name
        self.discription = discription
        self.solution = solution


class Rule:

    def __init__(self, name, discription):
        self.name = name
        self.discription = discription


chapter1 = Chapter()
r1 = Rule("asdad", "sasdasd")
chapter1.addRule(r1)

