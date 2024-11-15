from dessert import(
    DessertItem,
    Candy,
    Cookie,
    IceCream,
    Sundae
)
from receipt import make_receipt

class Order():
    def __init__(self):
        self.order = []

    def __str__(self):
        string = ""
        for value in self.order:
            string += value.name + "\n"

        return string
    
    def __len__(self):
        return len(self.order)
    
    def add(self, DessertItem):
        self.order.append(DessertItem)
    
    def order_cost(self):
        total = 0
        for item in self.order:
            total += item.calculate_cost()
        return total
    
    def order_tax(self):
        tax = 0
        for item in self.order:
            tax += item.calculate_tax()
        return tax

def main():
    listed = []
    sub_total = 0
    tax = 0
    order = Order()
    order.add(Candy("Candy Corn", 1.5, .25))
    order.add(Candy("Gummy Bears", .25, .35))
    order.add(Cookie("Chocolate Chip", 6, 3.99))
    order.add(IceCream("Pistachio", 2, .79))
    order.add(Sundae("Vanilla", 3, .69, "Hot Fudge", 1.29))
    order.add(Cookie("Oatmeal Raisin", 2, 3.45))

    print(order, end = "")
    print("Total number of items in order:", len(order))

    for item in order.order:
        listed.append([item.name, round(item.calculate_cost(), 2), round(item.calculate_tax(), 2)])
        sub_total += item.calculate_cost()
        tax += item.calculate_tax()

    total_cost = sub_total + tax
    total_number_of_items_in_the_order = len(order)

    listed.append(["Order Subtotals: ", round(sub_total, 2), round(tax, 2)])
    listed.append(["Order Total:", "", round(total_cost, 2)])
    listed.append(["Total items in the order: ","", total_number_of_items_in_the_order])

    make_receipt(listed, "receipt")

main()