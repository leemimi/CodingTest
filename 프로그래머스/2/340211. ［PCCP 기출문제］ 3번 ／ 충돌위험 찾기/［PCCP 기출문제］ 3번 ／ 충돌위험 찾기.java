import java.util.*;
class Solution {
    static Queue<int[]>[] q;
    static int n;
    static int answer;
    public int solution(int[][] points, int[][] routes) {
        answer = 0;
        n = routes.length;
        q = new LinkedList[n];
        
        for(int i=0; i<n;i++){
            q[i] = new LinkedList<>();
        }
        calRoute(points, routes);
        cal();
        
        return answer;
    }
    static void calRoute(int[][] points, int[][] routes){
        for(int i=0; i<n;i++){
            int[] point = points[routes[i][0] - 1];
            int x = point[0];
            int y = point[1];
            
            q[i].add(new int[]{x,y});
            for(int j =1; j<routes[0].length;j++){
                int[] npoint = points[routes[i][j]-1];
                int nx = npoint[0];
                int ny = npoint[1];
                
                int xx = nx - x;
                int yy = ny - y;
                
                while(xx!=0){
                    if(xx>0){
                        xx--;
                        x++;
                        q[i].add(new int[]{x,y});
                    }else{
                        xx++;
                        x--;
                        q[i].add(new int[]{x,y});
                    }
                }
                while(yy!=0){
                    if(yy>0){
                        yy--;
                        y++;
                        q[i].add(new int[]{x,y});
                    }else{
                        yy++;
                        y--;
                        q[i].add(new int[]{x,y});
                    }
                }
                
            }
        }
    }
    static void cal(){
        int cnt = 0;
        
        while(cnt!=n){
            int[][] map = new int[101][101];
            cnt = 0;
            
            for(int i=0; i<n;i++){
                if(q[i].isEmpty()){
                    cnt++;
                    continue;
                }
                int[] tmp = q[i].poll();
                map[tmp[0]][tmp[1]]++;
            }
            for(int i=0; i<101; i++){
                for(int j=0; j<101;j++){
                    if(map[i][j]>=2){
                        answer++;
                    }
                }
            }
            
        }
    }
}