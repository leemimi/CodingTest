import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int n;
    static int m;
    static int[][] arr;
    static int answer = 0;
    public static void main (String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        arr = new int[n+1][m+1];
        dfs(0);
        System.out.println(answer);

    }
    static void dfs(int L){
        if(L == n*m){
            answer++;
            return;
        }
        int x = L/m+1;
        int y = L%m+1;

        dfs(L+1);

        if(arr[x-1][y]==0||arr[x][y-1]==0||arr[x-1][y-1]==0){
            arr[x][y] = 1;
            dfs(L+1);
            arr[x][y] = 0;
        }
    }
}
