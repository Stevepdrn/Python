class Business:
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises


class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    def __repr__(self):
        return self.address  # self.menus?

    def available_menus(self, time):
        available = []
        for menu in self.menus:
            if time >= menu.start_time and time <= menu.end_time:
                available.append(menu)
        return available


class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

# Give Menu class a string representation method that will tell the name of the menu and when is available.
    def __repr__(self):
        return f"{self.name} menu is available from {self.start_time} to {self.end_time}"


# Give Menu a method that returns the total price of a purchase consisiting of all the items in purchased_items.


    def calculate_bill(self, purchased_items):
        total = 0
        for item in purchased_items:
            if item in self.items:
                # NOTICE loop over dictionary (array?)
                total += self.items[item]
            else:
                print(item, "- item not on menu")
        return f"Total: {total}"


""" brunch menu """
brunch_items = {
    'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}

brunch = Menu("Brunch", brunch_items, 11, 16)
# print(brunch)
print(brunch.calculate_bill(
    ['pancakes', 'home fries', 'coffee', 'ceaser salad']))


""" early birds menu """
early_bird_items = {
    'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}

early_birds = Menu("Early Birds", early_bird_items, 15, 18)
# NOTE: Below, prints what saved in the string representation for Menu class!!!
print(early_birds)
print(early_birds.calculate_bill(
    ['salumeria plate', 'mushroom ravioli (vegan)']))


""" dinner menu """
dinner_items = {
    'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}

dinner = Menu("Dinner", dinner_items, 17, 23)


""" kids menu """
kids_items = {
    'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}

kids = Menu("Kids", kids_items, 11, 21)
# print(kids.start_time, kids.end_time)


menus = [brunch, early_birds, dinner, kids]

flagship_store = Franchise("1232 West End Road", menus)
# NOTE Below, without the string representation in Franchise class I would get the obj location in memory for the address
print(flagship_store)

new_installment = Franchise("12 East Mulberry Street", menus)
print(new_installment)
# print(menus)

# test out our .available_menus() method! Call it with 12 noon as an argument and print out the results.
print(new_installment.available_menus(17))


""" 1st business """

first_business = Business("Basta Fazoolin' with my Heart", [
                          flagship_store, new_installment])


""" Arepa """

arepas_items = {
    'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}

arepas_menu = Menu("Take a' Arepa", arepas_items, 1000, 2000)
arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])


""" New Business """

new_business = Business("Take a' Arepa", [arepas_place])

print(new_business.franchises[0].menus[0])
