import java.util.*;
class Solution {
    static int n;
    static int m;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    static String[] board;
    public int solution(String[] b) {
        int answer = 0;
        board = b;
        n = board.length;
        m = board[0].length();
        for(int i=0; i<n;i++){
            for(int j=0; j<m; j++){
                if(board[i].charAt(j)=='R'){
                    return bfs(i,j);
                }
            }
        }
        
        return -1;
    }
    public static int bfs(int x,int y){
        Queue<int[]> q = new LinkedList<>();
        int[][] visited =  new int[n][m];
        
        q.offer(new int[]{x,y});
        visited[x][y] = 1;
        
        
        
        while(!q.isEmpty()){
            int[] tmp = q.poll();
            
            for (int i = 0; i < 4; i++) {
            int nx = tmp[0];
            int ny = tmp[1];
            
            // 벽이나 경계를 만날 때까지 이동
            while (0 <= nx + dx[i] && nx + dx[i] < n && 0 <= ny + dy[i] && ny + dy[i] < m
                   && board[nx + dx[i]].charAt(ny + dy[i]) != 'D') {
                nx += dx[i];
                ny += dy[i];
            }
            
            if (visited[nx][ny] == 0) {
                visited[nx][ny] = visited[tmp[0]][tmp[1]] + 1;
                if (board[nx].charAt(ny) == 'G') {
                    return visited[nx][ny] - 1;
                }
                q.offer(new int[]{nx, ny});
            }
        }
    }
        return -1;
    }
}