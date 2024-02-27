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

    def get_cost(self):
        """asdfjkl; """
        return self.price / self.weight

def knapsack(amount, i_list):
    """akio toma"""
    r_w = 0
    r_p = 0
    s_item_list = sorted(i_list, key=lambda x: x.get_cost(), reverse=True)
    print("Knapsack Size: %.1f kg"  % (amount))
    print("===============================")
    for i in s_item_list:
        if r_w + i.get_weight() <= amount:
            r_w += i.get_weight()
            r_p += i.get_price()
            print(i.get_name() + " -> " + str(i.get_weight()) + " kg -> " + \
                   str(i.get_price()) + " THB")
        else:
            break
    print("Total: %d THB" % int(r_p))


def main():
    """bro"""
    import json
    items = []
    num_items = int(input())
    while num_items != 0:
        item_in = json.loads(input())
        items.append(
            Item(item_in['name'], item_in['price'], item_in['weight']))
        num_items = num_items - 1
    knapsack_capacity = float(input())
    knapsack(knapsack_capacity, items)

main()
