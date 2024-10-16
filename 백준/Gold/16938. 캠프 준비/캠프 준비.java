import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int n;
    static int l;
    static int r;
    static int x;
    static int[] arr;
    static boolean[] visited;
    static int answer;
    public static void main (String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        l = Integer.parseInt(st.nextToken());
        r = Integer.parseInt(st.nextToken());
        x = Integer.parseInt(st.nextToken());
        arr = new int[n];

        st = new StringTokenizer(br.readLine());
        for(int i=0;i<n;i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        answer = 0;
        visited = new boolean[n];
        Arrays.sort(arr);
        for(int i=2; i<=n; i++){
            dfs(0,i);
        }

        System.out.println(answer);
    }
    static void dfs(int L, int num){
        if(num == 0) {
            int sum = 0;
            int max = Integer.MIN_VALUE;
            int min = Integer.MAX_VALUE;

            for(int i=0; i<arr.length;i++){
                if(visited[i]){
                    sum += arr[i];
                    min = Math.min(min, arr[i]);
                    max = Math.max(max, arr[i]);
                }
            }
            if(l<= sum && sum<=r && (max-min) >=x ){
                answer++;
            }
            return;
        }
        for(int i=L; i<arr.length;i++){
            if(!visited[i]){
                visited[i] = true;
                dfs(i+1, num-1);
                visited[i] = false;
            }
        }

    }
}