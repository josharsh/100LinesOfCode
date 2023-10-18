import java.util.Scanner;

public class MovieTicketManager {
    private static final int NUM_SHOWTIMES = 3;
    private static final int NUM_SEATS = 10;
    private static boolean[][] seatAvailability = new boolean[NUM_SHOWTIMES][NUM_SEATS];

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("\nMovie Ticket Manager");
            System.out.println("1. Show Available Seats");
            System.out.println("2. Book a Ticket");
            System.out.println("3. Exit");
            System.out.print("Select an option: ");
            int choice = scanner.nextInt();

            switch (choice) {
                case 1:
                    showAvailableSeats();
                    break;
                case 2:
                    bookTicket(scanner);
                    break;
                case 3:
                    System.out.println("Goodbye!");
                    scanner.close();
                    return;
                default:
                    System.out.println("Invalid choice. Please select a valid option.");
                    break;
            }
        }
    }

    private static void showAvailableSeats() {
        System.out.println("\nAvailable Seats:");
        for (int showtime = 0; showtime < NUM_SHOWTIMES; showtime++) {
            System.out.print("Showtime " + (showtime + 1) + ": ");
            for (int seat = 0; seat < NUM_SEATS; seat++) {
                if (!seatAvailability[showtime][seat]) {
                    System.out.print((seat + 1) + " ");
                } else {
                    System.out.print("X ");
                }
            }
            System.out.println();
        }
    }

    private static void bookTicket(Scanner scanner) {
        System.out.print("\nEnter Showtime (1-" + NUM_SHOWTIMES + "): ");
        int showtime = scanner.nextInt();
        if (showtime < 1 || showtime > NUM_SHOWTIMES) {
            System.out.println("Invalid showtime selection.");
            return;
        }

        System.out.print("Enter Seat Number (1-" + NUM_SEATS + "): ");
        int seat = scanner.nextInt();
        if (seat < 1 || seat > NUM_SEATS) {
            System.out.println("Invalid seat selection.");
            return;
        }

        if (seatAvailability[showtime - 1][seat - 1]) {
            System.out.println("Seat " + seat + " for Showtime " + showtime + " is already booked.");
        } else {
            seatAvailability[showtime - 1][seat - 1] = true;
            System.out.println("Ticket booked for Showtime " + showtime + ", Seat " + seat + ".");
        }
    }
}
