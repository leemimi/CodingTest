import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.sql.Time;
import java.util.*;

public class Main {
    static int l; // 층 수
    static int r; // 행 수
    static int c;
    static int[] dl = {0,0,0,0,-1,1};
    static int[] dx = {-1,1,0,0,0,0};
    static int[] dy = {0,0,-1,1,0,0};
    static char[][][] arr;
    static int ex;
    static int ey;
    static int eu;
    static int sx;
    static int sy;
    static int sz;
    public static void main (String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        while(true) {
            StringTokenizer st = new StringTokenizer(br.readLine());

            l = Integer.parseInt(st.nextToken());
            r = Integer.parseInt(st.nextToken());
            c = Integer.parseInt(st.nextToken());

            arr = new char[l][r][c];

            if(l==0 && r== 0 && c==0)return;

            for(int i =0; i<l;i++){
                for(int j=0; j<r;j++){
                    String str = br.readLine();
                    for(int k=0; k<c; k++){
                        arr[i][j][k] = str.charAt(k);

                        if(arr[i][j][k]== 'S'){
                            sx = j;
                            sy = k;
                            sz = i;
                        }
                        if(arr[i][j][k] == 'E'){
                            ex = j;
                            ey = k;
                            eu = i;
                        }
                    }
                }
                br.readLine();
        }
            bfs(sx,sy,sz);
        }
    }
    static void bfs(int x, int y, int u){
        Queue<int[]> q = new LinkedList<>();
        boolean[][][] visited = new boolean[l][r][c];
        q.offer(new int[]{x,y,u,0});
        visited[u][x][y] = true;

        while(!q.isEmpty()){
            int[] now = q.poll();
            if(now[0] == ex&& now[1]== ey&& now[2]==eu){
                System.out.println("Escaped in "+ now[3]+" minute(s).");
                return;
            }
            for(int i=0;i<6;i++){
                int nx = now[0]+dx[i];
                int ny = now[1]+dy[i];
                int nz = now[2]+dl[i];

                if(nz>=0&&nx>=0&&ny>=0&&nz<l&&nx<r&&ny<c&&arr[nz][nx][ny]!='#'){
                    if(!visited[nz][nx][ny]){
                        visited[nz][nx][ny]=true;
                        q.offer(new int[]{nx,ny,nz,now[3]+1});
                    }
                }
            }
        }
        System.out.println("Trapped!");

    }
}