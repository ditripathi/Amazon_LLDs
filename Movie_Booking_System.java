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



import java.util.ArrayList;

class Movie {
    private String title;
    private String genre;
    private int duration;

    public Movie(String title, String genre, int duration) {
        this.title = title;
        this.genre = genre;
        this.duration = duration;
    }

    public String getTitle() {
        return title;
    }

    public String getGenre() {
        return genre;
    }

    public int getDuration() {
        return duration;
    }
}

class Theater {
    private String name;
    private ArrayList<Movie> movies;

    public Theater(String name) {
        this.name = name;
        movies = new ArrayList<>();
    }

    public void addMovie(Movie movie) {
        movies.add(movie);
    }

    public void displayMovies() {
        for (Movie movie : movies) {
            System.out.println(movie.getTitle());
        }
    }
}

class Ticket {
    private Movie movie;
    private String seatNumber;
    private double price;

    public Ticket(Movie movie, String seatNumber, double price) {
        this.movie = movie;
        this.seatNumber = seatNumber;
        this.price = price;
    }

    public Movie getMovie() {
        return movie;
    }

    public String getSeatNumber() {
        return seatNumber;
    }

    public double getPrice() {
        return price;
    }
}

class BookingSystem {
    private ArrayList<Ticket> bookings;

    public BookingSystem() {
        bookings = new ArrayList<>();
    }

    public void bookTicket(Ticket ticket) {
        bookings.add(ticket);
    }

    public void displayBookings() {
        for (Ticket ticket : bookings) {
            System.out.println("Movie: " + ticket.getMovie().getTitle() + ", Seat: " + ticket.getSeatNumber() + ", Price: " + ticket.getPrice());
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Movie movie1 = new Movie("Inception", "Sci-Fi", 148);
        Movie movie2 = new Movie("The Shawshank Redemption", "Drama", 142);

        Theater theater = new Theater("Cineplex");

        theater.addMovie(movie1);
        theater.addMovie(movie2);

        Ticket ticket1 = new Ticket(movie1, "A12", 10.5);
        Ticket ticket2 = new Ticket(movie2, "B7", 8.5);

        BookingSystem bookingSystem = new BookingSystem();
        bookingSystem.bookTicket(ticket1);
        bookingSystem.bookTicket(ticket2);

        bookingSystem.displayBookings();
    }
}
