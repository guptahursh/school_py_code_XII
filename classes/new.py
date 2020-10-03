class x:
    def __init__(self):
        self.a = 10
        self.b = 20
    def hello(self):
        print(self.a,self.b)
    def __call__(self):
        print('its an object yo')

x = x()
