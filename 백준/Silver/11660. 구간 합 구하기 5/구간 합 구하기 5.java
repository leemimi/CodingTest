import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main (String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());

        //원본 배열 저장
        long [][]arr = new long[a+1][a+1];
        for(int i=1;i<=a;i++){
            st = new StringTokenizer(br.readLine());
                for(int j=1;j<=a;j++){
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        //구간합 배열 저장
        long [][]sumArr = new long[a+1][a+1];
        for(int i=1;i<=a;i++){
            for(int j=1;j<=a;j++){
                sumArr[i][j] = sumArr[i][j-1]+sumArr[i-1][j] -sumArr[i-1][j-1]+arr[i][j];
            }
        }
        for(int i=0;i<b;i++) {
            st = new StringTokenizer(br.readLine());
            int x1 = Integer.parseInt(st.nextToken());
            int y1 = Integer.parseInt(st.nextToken());
            int x2 = Integer.parseInt(st.nextToken());
            int y2 = Integer.parseInt(st.nextToken());
            long result = sumArr[x2][y2] - sumArr[x1 - 1][y2] - sumArr[x2][y1 - 1] + sumArr[x1 - 1][y1 - 1];
            System.out.println(result);
        }
    }
}
