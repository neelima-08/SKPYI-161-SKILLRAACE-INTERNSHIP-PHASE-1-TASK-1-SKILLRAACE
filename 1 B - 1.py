class Book:
    def _init_(self, title, author, publisher, price):
        self._title = title
        self._author = author
        self._publisher = publisher
        self._price = price
        self._copies_sold = 0

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        self._author = author

    @property
    def publisher(self):
        return self._publisher

    @publisher.setter
    def publisher(self, publisher):
        self._publisher = publisher

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price

    @property
    def copies_sold(self):
        return self._copies_sold

    @copies_sold.setter
    def copies_sold(self, copies_sold):
        self._copies_sold = copies_sold

    def royalty(self):
        if self._copies_sold <= 500:
            return self._copies_sold * self._price * 0.10
        elif self._copies_sold <= 1500:
            return (500 * self._price * 0.10) + ((self._copies_sold - 500) * self._price * 0.125)
        else:
            return (500 * self._price * 0.10) + (1000 * self._price * 0.125) + ((self._copies_sold - 1500) * self._price * 0.15)


class EBook(Book):
    def _init_(self, title, author, publisher, price, format):
        super()._init_(title, author, publisher, price)
        self._format = format

    @property
    def format(self):
        return self._format

    @format.setter
    def format(self, format):
        self._format = format


    def royalty(self):
        base_royalty = super().royalty()
        return base_royalty * 0.88  # Deduct 12% GST


# Example usage
physical_book = Book("Sample Book", "John Doe", "Sample Publisher", 20)
physical_book.copies_sold = 2000
print(f"Physical Book Royalty: ${physical_book.royalty():.2f}")

ebook = EBook("Sample EBook", "John Doe", "Sample Publisher", 15, "EPUB")
ebook.copies_sold = 2000
print(f"EBook Royalty: ${ebook.royalty():.2f}")