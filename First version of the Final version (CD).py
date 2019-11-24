import json

class Chapter:

    def __init__(self, name, categories):
        self.name = name
        self.categories = categories

    def addCategory(self, name, data):
        tmpCat = Category(name, data)
        self.categories.append(tmpCat)

    def display(self):
        print(self.name, "\n", "-----")
        for cat in self.categories:
            cat.display()


class Category:

    def __init__(self, name, statements):
        self.name = name
        self.statements = statements

    def displayStatements(self):
        print("**************", self.name, "******************")
        for key in self.statements:
            print(key)



class ChapterManager:

    def __init__(self):
        self.chapters = []
        self.chosenchapter = []
        self.chosencategory = None


    def loadChapters(self):
        with open("cd_data.json") as data_file:
            chapters = json.load(data_file)
            for key in chapters:
                tmpChapter = Chapter(key, [])

                for cat in chapters[key]:
                    tmpChapter.addCategory(cat, chapters[key][cat])

                self.chapters.append(tmpChapter)

    def Introduction(self):
        print("Hello, welcome to Calculus Dictionary.\n\nHere you can learn, and review calculus matterial in an easy way")
        if input("type 'go' to start working. Type 'exit' to exit") == 'exit':
            quit()
        else:
            return True

    def printAllChapters(self):
        print("Here are the available chapters")
        for chapter in self.chapters:
            print("\n", "***", chapter.name, "***")

    def printAllCategories(self):
        print("here are the categories")
        for category in self.chosenchapter:
            print("\n", "***", category.name, "***")


    def ChooseChapter(self):
        x = 1
        while x == 1:
            chaptername = input("\nPlease enter the name of the chapter you want. Type 'exit' to exit")
            if chaptername == 'exit':
                quit()
            for chapter in self.chapters:
                if chaptername == chapter.name:
                    self.chosenchapter = chapter.categories
                    x = 2
                    break

    def ChooseCategory(self):
            while True:
                categoryname = input("Enter the name of the category, type exit to exit")
                if categoryname == "exit":
                    quit()
                else:
                    for key in self.chosenchapter:
                        if categoryname == key.name:
                            self.chosencategory = key
                            return

    def printAllStatements(self):
        self.chosencategory.displayStatements()

    def ChooseStatement(self):
        nameofStatement = input("Write the name of the" + self.chosencategory.name + "that you want. If you want to exit type 'exit'")
        if nameofStatement == 'exit':
            quit()
        for statement in self.chosencategory.statements:
            if nameofStatement == statement:
                print("\n", self.chosencategory.statements[statement])


def main():
    myCalculusDictionary = ChapterManager()
    if myCalculusDictionary.Introduction():
        while True:
            myCalculusDictionary.loadChapters()
            myCalculusDictionary.printAllChapters()
            myCalculusDictionary.ChooseChapter()
            myCalculusDictionary.printAllCategories()
            myCalculusDictionary.ChooseCategory()
            myCalculusDictionary.printAllStatements()
            myCalculusDictionary.ChooseStatement()


main()
