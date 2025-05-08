import java.util.*;
class Solution {
    public int solution(int n, int[][] costs) {
        int answer = 0;
        
        
        List<List<int[]>> graph = new ArrayList<>();
        for(int i=0; i<n;i++){
            graph.add(new ArrayList<>());
        }
        for(int i=0; i<costs.length;i++){
            graph.get(costs[i][0]).add(new int[]{costs[i][1], costs[i][2]});
            graph.get(costs[i][1]).add(new int[]{costs[i][0], costs[i][2]});
        }
        
        
        boolean[] visited = new boolean[n];
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a->a[1]));
        pq.addAll(graph.get(0));
        int cnt = 1;
        visited[0] = true;
        while(!pq.isEmpty()){
            int[] nodes = pq.poll();
            
            if(visited[nodes[0]])continue;
            visited[nodes[0]] = true;
            answer += nodes[1];
            System.out.println(answer);
            if(check(visited)) break;
            
            for(int[] next: graph.get(nodes[0])){
                if(!visited[next[0]]){
                    pq.offer(next);
                }
            }
        }
        System.out.println(answer);
        return answer;
    }
    public static boolean check(boolean[] v){
        for(boolean i:v){
            if(i==false) return false;
        }
        return true;
    }
}