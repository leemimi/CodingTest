import java.util.*;
class Solution {
    static int n,m;
    static int[] arr;
    
    public int solution(int[][] land) {
        int answer = 0;

        n = land.length;
        m = land[0].length;
        arr = new int[m];
        
        boolean[][] visited = new boolean[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (land[i][j] == 1 && visited[i][j] == false) {
                    bfs(land, visited, i, j);
                }
            }
        }
        answer = Arrays.stream(arr).max().getAsInt();
        System.out.println(answer);
        
        return answer;
    }
    public static void bfs(int[][] land, boolean[][] visited, int x,int y){
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{x, y});
        visited[x][y] = true;
        int[] dx = {0,0,-1,1};
        int[] dy = {-1,1,0,0};
        
        int cnt = 1;
        
        Set<Integer> set = new HashSet<>();
        
        while(!q.isEmpty()){
            int[] now = q.poll();
            set.add(now[1]);
            
            for(int i=0; i<4; i++){
                int nx = dx[i] + now[0];
                int ny = dy[i] + now[1];
                
                if(nx<0||ny<0||nx>=n||ny>=m) continue;
                if(land[nx][ny] == 1 && visited[nx][ny]== false){
                    q.add(new int[]{nx,ny});
                    visited[nx][ny] = true;
                    cnt++;
                }
            }
        }
        for(int idx: set){
            arr[idx] += cnt;
        }
    }
}