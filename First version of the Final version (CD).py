import json


class ChapterManager:

    def __init__(self):
        self.chapters = []
        self.chosenchapter = []
        self.chosencategory = []


    def loadChapters(self):
        with open("cd_data.json") as data_file:
            chapters = json.load(data_file)
            for key in chapters:
                tmpChapter = Chapter(key)

                for cat in chapters[key]:
                    tmpChapter.addCategory(cat, chapters[key][cat])

                self.chapters.append(tmpChapter)

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
            for chapter in self.chapters:
                if chaptername == chapter.name:
                    self.chosenchapter = chapter.categories
                    x = 2
                    break





    def ChooseCategory(self):
        while True:
            x = 1
            while x ==1:
                categoryname = input("Enter the name of the category, type exit to exit")
                for key in self.chosenchapter:
                    if categoryname == key.name:
                        self.chosencategory.append(key)
                        x = 2
                        print(self.chosencategory)
                        break
                    elif chaptername == "exit":
                        quit()

class Chapter:

    def __init__(self, name, categories=[]):
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

    def __init__(self, name, statements={}):
        self.name = name
        self.statements = statements

    def display(self):
        print("**************", self.name, "******************")
        for key in self.statements:
            print(key, ":", self.statements[key])


def main():
    myCalculusDictionary = ChapterManager()
    myCalculusDictionary.loadChapters()
    myCalculusDictionary.printAllChapters()
    myCalculusDictionary.ChooseChapter()
    myCalculusDictionary.printAllCategories()
    myCalculusDictionary.ChooseCategory()

main()

# def returnChapter(self, name):
#     print("here are the available chapters")
#     for key in self.chapters:
#         if (key == name):
#             chapter = Chapter(name)
#     return 0