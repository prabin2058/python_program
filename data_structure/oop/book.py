class Book:
    def __init__(self, title="", author="", dates=""):
        self.title = title
        self.author = author
        self.date = dates

obj = Book()
obj.title = "Ram"
obj.author = "Prabin Karki"
obj.date = "2025-04-30"

print(obj.title)
print(obj.author)
print(obj.date)



