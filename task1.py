class Store :





class User :
    def __init__(self, bag,card ) :
        self.bag = bag
        self.card = card

    def sayHello(self) :
        print(str(self,"Hello from user!"))


class Product :
    def __init__(self, price, label ) :
        self.price = price
        self.label = label



class Cart :
    def __init__(self, sum_product) :



class Admin(User) :
    def __init__(self, bag, money, cash, wallet, card) :
        super.__init__(self, bag, money, cash, wallet, card)





        
    