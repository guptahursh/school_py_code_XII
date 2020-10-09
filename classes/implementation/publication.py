class Publication:

    def getdata(self):
        self.title = input('enter title:')
        self.price = float(input('enter price:'))

    def putdata(self):
        print('Title:',self.title,'\nPrice:',self.price)

class Book(Publication):

    def getdata(self):
        super().getdata()
        self.page_count = int(input("enter no. of pages: "))

    def putdata(self):
        super().putdata()
        print('No. of Pages:',self.page_count)


class Cassette(Publication):

    def getdata(self):
        super().getdata()
        self.playing_time = float(input("enter playing time(in minutes): "))

    def putdata(self):
        super().putdata()
        print('Playing Time:',self.playing_time)


b = Book()
b.getdata()
