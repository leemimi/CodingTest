import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken()); // 물품의 수
        int K = Integer.parseInt(st.nextToken()); // 버틸 수 있는 무게

        int[] W = new int[N + 1]; // 각 물건의 무게
        int[] V = new int[N + 1]; // 각 물건의 가치

        for (int i = 1; i <= N; i++) {
            st = new StringTokenizer(br.readLine());
            W[i] = Integer.parseInt(st.nextToken());
            V[i] = Integer.parseInt(st.nextToken());
        }

        int[][] dp = new int[N + 1][K+1];
        for(int i=1;i<=K;i++){
            for(int j=1; j<=N;j++){
                dp[j][i] = dp[j-1][i];
                if(i-W[j]>=0){
                    dp[j][i] = Math.max(dp[j-1][i], dp[j-1][i-W[j]]+V[j]);
                }
            }
        }
        System.out.println(dp[N][K]); // 최대 가치 출력
    }
}