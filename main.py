
class Library:

    def __init__(self, books):
        self.books = books

    def availableBooks(self):
        print('!!! Books In The Library are : !!!')
        for book in self.books:
            print(f'   ---{book}')

    def issueBook(self, bookName):
        if bookName in self.books:
            print(f'You Have Issued {bookName}')
            cart.append(bookName)
            self.books.remove(bookName)
        else:
            print('This Book is Not Available Right Now')

    def returnBook(self, bookName):
        if bookName in cart:
            print(f'You Have Returned {bookName}')
            self.books.append(bookName)
            cart.remove(bookName)
        else:
            print('No Such Book Found In Your Cart')


class Student(Library):

    def myCart(self):
        if len(cart) != 0:
            print(f'Issued Books : {cart}')
        else:
            print('Your cart is empty')


cart = []

if __name__ == '__main__':
    centralLib = Library(['Harry Potter', 'Flat Standley', 'Curious George',
                         'Calculus For Beginners', 'World Records 2017', 'Spider Man Comics III', 'Indiana Jones'])
    student1 = Student()

    while True:
        welcome_msg = '''
        ====== Welcome To The Library Portal=====
        press 1. to get list of available books
        press 2. to view your issued books
        press 3. to issue a book
        press 4. to return a book
        press 5. to exit
        '''
        print(welcome_msg)
        try:
            cmd = int(input(': '))
        except:
            print('Enter a valid response')
            continue

        if cmd == 1:
            centralLib.availableBooks()
        elif cmd == 2:
            student1.myCart()
        elif cmd == 3:
            try:
                isbook = input(
                    'Write The Name Of The Book You Would Like To Issue : ')
                centralLib.issueBook(isbook)
            except Exception as e:
                print(f'Please enter a valid book : {e}')
        elif cmd == 4:
            try:
                centralLib.returnBook(
                    input('Write The Name Of The Book You Would Like To Return : '))
            except:
                print('No Such Book Found In The Cart')
        elif cmd == 5:
            break
        else:
            print('Enter a valid response')
