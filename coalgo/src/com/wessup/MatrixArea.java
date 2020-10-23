package com.wessup;

import java.util.*;
import java.util.stream.Collectors;

public class MatrixArea {
        private static void solution(int sizeOfMatrix, int[][] matrix) {
            // TODO: 이곳에 코드를 작성하세요.
            Queue<Integer[]> queue = new LinkedList<>();
            final Integer[][] delta = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};// right, down, left, up
            int area = 1;
            Set<String> visited = new HashSet<>();
            int[][] table = new int[sizeOfMatrix][sizeOfMatrix];
            for (int i = 0; i < sizeOfMatrix; i++) {
                for (int j = 0; j < sizeOfMatrix; j++) {
                    Integer[] start = new Integer[]{i, j};
                    if (matrix[i][j] == 0 || table[i][j] != 0) {
                        continue;
                    }
                    queue.offer(start);
                    visited.clear();
                    visited.add(Arrays.toString(start));
                    while (!queue.isEmpty()) {
                        Integer[] current = queue.poll();
                        Integer currentX= current[0];
                        Integer currentY = current[1];
                        table[currentX][currentY] = area;
                        for (Integer[] temp: delta) {
                            Integer adjX = currentX + temp[0];
                            Integer adjY = currentY + temp[1];
                            Integer[] adj = new Integer[]{adjX, adjY};
                            if (adjX < 0 || adjX >= sizeOfMatrix || adjY < 0 || adjY >= sizeOfMatrix) continue;
                            if (matrix[adjX][adjY] == 1 && !visited.contains(Arrays.toString(adj))) {
                                queue.offer(adj);
                                visited.add(Arrays.toString(adj));
                            }
                        }
                    }
                    area++;
                }
            }
            Map<Integer, Integer> areaMap = new HashMap<>();
            for (int i = 1; i <= area; i++) {
                areaMap.put(i, 0);
            }
            for (int i = 0; i < sizeOfMatrix; i++) {
                for (int j = 0; j < sizeOfMatrix; j++) {
                    areaMap.computeIfPresent(table[i][j], (k, v) -> ++v);
                }
            }
            System.out.println(--area);
            String result = areaMap.values().stream().sorted().map(v -> String.valueOf(v)).collect(Collectors.joining(" "));
            if (result.length() > 2) {
                System.out.println(result.substring(2));
            }
        }

    private static class InputData {
        int sizeOfMatrix;
        int[][] matrix;
    }

    private static InputData processStdin() {
        InputData inputData = new InputData();

        try (Scanner scanner = new Scanner(System.in)) {
            inputData.sizeOfMatrix = Integer.parseInt(scanner.nextLine().replaceAll("\\s+", ""));

            inputData.matrix = new int[inputData.sizeOfMatrix][inputData.sizeOfMatrix];
            for (int i = 0; i < inputData.sizeOfMatrix; i++) {
                String[] buf = scanner.nextLine().trim().replaceAll("\\s+", " ").split(" ");
                for (int j = 0; j < inputData.sizeOfMatrix; j++) {
                    inputData.matrix[i][j] = Integer.parseInt(buf[j]);
                }
            }
        } catch (Exception e) {
            throw e;
        }

        return inputData;
    }

    public static void main(String[] args) throws Exception {
        InputData inputData = processStdin();

        solution(inputData.sizeOfMatrix, inputData.matrix);
    }
}
