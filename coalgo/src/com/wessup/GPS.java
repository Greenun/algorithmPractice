package com.wessup;

import java.util.*;

class GPS {

//    public static void main(String[] args) {
//        GPS s = new GPS();
//        int[][] a = {{1, 2}, {1, 3}, {2, 3}, {2, 4}, {3, 4}, {3, 5}, {4, 6}, {5, 6}, {5, 7}, {6, 7}};
//        int[] g = {1,2,3,3,6,7};
//        s.solution(7, 10, a, 6, g);
//    }

    public int solution(int n, int m, int[][] edge_list, int k, int[] gps_log) {
        int[][] dp = new int[k][n];
        for (int i = 0; i < k; i++) {
            for (int j = 0; j < n; j++) {
                dp[i][j] = k + 100;
            }
        }

        dp[0][gps_log[0]-1] = 0; // init
        Map<Integer, List<Integer>> roadMap = new HashMap<>();
        for (int i = 0; i < n; i++) {
            roadMap.put(i, new LinkedList<Integer>());
            roadMap.get(i).add(i);
        }
        for ( int i = 0; i < m; i++){
            int[] point = new int[2];
            point[0] = edge_list[i][0] - 1;
            point[1] = edge_list[i][1] - 1;
            roadMap.get(point[0]).add(point[1]);
            roadMap.get(point[1]).add(point[0]);
        }
        for (int i = 1; i < k; i++) {
            for (int j = 0; j < n; j++) {
                List<Integer> temp = new ArrayList<>();
                for (int v: roadMap.get(j)) {
                    temp.add(dp[i-1][v]);
                }
                dp[i][j] = Collections.min(temp);
                dp[i][j] += (gps_log[i] == j+1)? 0 : 1;
            }
        }
//        for (int i = 0; i < k; i++) {
//            for (int j = 0; j < n; j++) {
//                System.out.print(dp[i][j] + " ");
//            }
//            System.out.println();
//        }
        if (dp[k-1][gps_log[gps_log.length-1]-1] >= k + 100) {
            return -1;
        }
        return dp[k-1][gps_log[gps_log.length-1]-1];
    }

}