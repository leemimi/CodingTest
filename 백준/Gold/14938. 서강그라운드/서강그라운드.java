import java.io.*;
import java.util.*;
class Main {
    static final int INF = 100000000;
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(reader.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int r = Integer.parseInt(st.nextToken());

        int[] arr = new int[n]; //각 구역 아이템의 수
        st = new StringTokenizer(reader.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        ArrayList<int[]>[] graph = new ArrayList[n];
        for(int i=0; i<n;i++){
            graph[i]=new ArrayList<>();
        }

        for (int i = 0; i < r; i++) {
            st = new StringTokenizer(reader.readLine());
            int a = Integer.parseInt(st.nextToken()) - 1;
            int b = Integer.parseInt(st.nextToken()) - 1;
            int l = Integer.parseInt(st.nextToken());
            graph[a].add(new int[]{b, l});
            graph[b].add(new int[]{a, l});
        }

        
        int answer = 0;
        for(int i=0; i<n ;i++){
            int[] dist = new int[n];
            Arrays.fill(dist, INF);
            dijkstra(i, graph, dist);
            int sum = 0;
            for(int j=0; j<n;j++){
                if(dist[j] <= m){
                    sum += arr[j];
                }
            }
            answer = Math.max(answer, sum);
        }
        System.out.println(answer);
    
    }
    public static void dijkstra(int start, ArrayList<int[]>[] graph, int[] dist){
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a->a[1]));
        pq.offer(new int[]{start, 0});
        dist[start] = 0;

        while(!pq.isEmpty()){
            int[] cur = pq.poll();
            int now = cur[0];
            int cost = cur[1];

            if(dist[now] < cost) continue;
            for(int[] next: graph[now]){
                int nextNode = next[0];
                int nextCost = next[1];

                if(dist[nextNode] > dist[now]+ nextCost){
                    dist[nextNode] = dist[now]+nextCost;
                    pq.offer(new int[]{nextNode, dist[nextNode]});
                }
            }
        }
    } 
}
