import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main (String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        long[] arr = new long[n+1];
        long[] dp = new long[n+1];
        StringTokenizer st = new StringTokenizer(br.readLine());
        arr[0] = 0L;
        for(int i=1; i<=n;i++){
            arr[i] = Long.parseLong(st.nextToken());

        }
        dp[1] = 0;
        for(int i=2;i<=n;i++){
            dp[i] = Long.MAX_VALUE;
            for(int j=1;j<i;j++){
                long a = Math.max((i-j)*(1+Math.abs(arr[j]-arr[i])),dp[j]);
                dp[i] = Math.min(a,dp[i]);
            }
        }
        System.out.println(dp[n]);
    }
}
