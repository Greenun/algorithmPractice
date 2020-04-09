class Solution {
  int MOD = 20170805;
  public int solution(int m, int n, int[][] cityMap) {
      int[][] caseMap = new int[m][n];
      caseMap[0][0] = 1;
      // (0, 0) / (0, 1) (1, 0) / (2, 0) (1, 1) (0, 2) / (3, 0) (1, 2) (2, 1) (0, 3)
      for (int i = 1; i <= m + n - 2; i++) {
          for (int j = 0; j <= i; j++) {
              int row = j;
              int col = i - j;
              if (row >= m || col >= n) continue;
              if (cityMap[row][col] == 1) {
                  caseMap[row][col] = 0;
              }
              else {
                  int r = row - 1;
                  int c = col - 1;
                  while (r >= 0) {
                      if (cityMap[r][col] == 2) {
                          r--;
                      }
                      else{
                          break;
                      }
                  }
                  while (c >= 0) {
                      if (cityMap[row][c] == 2) {
                          c--;
                      }
                      else {
                          break;
                      }
                  }
                  int add1, add2 = 0;
                  if (c < 0) add2 = 0;                  
                  else add2 = caseMap[row][c];
                  if (r < 0) add1 = 0;
                  else add1 = caseMap[r][col];
                  caseMap[row][col] = (add1 + add2) % MOD;
              }
          }
      }
      return caseMap[m-1][n-1] % MOD;
  }
  public void print(int m, int n, int[][] caseMap) {
      for (int i = 0; i < m; i++) {
          for (int j = 0; j < n; j++) {
              System.out.print(caseMap[i][j]+" ");
          }
          System.out.println("");
      }
  }
}

// 오른쪽, 아래를 나눠서 - 더 빠를듯
class Solution {
  int MOD = 20170805;
  public int solution(int m, int n, int[][] cityMap) {
        int answer = 0;
        int[][] right = new int[m + 1][n + 1];
        int[][] down = new int[m + 1][n + 1];

        right[1][1] = 1;
        down[1][1] = 1;

        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (cityMap[i - 1][j - 1] == 0) {
                    right[i][j] += (right[i][j - 1] + down[i - 1][j]) % MOD;
                    down[i][j] += (down[i - 1][j] + right[i][j - 1]) % MOD;
                } else if (cityMap[i - 1][j - 1] == 2) {
                    right[i][j] = right[i][j - 1];
                    down[i][j] = down[i - 1][j];
                }
            }
        }
        answer = (right[m][n - 1] + down[m - 1][n]) % MOD;
        return answer;
    }
}
