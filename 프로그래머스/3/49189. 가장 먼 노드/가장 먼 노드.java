import java.util.*;
class Solution {
    
    public int solution(int n, int[][] edge) {
        int answer = 0;
        List<List<Integer>> graph = new ArrayList<>();
        for(int i=0;i<edge.length; i++){
            graph.add(new ArrayList<>());
        }
        
        for(int[] e: edge){
            graph.get(e[0]).add(e[1]);
            graph.get(e[1]).add(e[0]);
        }
        
        int[] dist = new int[n+1];
        Queue<Integer> q = new LinkedList<>();
        q.add(1);
        dist[1] = 1;
        
        while(!q.isEmpty()){
            int now = q.poll();
            for(int next: graph.get(now)){
                if(dist[next]==0){
                    dist[next] += dist[now]+1;
                    q.add(next);
                }
            }
        }
        int max = 0;
        for(int d:dist){
            max = Math.max(max, d);
        }
        int count = 0;
        for(int d:dist){
            if(d==max)count++;
        }
        
        
        return count;
    }
}