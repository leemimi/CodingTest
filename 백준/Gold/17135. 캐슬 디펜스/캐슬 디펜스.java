import java.io.*;
import java.util.*;

public class Main {
    static int N, M, D;
    static int[][] map;       // 원본 맵
    static List<int[]> enemies = new ArrayList<>(); // 초기 적 좌표 저장용 (선택)
    static List<int[]> combi = new ArrayList<>();
    static int min = 0;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        // N: 행, M: 열, D: 공격 거리
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken()); // 행 수
        M = Integer.parseInt(st.nextToken()); // 열 수
        D = Integer.parseInt(st.nextToken()); // 공격 거리

        map = new int[N][M];


        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
                
                // 필요 시 적의 초기 위치 저장
                if (map[i][j] == 1) {
                    enemies.add(new int[]{i, j});
                }
            }
        }
        //궁수 위치 조합
        combination(0,0,new int[3]);
        //조합별로 공격 최댓값 구하기
        min = 0;
        for (int[] soldier : combi) {
            attack(soldier);
        }
        System.out.println(min);


    }
    public static void combination(int L, int start, int[] visited){
        if(L==3){
            combi.add(visited.clone());
            return;
        }
        for(int i=start;i<M;i++){
            visited[L]= i;
            combination(L+1, i+1, visited);
        }
    }
    public static void attack(int[] soldier){
        int[][] arr = new int[N][M];
        for (int i = 0; i < N; i++) {
            arr[i] = map[i].clone();
        }
    
        int kill = 0;
        for (int t = 0; t < N; t++) {
            Set<String> target = new HashSet<>();
    
            for (int s : soldier) {
                int minDist = D + 1;
                int row = -1, col = -1;
    
                for (int i = N - 1 - t; i >= 0; i--) {
                    for (int j = 0; j < M; j++) {
                        if (arr[i][j] == 1) {
                            int dist = Math.abs(N - t - i) + Math.abs(s - j);
                            if (dist <= D) {
                                if (dist < minDist || (dist == minDist && j < col)) {
                                    row = i;
                                    col = j;
                                    minDist = dist;
                                }
                            }
                        }
                    }
                }
    
                if (row != -1) {
                    target.add(row + "," + col);
                }
            }
    
            // 적 제거
            for (String pos : target) {
                String[] parts = pos.split(",");
                int r = Integer.parseInt(parts[0]);
                int c = Integer.parseInt(parts[1]);
                arr[r][c] = 0;
            }
    
            kill += target.size();
        }
    
        min = Math.max(min, kill); // 조합별 최대 킬 수 반영
    }
    
}
