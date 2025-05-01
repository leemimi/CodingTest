import java.util.*;
class Solution {
    static List<Integer>[] graph; 
    static int min;
    public int solution(int n, int[][] wires) {
        int answer = Integer.MAX_VALUE;
        graph = new ArrayList[n+1];
        
        for(int i=0;i<=n;i++){
            graph[i] = new ArrayList<>();
        }
        for(int i=0;i<wires.length;i++){
            graph[wires[i][0]].add(wires[i][1]);
            graph[wires[i][1]].add(wires[i][0]);
        }
        for(int i=0; i<wires.length;i++){
            int a = wires[i][0];
            int b = wires[i][1];
            boolean[] visited = new boolean[n+1];
            graph[a].remove(Integer.valueOf(b));
            graph[b].remove(Integer.valueOf(a));
            
            int cnt = dfs(i+1, visited);
            cnt = Math.abs(cnt - (n-cnt));
            answer = Math.min(cnt, answer);
            graph[a].add(b);
            graph[b].add(a);
        }
        
        
        return answer;
    }
    public static int dfs(int start, boolean[] visited){
        visited[start] = true;
        int cnt = 1;
        
        for(int next: graph[start]){
            if(!visited[next]){
                cnt += dfs(next,visited);
            }
        }
        return cnt;
    }
}