
"""item_class"""
class Item:
    """toma toma"""
    def __init__(self, name, price, weight):
        """alo"""
        self.name = name
        self.price = price
        self.weight = weight
 
    def get_name(self):
        """asdfjkl; """
        return self.name
 
    def get_price(self):
        """asdfjkl; """
        return self.price
 
    def get_weight(self):
        """asdfjkl; """
        return self.weight
 
def main():
    """asd"""
    import json
    item_in = json.loads(input())
    item = Item(item_in["name"], item_in["price"], item_in["weight"])
    print(item.get_name(), item.get_price(), item.get_weight(), sep='\n')
 
main()
