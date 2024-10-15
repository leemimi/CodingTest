import java.util.*;
class Solution {
    static int[][] arr;
    public int solution(int n, int[][] wires) {
        int answer = n;
        arr = new int[n+1][n+1];
        
        
        for(int i=0; i<wires.length;i++){
            int a = wires[i][0];
            int b = wires[i][1];
            arr[a][b] = 1;
            arr[b][a] = 1;
        }
        for(int i=0; i<wires.length;i++){
            int a = wires[i][0];
            int b = wires[i][1];
            
            arr[a][b] = 0;
            arr[b][a] = 0;
            answer = Math.min(answer, bfs(n, a));
            
            arr[a][b] = 1;
            arr[b][a] = 1;
        }
        
        
        return answer;
    }
    static int bfs(int n, int x){
        boolean[] visited = new boolean[n+1];
        int cnt = 1;
        
        Queue<Integer> q = new LinkedList<>();
        visited[x] = true;
        q.offer(x);
        
        while(!q.isEmpty()){
            int tmp = q.poll();
            
            
            for(int i=1; i<=n;i++){
                if(arr[tmp][i] == 1 && !visited[i]){
                    visited[i] = true;
                    q.offer(i);
                    cnt++;
                }
            }
        }
        
        
        return (int)Math.abs(cnt-(n-cnt));
    }
}