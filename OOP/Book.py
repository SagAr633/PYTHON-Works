# book name, no of pages, author name
# attributes-the heading of datas that saved in backend of a program

class Book:
    def setvalue(self,name,no_of_pages,author_name):
        self.name=name
        self.no_of_pages=no_of_pages
        self.author_name=author_name
    def printvalue(self):
        print(self.name,self.no_of_pages,self.author_name)
book1=Book()
book1.setvalue('God_Father',678,'Mario_Pulzo')
book1.printvalue()