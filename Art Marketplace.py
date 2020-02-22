

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

    def add_listing(self, new_listing):
        self.listings.append(new_listing)

    def remove_listing(self, expired_listing):
        self.listings.remove(expired_listing)

    def show_listings(self):

        for listing in self.listings:
            print(listing)


# veneer = Marketplace()  # Moved below!
# veneer.show_listings()


class Client:
    def __init__(self, name, location, is_museum):
        self.name = name
        self.is_museum = is_museum

        if is_museum:
            self.location = location
        else:
            self.location = "Private Collection"

    def sell_artwork(self, artwork, price):

        if artwork.owner == self:  # self refers to this particular client 'calling' sell_artwork
            # create a variable (new_listing) we can add to the veneer obj instantiated using the class Marketplace()
            new_listing = Listing(artwork, price, self)
            # now we can use .add_listing method of Marketplace() to add new_listing
            veneer.add_listing(new_listing)

    def buy_artwork(self, artwork):

        if artwork.owner != self:
            art_listing = None  # new variable set to None so if it doesn't get changed from the iterate over veneer.listings the art isn't for sale and can't be bought!!
            for listing in veneer.listings:  # see line 22
                if listing.art == artwork:
                    art_listing = listing
                    break  # if we had a lot of items 'break' here will stop searching as soon as it finds a match
        if art_listing != None:  # this change the ownership of the item in art_listing then removes the item from veneer
            art_listing.art.owner = self
            veneer.remove_listing(art_listing)


class Listing:
    def __init__(self, art, price, seller):
        self.art = art
        self.price = price
        self.seller = seller

    def __repr__(self):
        return f"{self.art.title}, {self.price}"


veneer = Marketplace()


# first client
edytta = Client("Edytta Halpirt", None, False)

girl_with_mandolin = Art(
    "Picasso, Pablo", "\"Girl with a Mandolin (Fanny Tellier)\"", "oil on canvas", "1910", edytta)
print(girl_with_mandolin)

# use the .sell_artwork created in Client() class
edytta.sell_artwork(girl_with_mandolin, "$6M (USD).")
veneer.show_listings()

# second client
moma = Client("MOMA", "New York", True)

# buyer
moma.buy_artwork(girl_with_mandolin)
print(girl_with_mandolin)


veneer.show_listings()
# since we sold what was in the veneer marketplace to MOMA this list is now empty again
