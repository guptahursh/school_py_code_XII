from datetime import datetime
class Bill:
    def __init__(self,*args):
        self._bill_no = datetime.now().strftime("%D|%H:%M:%S")
        self.New_Bill()
        return_amount = self.generate_amount() * self._bill_period 
        if self._payment_mode == 'online':
            self.amount = return_amount * 0.95
        else:
            self.amount = return_amount

    def __repr__(self):
        return str(self._bill_no)

    def show_details(self):
        print("\nBill no.:",self._bill_no)
        print("Bill period:",self._bill_period,'months')
        print("No. of calls:",self._no_of_calls)
        print("Payment Mode:",self._payment_mode)
        print("---------------------------------")
        if self._payment_mode == 'online':
            print("AMOUNT:",self.amount,'(with 5% off)')
        else:
            print("AMOUNT:",self.amount)

    def New_Bill(self):
        self._bill_period = int(input("Enter time in months: "))
        self._no_of_calls = int(input('Enter number of calls: '))
        self._payment_mode = input("Enter payment mode (online/offline): ")

    def generate_amount(self):
        _x = self._no_of_calls
        if _x > 1200:
            return (_x-1200) * 4.0 + 1900
        if 501 <= _x <= 1200:
            return ((_x-500) * 2.0) + 500
        if _x <= 500:
            return _x * 1.0

b = Bill()
b.show_details()


