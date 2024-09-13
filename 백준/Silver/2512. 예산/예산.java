import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main (String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n];
        int lt =0;
        int rt=-1;
        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i=0; i<n;i++){
            arr[i] = Integer.parseInt(st.nextToken());
            rt = Math.max(arr[i], rt);
        }
        int m = Integer.parseInt(br.readLine());

        while(lt<=rt){
            long sums = 0;
            int mid = (lt+rt)/2;

            for(int i=0;i<n;i++){
                if(mid>arr[i]){
                    sums+=arr[i];
                }else{
                    sums += mid;
                }
            }
            if(sums<=m){
                lt = mid +1;
            }
            else{
                rt = mid -1;
            }
        }

        System.out.println(rt);

    }
}