import java.util.*;
class Solution {
    public int solution(int m, int n, int[][] puddles) {
        int answer = 0;
        int[][] dp = new int[n+1][m+1];
        int num = 1000000007;
        boolean[][] visited = new boolean[n+1][m+1];
        for(int i=0; i<puddles.length;i++){
            visited[puddles[i][1]][puddles[i][0]] = true;
        }
        int cnt = 0;
        dp[1][1] = 1;
        for(int i=1;i<n+1;i++){
            for(int j=1; j<m+1;j++){
                if(visited[i][j]) continue;
                dp[i][j] += dp[i][j-1] + dp[i-1][j]; //왼쪽 + 위
                dp[i][j] %= num;
            }
        }
        
        
        return dp[n][m];
    }
}