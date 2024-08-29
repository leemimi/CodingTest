import java.util.*;
import java.io.*;

public class Main {
    public static void main (String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] arr = new int[N+1];
        for(int i=1;i<=N;i++){
            arr[i] = Integer.parseInt(br.readLine())+arr[i-1];
        }
        int ans =  0;
        for(int i=0;i<N;i++){
            for(int j=i+1;j<N;j++){
                int pre = Math.abs(arr[j] -arr[i]);
                int back = arr[N] - pre;
                int dist = Math.min(pre, back);
                ans = Math.max(dist,ans);
            }
        }
        System.out.println(ans);

    }
}