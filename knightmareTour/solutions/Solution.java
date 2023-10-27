import java.util.*;
import java.util.stream.*;

public class Solution {
    
    static class Pair {
        int y, x;

        Pair(int y, int x) {
            this.y = y;
            this.x = x;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            Pair pair = (Pair) o;
            return y == pair.y && x == pair.x;
        }

        @Override
        public int hashCode() {
            return Objects.hash(y, x);
        }

        @Override
        public String toString() {
            return "(" + y + ", " + x + ")";
        }
    }
    
    static Set<Pair> tryDirection(int start_y, int start_x, List<int[]> _moves_remaining,
                                  Map<Pair, Integer> positionToNumber, Map<Integer, Set<Pair>> numberToPositions, int yDim, int xDim) {
        Deque<Object[]> fringe = new ArrayDeque<>();
        Pair start = new Pair(start_y, start_x);
        numberToPositions.get(positionToNumber.get(start)).forEach(spot -> {
            fringe.add(new Object[]{spot, new HashSet<>(Collections.singletonList(positionToNumber.get(spot))), new ArrayList<>(_moves_remaining)});
        });
        
        Set<Pair> ret = new HashSet<>();
        while (!fringe.isEmpty()) {
            Object[] pop = fringe.pop();
            Pair spot = (Pair) pop[0];
            Set<Integer> landsSeen = (Set<Integer>) pop[1];
            List<int[]> remainingMoves = (List<int[]>) pop[2];
            
            if (remainingMoves.isEmpty()) {
                ret.add(spot);
                continue;
            }
            
            int[] move = remainingMoves.remove(0);
            Pair newSpot = new Pair(spot.y + move[0], spot.x + move[1]);
            if (positionToNumber.get(newSpot) != null && positionToNumber.get(spot) != null && positionToNumber.get(newSpot).equals(positionToNumber.get(spot))) {
                newSpot = new Pair(spot.y + 2 * move[0], spot.x + 2 * move[1]);
            }
            
            List<Object[]> toAdd = new ArrayList<>();
            var temp  =positionToNumber.get(newSpot);
            // System.err.println("newSpot is " + newSpot);
            // System.err.println("temp is " + temp);
            // System.err.println("numberToPositions at temp is " + temp);
            if (newSpot.y >= 0 && newSpot.y < yDim && newSpot.x >= 0 && newSpot.x < xDim && positionToNumber.containsKey(newSpot)) {
                numberToPositions.get(positionToNumber.get(newSpot)).forEach(connectedSpot -> {
                    if (!landsSeen.contains(positionToNumber.get(connectedSpot))) {
                        Set<Integer> newLandsSeen = new HashSet<>(landsSeen);
                        newLandsSeen.add(positionToNumber.get(connectedSpot));
                        toAdd.add(new Object[]{connectedSpot, newLandsSeen, new ArrayList<>(remainingMoves)});
                    }
                });
            }
            
            fringe.addAll(toAdd);
        }
        return ret;
    }

    static void runCase(Scanner scanner) {
        int yDim = scanner.nextInt();
        int xDim = scanner.nextInt();
        int startY = scanner.nextInt();
        int startX = scanner.nextInt();
        scanner.nextLine();  // to skip the rest of the line

        int[][] grid = new int[yDim][xDim];
        for (int i = 0; i < yDim; i++) {
            for (int j = 0; j < xDim; j++) {
                grid[i][j] = scanner.nextInt();
            }
        }
        
        Map<Integer, Set<Pair>> numberToPositions = new HashMap<>();
        Map<Pair, Integer> positionToNumber = new HashMap<>();
        for (int y = 0; y < yDim; y++) {
            for (int x = 0; x < xDim; x++) {
                numberToPositions.computeIfAbsent(grid[y][x], k -> new HashSet<>()).add(new Pair(y, x));
                positionToNumber.put(new Pair(y, x), grid[y][x]);
            }
        }

        Set<Pair> reachableSpots = new HashSet<>();
        Pair start = new Pair(startY, startX);
        int[][] directions = {{-1, -1}, {-1, 1}, {1, -1}, {1, 1}};
        int[][] moves = {{2, 1}, {1, 2}};
        for (int[] dir : directions) {
            for (int[] move : moves) {
                List<int[]> currentMoves = new ArrayList<>();
                for (int i = 0; i < move[0]; i++) currentMoves.add(new int[]{dir[0], 0});
                for (int i = 0; i < move[1]; i++) currentMoves.add(new int[]{0, dir[1]});
                for (int i = 0; i < 2; i++) {
                    reachableSpots.addAll(tryDirection(start.y, start.x, currentMoves, positionToNumber, numberToPositions, yDim, xDim));
                    Collections.reverse(currentMoves);
                }
            }
        }

        long uniqueNumbers = reachableSpots.stream().map(positionToNumber::get).distinct().count();
        System.out.println(uniqueNumbers);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int cases = scanner.nextInt();
        for (int t = 0; t < cases; t++) {
            runCase(scanner);
        }
        scanner.close();
    }
}
