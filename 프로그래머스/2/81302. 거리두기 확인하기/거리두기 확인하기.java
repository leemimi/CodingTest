import java.util.*;
class Solution {
    static int n;
    static int m;
    static int[] dx = {0,0,-1,1};
    static int[] dy= {1,-1,0,0};
    public int[] solution(String[][] places) {
        List<Integer> answer = new ArrayList<>();
        n = places.length;
        m = places[0].length;
        for(String[] place : places){
            boolean isSafe = true;
            for(int i =0; i<n;i++){
                for(int j =0; j<m ;j++){
                    if(place[i].charAt(j)=='P'){
                        int ans = bfs(i,j,place);
                        if(ans==0){
                            isSafe = false;
                            break;
                        }
                    }
                }
            }
            if(isSafe){
                answer.add(1);
            }else{
                answer.add(0);
            }
    }
        
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
    public int bfs(int x, int y, String[] place){
        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{x,y,0});
        boolean[][] visited = new boolean[n][m];
        visited[x][y] = true;
        
        while (!q.isEmpty()){
            int[] tmp = q.poll();
            int cx = tmp[0];
            int cy = tmp[1];
            int dist = tmp[2];
            if (dist >2 ) continue;
            if (dist>0 && place[cx].charAt(cy)=='P') return 0;
            for(int i=0; i<4; i++){
                int nx = cx+ dx[i];
                int ny = cy +dy[i];
                if(nx>=0&&nx<n&& ny>=0 && ny<m && !visited[nx][ny]&& place[nx].charAt(ny)!='X'){
                    visited[nx][ny] = true;
                    q.offer(new int[]{nx,ny,dist+1});
                }
            }
            
        }
        
        return 1;
    }
}