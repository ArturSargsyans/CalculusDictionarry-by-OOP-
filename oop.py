import json

class Chapter:
    def __init__(self, name):
        self.name = name
        self.categories = {}

    def ChooseCategory(self):
        for category in self.categories:
            print(category)
        chosencat = input("Choose the category")
        return chosencat

    @staticmethod
    def LoadChapters():
        global chapters
        with open("cd_data.json") as data_file:
            chapters = json.load(data_file)
        return chapters

    @staticmethod
    def ChooseTheChapter():
        print("here are the available chapters")
        chapters = Chapter.LoadChapters()
        for key in chapters:
            print(key)
        nameofchap = input("choose the chapter you want")
        return nameofchap




class Category:

    def __init__(self, type):
        self.type = type
        self.listofstatements = {}

    def ChooseAstatement(self):
        for statement in self.listofstatements:
            print(statement)
        chosenstate = input("Choose among these")
        return chosenstate

def main():
    name = Chapter.ChooseTheChapter()
    currentchapter = Chapter(name)
    print(currentchapter)


main()
