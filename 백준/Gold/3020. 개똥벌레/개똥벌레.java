import java.io.IOException;
import java.io.*;
import java.util.*;
class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int H = Integer.parseInt(st.nextToken());
        int[] arr = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }
        int[] bottom = new int[N/2];
        int[] top = new int[N/2];

        for (int i = 0; i < N/2; i++) {
            bottom[i] = arr[i*2];
            top[i] = arr[i*2+1];
        }
        Arrays.sort(bottom);
        Arrays.sort(top);

        int min = N;
        int cnt =0;

        for(int h = 1; h<=H; h++){
            int bc = bottom.length - find(bottom, h);
            int tc = top.length - find(top, H-h+1);
            int total = bc + tc;
            if(total < min){
                min = total;
                cnt = 1;
                
            } else if(total==min){
                cnt++;
            }


        }
        System.out.println(min + " " + cnt);

    }
    static int find(int[] arr, int target){
        int lt = 0;
        int rt = arr.length;
        while(lt<rt){
            int mid = (lt+rt)/2;
            if(arr[mid] < target){
                lt = mid+1;
            }else{
                rt = mid;
            }
        }
        return lt;
    }
}