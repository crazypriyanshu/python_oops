# create a basic class
class Book:
    def __init__(self, title, autor, pages, price):
        self.title = title
        self.autor = autor
        self.pages = pages
        self.price = price
        self.__secret = "This is a secret string"
    def getPrice(self):
        if hasattr(self, 'discount'):
            return self.price - (self.price * self.discount)
        else:
            return self.price

    def setDiscount(self, amount):
        self.discount = amount



# instance of class
book1 = Book("Brave world ", "Leo Tostoy", 255, 40.5)
book2 = Book("Do things automatically ", "Gomal Tol", 25, 0.5)
print(book1.title)
print(book2)
print(book1.getPrice())
book1.setDiscount(0.25)
print(book1.getPrice())
print(book1._Book__secret)

print(type(book1)) # gives the type of method or class