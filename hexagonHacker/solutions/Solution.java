import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Solution {

    static Map<String, double[]> moveOffsets;
    static {
        moveOffsets = new HashMap<>();
        moveOffsets.put("NW", new double[]{-0.5, -1});
        moveOffsets.put("N", new double[]{-1, 0});
        moveOffsets.put("NE", new double[]{-0.5, 1});
        moveOffsets.put("SE", new double[]{0.5, 1});
        moveOffsets.put("S", new double[]{1, 0});
        moveOffsets.put("SW", new double[]{0.5, -1});
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int cases = Integer.parseInt(scanner.nextLine());
        for (int t = 0; t < cases; t++) {
            runTestCase(scanner);
        }
    }

    private static void runTestCase(Scanner scanner) {
        String[] input = scanner.nextLine().split(" ");
        int n = Integer.parseInt(input[0]);
        String a = input[1];

        Matcher matcher = Pattern.compile("NW|NE|SE|SW|N|S").matcher(a);
        Map<String, Integer> seen = new HashMap<>();
        double pos_y = 0;
        double pos_x = 0;
        seen.put(pos_y + "," + pos_x, 1);

        while (matcher.find()) {
            String match = matcher.group();
            double[] offset = moveOffsets.get(match);
            pos_y += offset[0];
            pos_x += offset[1];
            String key = pos_y + "," + pos_x;
            seen.put(key, seen.getOrDefault(key, 0) + 1);
        }

        long numBeenToMoreThanOnce = seen.values().stream().filter(count -> count > 1).count();
        if (numBeenToMoreThanOnce > 0 && numBeenToMoreThanOnce % n == 0) {
            System.out.println("yes " + numBeenToMoreThanOnce);
        } else {
            System.out.println("no");
        }
    }
}
