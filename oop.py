import json

class ChapterManager:
    
    def __init__(self):
        self.chapters = []

    def loadChapters(self):
        global chapters
        with open("cd_data.json") as data_file:
            chapters = json.load(data_file)
            for key in chapters:
                tmpChapter = Chapter(key, [])

                for cat in chapters[key]:
                    tmpChapter.addCategory(cat, chapters[key][cat])

                self.chapters.append(tmpChapter)

    def printAllChapters(self):
        print("here are the available chapters")
        for chapter in self.chapters:
            chapter.display()

    def returnChapter(self, name):
        print("here are the available chapters")
        for key in self.chapters:
            if (key == name):
                chapter = Chapter(name, [])
        return 0

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

main()
