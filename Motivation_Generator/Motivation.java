import java.util.Random;
import java.util.Scanner;

public class Motivation {

    private static String[] tough = new String[]{"Time to move your butt","Get up","Up you get","Go go go","Get the fuck up","Fuck it up","Shift your butt","Someone's gotta do it", "Bitch, please","The day isn't going to start itself","Make some coffee","Time to burn some toast","Better get going","You need to get moving","Remember the money"};
    private static String[] tough_nickname = new String[]{"butt-face", "bitch", "gremlin", "goblin", "fucker", "demon","asshat","stupid","jerk","dipstick","dork","bonehead","dingbat","jackass","galah","cretin","idiot","twat","wanker","bird brain"};
    private static String[] soft = new String[]{"You got this", "C'mon, up you get", "It's a bones day", "Let's go","Let's get this bread","Smash it","Coffee is worth it","Remember the money","The sun is shining and so are you","Today is a beautiful day","You're gonna smash this","Your dreams are so close","Everybody loves you","You're amazing"};
    private static String[] soft_nickname = new String[]{"cutie","sweetie","love","precious","babe","bae","cuddle bunny","darling","dear","gorgeous","honey","hot stuff","peanut","royalty","sunshine","handsome","casanova"};

    public static void main(String[] args) {
        Boolean loop = true;
        Scanner input = new Scanner(System.in);
        System.out.println("Welcome to the Motivation Generator.");
        while (loop == true) {
            System.out.println("Would you like a soft or a tough motivation?");
            String userInput = input.nextLine().toLowerCase();
            if (userInput.equals("soft")) {
                System.out.println(softGenerator());
                loop = keepGoing();
            } else if (userInput.equals("tough")) {
                System.out.println(toughGenerator());
                loop = keepGoing();
            }
            else {
                System.out.println("Hmm, I didn't understand that. Would you like a tough or soft motivation?");
            }
        }
        System.out.println("Have a great day! Bye bye!");
    }

    public static String getRandom(String[] array) {
        int rnd = new Random().nextInt(array.length);
        return array[rnd];
    }

    public static String softGenerator() {
        return getRandom(soft) + " my " + getRandom(soft_nickname);
    }

    public static String toughGenerator() {
        return getRandom(tough) + " you " + getRandom(tough_nickname);
    }

    public static boolean keepGoing() {
        Scanner input = new Scanner(System.in);
        System.out.println("Type 'yes' if you would like another motivation.");
        if (input.nextLine().toLowerCase().equals("yes")) {
            return true;
        }
        else {
            return false;
        }
    }
}