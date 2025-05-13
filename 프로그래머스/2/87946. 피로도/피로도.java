import java.util.*;
class Solution {
    static int n;
    static int[][] dungeons;
    static int answer;
    public int solution(int k, int[][] dungeons) {
        this.dungeons = dungeons;
        answer = 0;
        n = dungeons.length;
        for(int i=0;i<n;i++){
            boolean[] visited = new boolean[n];
            dfs(i, k, 0, visited);
        }
        
        return answer;
    }
    public static void dfs(int L, int hp, int cnt, boolean[] visited){
        if(L==n){
            answer = Math.max(cnt, answer);
        }
        for(int i=0; i<n;i++){
            if(!visited[i]&& hp >= dungeons[i][0]){
                visited[i] = true;
                dfs(L+1, hp-dungeons[i][1], cnt+1, visited);
                visited[i] = false;
            }
        }
    }
}