package com.wessup;
import java.util.*;

public class TurnHang {
    private static void solution(int numOfAllPlayers, int numOfQuickPlayers, char[] namesOfQuickPlayers, int numOfGames, int[] numOfMovesPerGame){
        // TODO: 이곳에 코드를 작성하세요. 추가로 필요한 함수와 전역변수를 선언해서 사용하셔도 됩니다.
        String pool = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        Map<String, Integer> table = new HashMap<>();
        char[] players = new char[numOfAllPlayers-1];
        table.put(String.valueOf(pool.charAt(0)), 1); // A
        for (int i = 1; i < numOfAllPlayers; i++) {
            players[i-1] = pool.charAt(i);
            table.put(String.valueOf(pool.charAt(i)), 0);
        }
        Set<Character> quickPlayers = new HashSet<>();
        for (char p: namesOfQuickPlayers) {
            quickPlayers.add(p);
        }
        char tagger = 'A';
        int current = 0;
        for (int i = 0; i < numOfGames; i++) {
            current = (current + numOfMovesPerGame[i] + numOfAllPlayers - 1) % (numOfAllPlayers - 1);
            if (quickPlayers.contains(players[current])) {
                table.compute(String.valueOf(tagger), (k, v) -> ++v);
            } else {
                char temp = tagger;
                table.compute(String.valueOf(players[current]), (k, v) -> ++v);
                tagger = players[current];
                players[current] = temp;
            }
        }
        for (char temp: players) {
            int value = table.get(String.valueOf(temp));
            System.out.println(temp + " " + value);
        }
        System.out.println(tagger + " " + table.get(String.valueOf(tagger)));

    }

    private static class InputData {
        int numOfAllPlayers;
        int numOfQuickPlayers;
        char[] namesOfQuickPlayers;
        int numOfGames;
        int[] numOfMovesPerGame;
    }

    private static InputData processStdin() {
        InputData inputData = new InputData();

        try (Scanner scanner = new Scanner(System.in)) {
            inputData.numOfAllPlayers = Integer.parseInt(scanner.nextLine().replaceAll("\\s+", ""));

            inputData.numOfQuickPlayers = Integer.parseInt(scanner.nextLine().replaceAll("\\s+", ""));
            inputData.namesOfQuickPlayers = new char[inputData.numOfQuickPlayers];
            System.arraycopy(scanner.nextLine().trim().replaceAll("\\s+", "").toCharArray(), 0, inputData.namesOfQuickPlayers, 0, inputData.numOfQuickPlayers);

            inputData.numOfGames = Integer.parseInt(scanner.nextLine().replaceAll("\\s+", ""));
            inputData.numOfMovesPerGame = new int[inputData.numOfGames];
            String[] buf = scanner.nextLine().trim().replaceAll("\\s+", " ").split(" ");
            for(int i = 0; i < inputData.numOfGames ; i++){
                inputData.numOfMovesPerGame[i] = Integer.parseInt(buf[i]);
            }
        } catch (Exception e) {
            throw e;
        }

        return inputData;
    }

    public static void main(String[] args) throws Exception {
        InputData inputData = processStdin();

        solution(inputData.numOfAllPlayers, inputData.numOfQuickPlayers, inputData.namesOfQuickPlayers, inputData.numOfGames, inputData.numOfMovesPerGame);
    }
}
