import java.util.*;

class Solution {
    public int[] solution(String[][] places) {
        int[] answer = new int[5];
        
        for(int k=0;k<places.length;k++){
            String[] tmp = places[k];
            boolean check = false;
            for(int i=0; i<5;i++){
                for(int j=0; j<5;j++){
                    if(tmp[i].charAt(j)=='P'){
                        if(bfs(i,j,tmp)) check = true;
                    }
                }
            }
            answer[k] = check ? 0:1; 
        }
        
        return answer;
    }
static boolean bfs(int x, int y, String[] p){
    Queue<int[]> q = new LinkedList<>();
    q.add(new int[]{x,y});
    
    int[] dx = {1,-1,0,0};
    int[] dy = {0,0,-1,1};
    
    while(!q.isEmpty()){
        int[] temp = q.poll();
        for(int i=0; i<4;i++){
            int nx = dx[i]+temp[0];
            int ny = dy[i] + temp[1];
        
        if((nx<0||ny<0||nx>=5||ny>=5)||(nx==x &&ny==y)){
            continue;
        }
        
        int m = Math.abs(x-nx)+Math.abs(y-ny);
        if(p[nx].charAt(ny)=='P'&&m<=2){
            return true;
        }else if(p[nx].charAt(ny)=='O'&&m<2){
            q.add(new int[]{nx,ny});
        }
    }
    }
            return false;
}
}