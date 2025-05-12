import java.util.*;
import java.io.*;

class Main {
    static int N;
    static boolean[][] apples;
    static Map<Integer, Character> directionChanges = new HashMap<>();
    static int[]dx = {0, 1, 0, -1};
    static int[] dy = {1,0,-1,0};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        // 보드 크기
        N = Integer.parseInt(br.readLine());

        // 사과 개수
        int K = Integer.parseInt(br.readLine());

        // 사과 위치 저장 (1-based)
        apples = new boolean[N + 1][N + 1];
        for (int i = 0; i < K; i++) {
            st = new StringTokenizer(br.readLine());
            int row = Integer.parseInt(st.nextToken());
            int col = Integer.parseInt(st.nextToken());
            apples[row][col] = true;
        }

        // 방향 변환 횟수
        int L = Integer.parseInt(br.readLine());

        // 방향 전환 정보 저장
        for (int i = 0; i < L; i++) {
            st = new StringTokenizer(br.readLine());
            int time = Integer.parseInt(st.nextToken());
            char dir = st.nextToken().charAt(0);
            directionChanges.put(time, dir);
        }

        int res = simulate();
        System.out.println(res);

    }
    public static int simulate(){
        Deque<int[]> snake = new LinkedList<>();
        snake.add(new int[]{1,1});

        boolean[][] visited = new boolean[N+1][N+1];
        visited[1][1]= true;

        int time = 0;
        int dir = 0;
        int x = 1,y=1;
        while (true){
            time++;
            int nx = x+dx[dir];
            int ny = y + dy[dir];
            if(nx<1 || nx > N || ny < 1||ny>N ||visited[nx][ny]) break;

            snake.addFirst(new int[]{nx,ny});
            visited[nx][ny] = true;

            if(apples[nx][ny]){
                apples[nx][ny] = false;
            }else{
                int[] tail = snake.removeLast();
                visited[tail[0]][tail[1]]= false;
            }

            if(directionChanges.containsKey(time)){
                char turn = directionChanges.get(time);
                if(turn == 'L'){
                    dir = (dir+3)%4;
                }else if(turn == 'D'){
                    dir = (dir+1)%4;
                }
            }
            x = nx;
            y = ny;
        }
        return time;
    }
}