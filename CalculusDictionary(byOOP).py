import json

class Chapter:

    chapters = None
    def __init__(self, name):
        self.name = name
        self.categories = Chapter.chapters[name]

    def ChooseCategory(self):
        for category in self.categories:
            print("\n", category)
        while True:
            chosencat = input("\nChoose the category. To go back type back. Type 'exit' to exit")
            if chosencat == "back":
                return False
            elif chosencat == 'exit':
                quit()
            elif chosencat in self.categories:
                return chosencat
            else:
                print("there is no such category")

    @classmethod
    def LoadChapters(cls):
        with open("cd_data.json") as data_file:
            cls.chapters = json.load(data_file)
        return cls.chapters

    @staticmethod
    def ChooseTheChapter():
        print("Here are the available chapters\n")
        chapters = Chapter.LoadChapters()
        for key in chapters:
            print(key)
        while True:
            nameofchap = input("Enter the name of the chapter that you want to study. \n Type 'exit' to exit")
            if nameofchap in chapters:
                return nameofchap
            elif nameofchap == "exit":
                quit()
            else:
                print("There is no such chapter")


class Category:

    def __init__(self, type, chapter):
        self.type = type
        self.listofstatements = chapter[type]

    def ChooseAstatement(self):
        for statement in self.listofstatements:
            print(statement)
        while True:
            chosenstateName = input("\nChoose among these. If you want to go back type 'back', type 'exit' to exit")
            if chosenstateName == 'back':
                return False
            elif chosenstateName == 'exit':
                quit()
            elif chosenstateName in self.listofstatements:
                chosenstate = self.listofstatements[chosenstateName]
                return chosenstate
            else:
                print("There is no such thing available")

def main():
    print("Hello! Welcome to Calculus Dictionary\n")
    while True:
        name = Chapter.ChooseTheChapter()
        currentchapter = Chapter(name)
        while True:
            currcattype = Chapter.ChooseCategory(currentchapter)
            if currcattype == False:
                break
            currcat = Category(currcattype, currentchapter.categories)
            while True:
                chosenstate = Category.ChooseAstatement(currcat)
                if chosenstate == False:
                    break
                else:
                    print("\n", chosenstate, "\n")
                    while True:
                        if input("type 'back' to go back") == "back":
                            break
                        else:
                            print("follow the instructions")

main()