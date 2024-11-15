from dessert import(
    DessertItem,
    Candy,
    Cookie,
    IceCream,
    Sundae
)

def test_DessertItem():
    item1 = DessertItem("Pie")
    item2 = DessertItem("Cake")
    item3 = DessertItem("Cakepop")
    assert item1.name == "Pie"
    assert item2.name == "Cake"
    assert item3.name == "Cakepop"

def test_Candy():
    item1 = Candy("Lollipop", 4.5, 2.00)
    item2 = Candy("Slurpables", 1.0, 2.0)
    item3 = Candy("Skittles", 2.4, 3.00)
    assert item1.name == "Lollipop"
    assert item2.candy_weight == 1.0
    assert item3.price_per_pound == 3.00

def test_Cookie():
    item1 = Cookie("Chocolate chip cookies", 4, 2.45)
    item2 = Cookie("Blondie bites", 10, 2.01)
    item3 = Cookie("Lemon cookies", 7, 3.00)
    assert item1.name == "Chocolate chip cookies"
    assert item2.quantity == 10
    assert item3.price_per_dozen == 3.00
    
def test_IceCream():
    item1 = IceCream("Vanilla", 4, 2.00)
    item2 = IceCream("Chocolate", 2, 1.00)
    item3 = IceCream("Mint", 5, 2.49)
    assert item1.name == "Vanilla"
    assert item2.scoop_count == 2
    assert item3.price_per_scoop == 2.49


def test_Sundae():
    item1 = Sundae("Vanilla", 3, 2.00, "Sprinkles", 1.00)
    item2 = Sundae("Chocolate", 4, 1.00, "Chocolate chips", 0.45)
    item3 = Sundae("Mint", 1, 2.49, "Cherry", 3.00)
    assert item1.name == "Vanilla"
    assert item2.scoop_count == 4
    assert item2.price_per_scoop == 1.00
    assert item3.topping_name == "Cherry"
    assert item3.topping_price == 3.00