import java.util.Scanner;
import java.util.List;
import java.util.ArrayList;

public class CoinCombinations {
    int value;

    public CoinCombinations(int value) {
        this.value = value;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(); sc.close();

        int[] coins = {1, 5, 10, 25, 50, 100};
        List<Integer> combination = new ArrayList<>();
        CoinCombinations totalCombinations = new CoinCombinations(0);
        findCombinations(n, coins, combination, 0, totalCombinations);

        System.out.println("Total Combinations: " + totalCombinations.value);
    }

    private static void findCombinations(int n, int[] coins, List<Integer> combination, int start, CoinCombinations totalCombinations) {
        if (n == 0) {
            System.out.println(combination);
            totalCombinations.value++;
            return;
        }

        if (n > 0) {
            for (int i = start; i < coins.length; i++) {
                combination.add(coins[i]);
                findCombinations(n - coins[i], coins, combination, i, totalCombinations);
                combination.remove(combination.size() - 1);
            }
        }
    }
}