package com.wessup;

import java.util.*;

public class Cement {
    private static void solution(int day, int width, int[][] blocks) {
        // TODO: 이곳에 코드를 작성하세요. 추가로 필요한 함수와 전역변수를 선언해서 사용하셔도 됩니다.
        int[] space = new int[width];
        int cement = 0;
        int[] cementPerDay = new int[width];
        for (int i = 0; i < day; i++) {
            for (int j = 0; j < width; j++) {
                space[j] += blocks[i][j];
            }
            // after add blocks
            System.out.println(Arrays.toString(space));
            cement += putCement(space, width);
            System.out.println(Arrays.toString(space));
            System.out.println(cement);
        }
    }
    private static int putCement(int[] space, int width) {
        int cement = 0;
        int left = 0;
        int current = left + 1;
        while (left < width - 1) {
            System.out.println("first" + left + " " + current);
            if (space[left] > space[current]) {
                boolean increase = true;
                if (current < width - 1 && space[current] < space[current+1]) {
                    increase = true;
                } else {
                    increase = false;
                }
                while (current < width - 1) {
                    if (increase) {
                        if (space[current] >= space[current+1]) {
                            break;
                        }
                    } else {
                        if (space[current] < space[current+1]) break;
                    }
                    current++;
                    if (space[current] > space[left]) break;
                }
                System.out.println("put" + left + " " + current);
                if ( current - left > 1 ) {
                    int idx = Math.min(space[current], space[left]);
                    for (int i = left+1; i < current; i++) {
                        cement += idx - space[i];
                        space[i] = idx;
                    }
                }
                left = current;
                current = left + 1;
            } else {
                left = current;
                current = left + 1;
            }
        }
        return cement;
    }

    private static class InputData {
        int day;
        int width;
        int[][] blocks;
    }

    private static InputData processStdin() {
        InputData inputData = new InputData();

        try (Scanner scanner = new Scanner(System.in)) {
            inputData.day = Integer.parseInt(scanner.nextLine().replaceAll("\\s+", ""));
            inputData.width = Integer.parseInt(scanner.nextLine().replaceAll("\\s+", ""));

            inputData.blocks = new int[inputData.day][inputData.width];
            for (int i = 0; i < inputData.day; i++) {
                String[] buf = scanner.nextLine().trim().replaceAll("\\s+", " ").split(" ");
                for (int j = 0; j < inputData.width; j++) {
                    inputData.blocks[i][j] = Integer.parseInt(buf[j]);
                }
            }
        } catch (Exception e) {
            throw e;
        }

        return inputData;
    }

    public static void main(String[] args) throws Exception {
        InputData inputData = processStdin();

        solution(inputData.day, inputData.width, inputData.blocks);
    }
}
