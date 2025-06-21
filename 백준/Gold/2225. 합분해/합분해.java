import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;

class Main {
    public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] input = br.readLine().split(" ");
		int N = Integer.valueOf(input[0]);
		int K = Integer.valueOf(input[1]);
		
		long [][]dp=new long [N+1][K+1];
		
		for(int i=1;i<=N;i++) {
			for(int j=1;j<=K;j++) {
				dp[i][j]=1; //최소 1개의 경우의 수는 있으므로 1개로 모두 초기화
				for(int k=1;k<=N;k++) {
					dp[i][j]+=dp[k][j-1]%1000000000;//구한 점화식
				}
			}
		}
		
		System.out.println(dp[N][K]%1000000000);
	}
}