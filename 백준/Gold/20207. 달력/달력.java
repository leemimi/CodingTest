import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int n;

    public static void main (String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        int[] arr = new int[366];
        int max_h = 0;
        for(int i=0; i<n;i++){
            st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());
            for(int j=s;j<=e;j++){
                arr[j]++;
            }
        }

        int sum = 0;
        int width = 0;
        for(int i=0;i<=365;i++){
            if(arr[i]==0){
                sum+=max_h*width;
                max_h=width=0;
                continue;
            }
            width++;
            max_h = Math.max(max_h, arr[i]);
        }
        sum+= max_h * width;
        System.out.println(sum);


    }
}
