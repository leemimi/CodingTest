import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] nums = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }
        long[][] dp = new long[N][21];
        
        int last = nums[N-1];
        dp[0][nums[0]]=1;
        for(int i=1;i<N-1;i++){
            for(int j=0;j<=20;j++){
                if(j+nums[i]<=20){
                    dp[i][j+nums[i]]+= dp[i-1][j];
                }
                if(j-nums[i]>=0){
                    dp[i][j-nums[i]] += dp[i-1][j];
                }
            }
        }
        System.out.println(dp[N-2][last]);

    }
}