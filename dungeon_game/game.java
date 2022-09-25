import java.util.Scanner;
import java.util.Random;

public class Main {


    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);
        Random rand = new Random();

        boolean running = true;
        while (running) {
            String[] enemies = {"Skeleton", "Zombie", "Warrior", "Assassin"};
            int maxEnemyHealth = 75;
            int enemyAttackDamage = 25;

            // variables
            int health = 100;
            int attackDamage = 50;
            int numHealthPotions = 1;
            int healthPotionHealAmount = 20;
            int healthPotionDropChance = 35; // % drop chance


            System.out.println("Welcome to the Dungeon!");

            GAME:
            while (true) {

                System.out.println("----------------------------------------");

                int enemyHealth = rand.nextInt(maxEnemyHealth);
                String enemy = enemies[rand.nextInt(enemies.length)];
                System.out.println("\t#  " + enemy + " has appeared!  #\n");

                while (enemyHealth > 0) {

                    System.out.println("\n\tYour HP: " + health);
                    System.out.println("\t" + enemy + "'s HP: " + enemyHealth);
                    System.out.println("\n\tWhat do you want to do?");
                    System.out.println("\t1. Attack");
                    System.out.println("\t2. Drink health potion");
                    System.out.println("\t3. Run!");

                    String input = in.nextLine();
                    if (input.equals("1")) {
                        int damageDealt = rand.nextInt(attackDamage);
                        int damageTaken = rand.nextInt(enemyAttackDamage);

                        enemyHealth -= damageDealt;
                        health -= damageTaken;

                        System.out.println("\t> You strike the " + enemy + " for " + damageDealt + " damage.");
                        System.out.println("\t> You receive " + damageTaken + " in retaliation");

                        if (health < 1) {
                            System.out.println("\t> You have taken too much damage, you are too weak to keep going!");
                            break;

                        }

                    } else if (input.equals("2")) {

                        if (numHealthPotions <= 0) {
                            System.out.println("\t You have no potions left!");
                        } else if (health >= 76) {
                            System.out.print("\t You are too healthy for one!");

                        } else {

                            health += healthPotionHealAmount;
                            numHealthPotions--;
                            System.out.println("\t> You drink a health potion, healing yourself for " + healthPotionHealAmount + "."
                                    + "\n\t> " + health + "HP." + "\n\t> You have " + numHealthPotions + " health potions left.\n");
                        }


                    } else if (input.equals("3")) {
                        System.out.println("\t You run away from the " + enemy + "!");
                        continue GAME;
                    } else {

                        System.out.println("\t Invalid Command.");

                    }
                }
                if (health < 1) {

                    System.out.println("You crawl out of the dungeon, quite weak from battle.");
                    break;
                }

                System.out.println("----------------------------------------");
                System.out.println(" # " + enemy + " was defeated! # ");
                System.out.println("# You have " + health + " HP left. #");
                if (rand.nextInt(100) < healthPotionDropChance) ;
                numHealthPotions++;
                System.out.println(" # The " + enemy + " dropped a health potion! #");
                System.out.println(" # You now have " + numHealthPotions + " health potion(s). # ");

            }
            System.out.println("----------------------------------------");
            System.out.println("What would you like to do now?");
            System.out.println("1. Another Chance!");
            System.out.println("2. Exit dungeon!");

            do {
                String input = in.nextLine();
                if (input.equals("1")) {
                    System.out.println("You continue on your adventure.");
                    break;
                } else if (input.equals("2")) {
                    System.out.println("You exit the dungeon, goodbye!");
                    (running)=false;
                    break;
                } else {
                    System.out.println("Invalid Command.");
                }
            }
            while (true);

            System.out.println("###########################");
            System.out.println("# THANKS FOR PLAYING! #");
            System.out.println("###########################");


        }
    }
}
