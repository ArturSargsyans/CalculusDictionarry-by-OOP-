import json

class LinkedList():
    def __init__(self):
        self.head = None

    def add(self, node):
        if self.head == None:
            self.head = node
        else:
            tmp = self.head
            while tmp.next != None:
                tmp = tmp.next

            tmp.next = node

    def _display(self, currhead):
        if currhead != None:
            print("\n", currhead.name)
            if currhead.next != None:
                self._display(currhead.next)
            else:
                return

    def display(self):
        self._display(self.head)

    def find(self, nodename):
        tmp = self.head
        while tmp != None:
            if tmp.name == nodename:
                return tmp
            tmp = tmp.next

        return None

class Chapter:

    def __init__(self, name, categories):
        self.name = name
        self.categories = categories
        self.next = None

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
        self.chapters = LinkedList()
        self.chosenchapter = []
        self.chosencategory = None


    def loadChapters(self):
        with open("cd_data.json") as data_file:
            chapters = json.load(data_file)
            for key in chapters:
                tmpChapter = Chapter(key, [])

                for cat in chapters[key]:
                    tmpChapter.addCategory(cat, chapters[key][cat])

                self.chapters.add(tmpChapter)

    def Introduction(self):
        print("Hello, welcome to Calculus Dictionary.\n\nHere you can learn, and review calculus matterial in an easy way")
        if input("\nType 'go' to start working. Type 'exit' to exit") == 'exit':
            quit()
        else:
            return True

    def printAllChapters(self):
        print("\nHere are the available chapters")
        self.chapters.display()

    def printAllCategories(self):
        print("\nHere are the categories")
        for category in self.chosenchapter:
            print("\n", "***", category.name, "***")


    def ChooseChapter(self):
        while True:
            chaptername = input("\nPlease enter the name of the chapter you want. Type 'exit' to exit")
            if chaptername == 'exit':
                quit()
            else:
                self.chosenchapter = self.chapters.find(chaptername).categories
                break

    def ChooseCategory(self):
            while True:
                categoryname = input("\nEnter the name of the category, type exit to exit")
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
        nameofStatement = input("\nWrite the name of the" + self.chosencategory.name + "that you want. If you want to exit type 'exit'")
        if nameofStatement == 'exit':
            quit()
        for statement in self.chosencategory.statements:
            if nameofStatement == statement:
                print("\n", self.chosencategory.statements[statement])
                while True:
                    contorquit = input("\n\ntype 'continue' to go back to chapters. Type 'exit' to exit")
                    if contorquit == 'continue':
                        return True
                    elif contorquit == 'exit':
                        quit()
                    else:
                        print("\npleas follow the instructions")



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
