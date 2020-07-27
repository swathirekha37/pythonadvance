class Book:

    def __init__(self,title,author):
        self.title=title
        self.author=author

    def __str__(self):
        return "{} by {}".format(self.title,self.author)

class BookCase:
    def __init__(self,books=None):
        self.books=books

    @classmethod
    def create_Booklist(cls,booklist):
        books=[]
        for title,author in booklist:
            books.append(Book(title,author))
        return cls(books)

#to access:

"""
bc=BookCase.create_Booklist([('The Lord of Rings','xyz'),('Life of pi','jkl')])
print(bc)
print(bc.books)
print(str(bc.books[0]))"""
