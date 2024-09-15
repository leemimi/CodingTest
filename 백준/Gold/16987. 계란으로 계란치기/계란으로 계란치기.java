import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class Main {
    static int answer;
    static int[][]arr;
    static int n;
    public static void main (String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());
        arr = new int[n][2];

        for(int i=0; i<n;i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            arr[i] = new int[]{Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())};
        }
        answer = 0;
        dfs(0,0);
        System.out.println(answer);
    }
    static void dfs(int L, int cnt){
        if(L== n||cnt==n-1){
            answer = Math.max(answer, cnt);
            return;
        }
        if(arr[L][0]<=0){
            dfs(L+1,cnt);
        }else{
        for(int i=0;i<n;i++){
            if(i==L)continue;
            if(arr[i][0]>0){
                arr[i][0]-=arr[L][1];
                arr[L][0] -=arr[i][1];
                dfs(L+1,cnt+(arr[i][0]<=0?1:0)+(arr[L][0]<=0?1:0));
                arr[i][0]+=arr[L][1];
                arr[L][0] +=arr[i][1];
            }
        }
    }


    }
}