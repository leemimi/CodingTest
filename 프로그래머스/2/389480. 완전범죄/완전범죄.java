import java.util.*;
class Solution {
    static int[][] info;
    static int n,m;
    static boolean[][][] visited;
    static int res = Integer.MAX_VALUE;
    static int len;
    public int solution(int[][] info, int n, int m) {
        int answer = 0;
        this.info = info;
        this.n = n;
        this.m = m;
        len = info.length;
        
        visited = new boolean[len][n+1][m+1];
        dfs(0,0,0);
        if(res == Integer.MAX_VALUE) return -1;
        
        return res;
    }
    public static void dfs(int L, int a, int b){
        if(a>=n || b>=m) return;
        if(L==len){
            res = Math.min(a, res);
            return;
        }
        if(visited[L][a][b]) return;
        visited[L][a][b] = true;
        
        dfs(L+1, a+info[L][0],b);
        dfs(L+1, a, b+info[L][1]);
        
        
    }
}