+-----------------+       +----------------+
|     Movie       |       |    Theater     |
+-----------------+       +----------------+
| - title: String |       | - name: String |
| - genre: String |       | - movies: List |
| - duration: int |       +----------------+
+-----------------+             |
      |                          |
      | has a                    | contains
      |                          |
      V                          V
+----------------+       +-----------------+
|     Ticket     |       | BookingSystem   |
+----------------+       +-----------------+
| - movie: Movie |       | - bookings: List|
| - seat_number  |       +-----------------+
| - price: float |
+----------------+

class Movie:
    def __init__(self, title, genre, duration):
        self.title = title
        self.genre = genre
        self.duration = duration

class Theater:
    def __init__(self, name):
        self.name = name
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)

    def display_movies(self):
        for movie in self.movies:
            print(movie.title)

class Ticket:
    def __init__(self, movie, seat_number, price):
        self.movie = movie
        self.seat_number = seat_number
        self.price = price

class BookingSystem:
    def __init__(self):
        self.bookings = []

    def book_ticket(self, ticket):
        self.bookings.append(ticket)

    def display_bookings(self):
        for ticket in self.bookings:
            print(f"Movie: {ticket.movie.title}, Seat: {ticket.seat_number}, Price: {ticket.price}")

movie1 = Movie("Inception", "Sci-Fi", 148)
movie2 = Movie("The Shawshank Redemption", "Drama", 142)

theater = Theater("Cineplex")

theater.add_movie(movie1)
theater.add_movie(movie2)

ticket1 = Ticket(movie1, "A12", 10.5)
ticket2 = Ticket(movie2, "B7", 8.5)

booking_system = BookingSystem()
booking_system.book_ticket(ticket1)
booking_system.book_ticket(ticket2)

booking_system.display_bookings()
