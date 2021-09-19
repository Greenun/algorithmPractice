package com.wessup;
import java.util.*;

public class OrderList {
    private static void solution(int numOfOrder, String[] orderArr) {
        // TODO: 이곳에 코드를 작성하세요. 추가로 필요한 함수와 전역변수를 선언해서 사용하셔도 됩니다.
        for (int i = 0; i < numOfOrder; i++) {
            Stack<Character> stack = new Stack<>();
            String order = orderArr[i];
            String changed = "";
            for (int j = 0; j < order.length(); j++) {
                if (order.charAt(j) == ')') {
                    String subStr = "";
                    while (!stack.isEmpty()) {
                        char temp = stack.pop();
                        if (temp == '(') {
                            break;
                        }
                        subStr = temp + subStr;
                    }
                    // handle sub string
                    char temp = stack.pop();
                    if (Character.isDigit(temp)) {
                        int len = Integer.parseInt(String.valueOf(temp));
                        for (int k = 0; k < len; k++) {
                            changed += subStr;
                        }
                    } else {
                        String changedSub = "";
                        int len = subStr.length();
                        for (int k = 0; k < len; k++) {
                            changedSub += temp + subStr.charAt(k);
                        }
                        changed += changedSub;
                    }
                } else {
                    stack.push(order.charAt(j));
                }
            }

            System.out.println(changed);
        }
    }

    private static class InputData {
        int numOfOrder;
        String[] orderArr;
    }

    private static InputData processStdin() {
        InputData inputData = new InputData();

        try (Scanner scanner = new Scanner(System.in)) {
            inputData.numOfOrder = Integer.parseInt(scanner.nextLine().replaceAll("\\s+", ""));

            inputData.orderArr = new String[inputData.numOfOrder];
            for (int i = 0; i < inputData.numOfOrder; i++) {
                inputData.orderArr[i] = scanner.nextLine().replaceAll("\\s+", "");
            }
        } catch (Exception e) {
            throw e;
        }

        return inputData;
    }

    public static void main(String[] args) throws Exception {
        InputData inputData = processStdin();

        solution(inputData.numOfOrder, inputData.orderArr);
    }
}
