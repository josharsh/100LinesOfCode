import java.util.Random;
import java.util.Scanner;
class blackJack {
    public static void main(String[] args) {

        System.out.println("Welcome to the simplified blackjack game!");
        Scanner scannerObject = new Scanner(System.in);

        Random dice = new Random();
        int number1p, number2p;
        int number1d, number2d;
        int sumplayer, sumdealer;
        int number3p, number3d;
        boolean dealerGo;

        number1p = 2 + dice.nextInt(9);
        number2p = 2 + dice.nextInt(9);
        System.out.println("You get " + number1p + " and " + number2p);

        sumplayer = number1p + number2p;
        System.out.println("Your total is " + sumplayer);

        number1d = 2 + dice.nextInt(9);
        number2d = 2 + dice.nextInt(9);
        sumdealer = number1d + number2d;

        System.out.println("The dealer has a " + number1d + " showing , and a hidden card.");
        String answer;
        System.out.print("Would you like to 'hit' or 'stay'?");
        answer = scannerObject.nextLine();
        while (!answer.equals("stay") && sumplayer < 22) {


            number3p = 2 + dice.nextInt(9);
            System.out.println("You drew a " + number3p);
            sumplayer += number3p;
            System.out.println("Your total is " + sumplayer);
            if(sumplayer<22) {
                System.out.print("Would you like to 'hit' or 'stay'?");
                answer = scannerObject.nextLine();
            }
        }
        if (sumplayer > 21)
            System.out.println("DEALER WINS");
        else {
            System.out.println("OK,dealer is playing");
            System.out.println("His hidden card was " + number2d);
            System.out.println("His total is " + sumdealer);


            dealerGo = dice.nextBoolean();
            while (dealerGo  && sumdealer <= 16) {

                System.out.println("Dealer chooses to hit");
                number3d = 2 + dice.nextInt(12);
                System.out.println("He draws a " + number3d);
                sumdealer += number3d;
                System.out.println("His total is " + sumdealer);
                dealerGo = dice.nextBoolean();

            }
            if (sumdealer > 21)
                System.out.println("YOU WIN");
            else {
                System.out.println("Dealer stays");

                System.out.println("Dealer total is " + sumdealer);
                System.out.println("Your total is " + sumplayer);
                if (sumplayer < sumdealer)
                    System.out.println("DEALER WINS!");
                else
                    System.out.println("YOU WINS!");
            }
        }

    }
}
