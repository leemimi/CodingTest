import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.sql.Time;
import java.util.*;

public class Main {
    static int n; // 층 수
    static int m; // 행 수
    public static void main (String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        int[] arr = new int[n];
        st = new StringTokenizer(br.readLine());

        int lt = 0;
        int rt = 0;
        for(int i = 0; i<n;i++){
            arr[i] = Integer.parseInt(st.nextToken());
            rt = Math.max(arr[i], rt);
        }

        int answer = rt;

        while(lt<=rt){
            int mid = (rt+lt)/2;
            if(isVaild(arr, mid)){
                answer = Math.min(answer, mid);
                rt = mid - 1;
            }else{
                lt = mid +1;
            }

        }
        System.out.println(answer);

    }
    static boolean isVaild(int[] arr, int mid){
        int cnt =1;
        int min = arr[0];
        int max = arr[0];

        for(int i=0; i<arr.length;i++){
            if(arr[i]<min) min = arr[i];
            if(arr[i]>max) max = arr[i];

            if(max-min>mid){
                cnt++;
                min = arr[i];
                max = arr[i];
            }
        }
        return cnt<=m;
    }
}