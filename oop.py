import json

class Chapter:
    def __init__(self, name):
        self.name = name
        self.categories = chapters[name]

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

    def __init__(self, type, chapter):
        self.type = type
        self.listofstatements = chapter[type]


    def ChooseAstatement(self):
        for statement in self.listofstatements:
            print(statement)
        chosenstateName = input("Choose among these")
        chosenstate = self.listofstatements[chosenstateName]
        print(chosenstate)

def main():
    name = Chapter.ChooseTheChapter()
    currentchapter = Chapter(name)
    currcattype= Chapter.ChooseCategory(currentchapter)
    currcat = Category(currcattype, currentchapter.categories)
    Category.ChooseAstatement(currcat)

main()
