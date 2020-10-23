package com.wessup;

import java.util.*;

public class Lifeboat {
    public int solution(int[] people, int limit) {
        int length = people.length;
        Arrays.sort(people);
        int remain = limit;
        int count = 0;
        int left = 0;
        int right = length - 1;
        while (left <= right) {
            remain = limit - people[right];
            if (people[left] <= remain) {
                left++;
            }
            right--;
            count++;
        }
        return count;

//        // 효율성 실패
//        int length = people.length;
//        Arrays.sort(people);
//        Set<Integer> saved = new HashSet<>();
//        int remain = limit;
//        int count = 0;
//        int setSize = 0;
//        for (int left = 0; left < length; left++) {
//            if (setSize >= length) break;
//            remain = limit - people[left];
//            saved.add(left);
//            setSize++;
//            for (int right = length - 1; right > left; right--) {
//                if (!saved.contains(right) && people[right] <= remain) {
//                    saved.add(right);
//                    setSize++;
//                    break;
//                }
//            }
//            count++;
//        }
//        return count;

        // 실패
//        int length = people.length;
//        Set<Integer> saved = new HashSet<>();
//        Arrays.sort(people);
//        Stack<Integer> stack = new Stack<>();
//        int remain = 0;
//        int count = 0;
//        for (int right = length - 1; right >= 0; right--) {
//            if (saved.size() >= length) break;
//            saved.add(right);
//            remain = limit - people[right];
//            int left = 0;
//            while (people[left] <= remain) {
//                if (!saved.contains(left)) {
//                    stack.push(left);
//                }
//                left++;
//            }
//            if (!stack.isEmpty()) {
//                saved.add(stack.pop());
//                stack.clear();
//            }
//            System.out.println(stack);
//            count++;
//        }
//        System.out.println(count);
//        return count;
    }
}
