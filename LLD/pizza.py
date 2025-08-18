class PriceBook:
    BASE = {
        'Small':  {'Thin': 6.0,  'Pan': 6.5},
        'Medium': {'Thin': 8.0,  'Pan': 8.5},
        'Large':  {'Thin':10.0,  'Pan':10.5},
    }
    TOPPING = {'Cheese':1.0, 'Pepperoni':1.5, 'Mushroom':1.2, 'Bacon':1.8}
    ITEM = {                                 # << 要求的二级结构
        'Coke':  {'Can': 1.5, 'Bottle': 2.5},
        'Wings': {'6pc': 6.0, '12pc': 11.0},
    }

    def __init__(self, base = None, tp = None, item=None):
        self.base = base or PriceBook.BASE
        self.tp   = tp or PriceBook.TOPPING
        self.it   = item or PriceBook.ITEM
        
    def base_price(self, size, base):
        return self.base[size][base]
    
    def topping_price(self, name):
        return self.tp[name]
        
    def item_price(self, kind, option):   
        return self.it[kind][option]

class Pizza:
    def __init__(self, size, base):
        self.size = size
        self.base = base
        self.topping = []
        
    def add_topping(self, name):
        self.topping.append(name)
        
    def get_toppings(self):
        print("all topping:", self.topping)
        return self.topping
        
    def pricing_repr(self):
        return ('pizza', self.size, self.base, self.get_toppings())

class Item:
    def __init__(self, kind, option):
        self.kind = kind       # 如 'Coke' / 'Wings'
        self.option = option   # 如 'Can' / '12pc'

    # ('item', kind, option)
    def pricing_repr(self):
        return ('item', self.kind, self.option)

class Order:
    def __init__(self):
        self._items = []  # 可混放 Pizza 和 Item
    def add(self, obj):
        self._items.append(obj)
    def items(self):
        return list(self._items)


class OrderCalculator:
    def __init__(self, price_book):
        self.book = price_book
        
    def price_item(self, obj):
        rep = obj.pricing_repr()   # 例如 ('pizza', size, base, [tops...]) 或 ('item', kind, option)
        tag = rep[0]
    
        if tag == 'pizza':
            _, size, base, tops = rep   # 逐个变量解包（不使用星号）
            total = self.book.base_price(size, base)
            for t in tops:
                total += self.book.topping_price(t)
            return round(total, 2)
    
        elif tag == 'item':
            _, kind, option = rep
            return round(self.book.item_price(kind, option), 2)
    
        else:
            raise ValueError("Unknown pricing tag")
    
    def price_order(self, order: Order):
        s = 0.0
        for x in order.items():
            s += self.price_item(x)
        return round(s, 2)

        
    # def calculate_price(self, pizza : Pizza):
    #     payment = 0
    #     base = self.book.base_price(pizza.size, pizza.base)
    #     payment += base 
        
    #     for tps in pizza.get_toppings():
    #         payment += self.book.topping_price(tps) 
        
    #     # print(f"You have to pay $: {payment} dollars")
    #     return payment
            
            
if __name__ == "__main__":
    book = PriceBook()
    calc = OrderCalculator(book)

    # p1 = Pizza('Large', 'Thin')
    # p1.add_topping('Cheese')
    # p1.add_topping('Pepperoni')
    # p1.add_topping('Mushroom')

    # print("Customer 1 should pay:", calc.calculate_price(p1))  # 13.7

    # # 第二位客人
    # p2 = Pizza('Medium', 'Pan')
    # p2.add_topping('Bacon')
    # print("Customer 2 should pay:", calc.calculate_price(p2))  # 10.3
    
    p = Pizza('Large', 'Thin')
    p.add_topping('Cheese')
    p.add_topping('Pepperoni')
    p.add_topping('Mushroom')

    # 额外商品：直接用二级键（kind/option）
    coke  = Item('Coke',  'Bottle')
    wings = Item('Wings', '6pc')

    order = Order()
    order.add(p)
    order.add(coke)
    order.add(wings)

    print(calc.price_item(p))       # 13.7
    print(calc.price_order(order))  # 13.7 + 2.5 + 6.0 = 22.2

        
