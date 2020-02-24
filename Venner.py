""" Veneer """


class Art:
    def __init__(self, artist, title, medium, year, owner):
        self.artist = artist
        self.title = title
        self.medium = medium
        self.year = year
        self.owner = owner

    def __repr__(self):
        return f"{self.artist}. {self.title}. {self.year}, {self.medium}. {self.owner.name}, {self.owner.location}."

# girl_with_mandolin = Art("Picasso, Pablo", "\"Girl with a Mandolin (Fanny Tellier)\"", "oil on canvas", "1910")

# print(girl_with_mandolin)


class Marketplace:
    def __init__(self):
        self.listings = []
        self.sold = []
        self.veneer_wallet = []

    def add_listing(self, new_listing):
        self.listings.append(new_listing)

    def remove_listing(self, expired_listing):
        self.listings.remove(expired_listing)
        self.sold.append(expired_listing)

    # def sold_listing(self, removed_listing):  # check if needed
    # self.sold.append(removed_listing)

    def show_listings(self):

        for listing in self.listings:
            print("New Listing:", listing)

    def commission(self, new_commission):
        self.veneer_wallet.append(new_commission)

    def __repr__(self):
        return f"Listings: {self.listings}.\nSold: {self.sold}.\nCommissions (USD $): {self.veneer_wallet}"


# veneer = Marketplace()  # Moved below!
# veneer.show_listings()


class Client:
    def __init__(self, name, wallet, location, is_museum):
        self.name = name
        self.wallet = wallet
        self.is_museum = is_museum

        if is_museum:
            self.location = location
        else:
            self.location = "Private Collection"

    def __repr__(self):
        return f"{self.name}: ${self.wallet} (USD)"

    def sell_artwork(self, artwork, price):

        if artwork.owner == self:  # self refers to this particular client 'calling' sell_artwork
            # create a variable (new_listing) we can add to the veneer obj instantiated using the class Marketplace()
            new_listing = Listing(artwork, price, self)

            # now we can use .add_listing method of Marketplace() to add new_listing
            veneer.add_listing(new_listing)

        if artwork.owner != self:
            self.wallet += price - (price * 0.03)  # price minus commission
            veneer.commission(price * 0.03)

    def buy_artwork(self, artwork, price):

        if artwork.owner != self:
            art_listing = None  # new variable set to None so if it doesn't get changed from the iterate over veneer.listings the art isn't for sale and can't be bought!!
            for listing in veneer.listings:  # see line 22
                if listing.art == artwork:
                    art_listing = listing
                    break  # if we had a lot of items 'break' here will stop searching as soon as it finds a match
        if art_listing != None:  # this change the ownership of the item in art_listing then removes the item from veneer
            art_listing.art.owner = self
            veneer.remove_listing(art_listing)
            self.wallet -= price


class Listing:
    def __init__(self, art, price, seller):
        self.art = art
        self.price = price
        self.seller = seller

    def __repr__(self):
        return f"{self.art.title} \nPrice: ${self.price} (USD)"


veneer = Marketplace()


# # sellers client
edytta = Client("Edytta Halpirt", 1, None, False)
marcus = Client("Marcus Gonzo", 20, None, False)


print("Description art for sale: \n")
girl_with_mandolin = Art(
    "Picasso, Pablo", "\"Girl with a Mandolin (Fanny Tellier)\"", "oil on canvas", "1910", edytta)

dogs_play_poker = Art("Teomondo, Scrofalo",
                      "\"Dogs Bluffing\"", "oil on canvas", "1974", marcus)

print(girl_with_mandolin)
print()
print(dogs_play_poker)
print("\n \n")

print("Name of the seller and balance: \n")
print(edytta)
print(marcus)
print("\n \n")

# # use the .sell_artwork created in Client() class
print("Listing and price asked: \n")
edytta.sell_artwork(girl_with_mandolin, 6000000)
marcus.sell_artwork(dogs_play_poker, 300000)
veneer.show_listings()
print("\n \n")

print("Veneer Marketplace: \n")
print(veneer)
print()

# # buyer clients
moma = Client("MOMA", 10000000, "New York", True)

# # buyer-seller transaction

moma.buy_artwork(girl_with_mandolin, 6000000), edytta.sell_artwork(
    girl_with_mandolin, 6000000)  # only if called again after buy then .sell_artwork adds money to the seller!

moma.buy_artwork(dogs_play_poker, 300000), marcus.sell_artwork(
    dogs_play_poker, 300000)

print("New Description art and owner: \n")
print(girl_with_mandolin)
print("\n \n")
print(dogs_play_poker)
print("\n \n")
# # show balance after transaction
print(edytta)
print(marcus)
print(moma)
print("\n \n")

veneer.show_listings()
# # since we sold what was in the veneer marketplace to MOMA this list is now empty again

print("Veneer Marketplace: \n")
print(veneer)
