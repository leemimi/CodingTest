import java.util.*;
class Solution {
    static int answer;
    static int n;
    static int[][] dun;
    static boolean[] visited;    
    public int solution(int k, int[][] dungeons) {
        answer = 0;
        visited = new boolean[dungeons.length];
        n = dungeons.length;
        
        dun = dungeons;
        
        dfs(0,k);
        
        return answer;
    }
    static void dfs(int L, int kk){
        
        for(int i=0; i<n; i++){
            if(!visited[i] && kk>=dun[i][0]){
                visited[i] = true;
                dfs(L+1, kk- dun[i][1]);
                visited[i] = false;
            }
        }
         answer = Math.max(answer, L);
        
    }
}