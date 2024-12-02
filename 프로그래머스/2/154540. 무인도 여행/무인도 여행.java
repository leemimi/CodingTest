import java.util.*;
class Solution {
    static boolean[][] visited;
    static char[][] map;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    public int[] solution(String[] maps) {
        List<Integer> answer = new ArrayList<>();
        int cnt =0;
        map = new char[maps.length][maps[0].length()];
        visited = new boolean[map.length][map[0].length];
        for(int i=0;i<maps.length;i++){
            map[i] = maps[i].toCharArray();
        }
        for(int i=0; i<map.length; i++){
            for(int j=0; j<map[0].length;j++){
                if(!visited[i][j] && map[i][j] != 'X'){
                    answer.add(bfs(i, j));
                }
            }
        }
        if(answer.size()==0){
            answer.add(-1);
        }
        Collections.sort(answer);
        
        int[] ans = answer.stream().mapToInt(Integer::intValue).toArray();
        
        return ans;
    }
    public static int bfs(int x, int y){
        int sum = 0;
        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{x,y});
        visited[x][y] = true;
        
        while(!q.isEmpty()){
            int cur[] = q.poll();
            int cx = cur[0];
            int cy = cur[1];
            
            sum+= map[cx][cy] - '0';
            for(int i=0;i<4;i++){
                int nx = cx+dx[i];
                int ny = cy +dy[i];
                if(nx<0||ny<0||nx >=map.length|| ny>=map[0].length)
                    continue;
                if(!visited[nx][ny]&&map[nx][ny]!='X'){
                    visited[nx][ny] = true;
                    q.offer(new int[]{nx,ny});
                }
            }
        }
        return sum;
    }
}