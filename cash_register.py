class CashRegister():
    """
    Write a Python class that allows us to track item count and total amount in cash register. The class
    should allow 1) add item and price to cash register, 2) check total money and item in cash register.


    """

    def __init__(self):
        self.item_and_price = {}

    def add_item(self, denomination, count):
        if denomination in self.item_and_price:
            prev_count = self.item_and_price[denomination]
        else:
            prev_count = 0
        self.item_and_price[denomination] = prev_count + count

    def pop_item(self, denomination, count):
        if denomination in self.item_and_price:
            prev_count = self.item_and_price[denomination]
        else:
            prev_count = 0
        self.item_and_price[denomination] = prev_count - count

    def get_total_money(self):
        print(self.item_and_price)
        total_money = 0
        for key in self.item_and_price:
            total_money += key * self.item_and_price[key]
        return total_money
