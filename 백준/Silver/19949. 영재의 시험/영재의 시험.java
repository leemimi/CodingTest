import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int n;
    static int m;
    static int[][] arr;
    static int[] answer;
    static int[] yj;
    static int ans;
    public static void main (String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        answer = new int[10];
        yj = new int[10];

        for (int i = 0; i < 10; i++) {
            answer[i] = Integer.parseInt(st.nextToken());
        }

        ans = 0;
        dfs(0);
        System.out.println(ans);
    }
    static void dfs(int L){
        if(L==10){
            int cnt = 0;
            for(int i=0; i<10;i++){
                if(answer[i] == yj[i]){
                    cnt++;
                }
            }
            if(cnt>=5){
                ans++;
            }
            return;
        }
        for(int i=1; i<=5;i++){
            if(L>=2){
                if(yj[L-1]==i && yj[L-2] == i) continue;
            }
            yj[L] = i;
            dfs(L+1);
        }
    }
}
