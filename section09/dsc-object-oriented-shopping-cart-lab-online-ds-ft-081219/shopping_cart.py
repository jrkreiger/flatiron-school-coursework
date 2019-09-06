class ShoppingCart:
    # write your code here
    def __init__(self, total=0, employee_discount=None, items=[]):
        self.total = total
        self.employee_discount = employee_discount
        self.items = items
        
    def add_item(self, name, price, quantity=1):
        for i in range(0, quantity):
            self.items.append({'name':name, 'price':price})
        self.total = self.total + (price*quantity)
        return self.total
    
    def mean_item_price(self):
        return round(self.total / len(self.items), 2)

    def median_item_price(self):
        prices = [i['price'] for i in self.items]
        prices = sorted(prices)
        if len(prices) % 2 == 1:
            return prices[len(prices)//2]
        else:
            middle_1 = prices[len(prices)//2]
            middle_2 = prices[len(prices)//2-1]
            return round((middle_1 + middle_2) / 2, 2)

    def apply_discount(self):
        if self.employee_discount == None:
            return "Sorry, there is no discount to apply to your cart :("
        else:
            new_total = self.total - self.total * (self.employee_discount/100)
            return  new_total

    def void_last_item(self):
        if len(self.items) == 0:
            return "There are no items in your cart!"
        else: 
            item_to_remove = self.items.pop()
            self.total -= item_to_remove['price']
            return self.total