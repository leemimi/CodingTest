import java.io.*;
import java.util.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(reader.readLine());
        int D = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(st.nextToken());
        int[] oven = new int[D];
        st = new StringTokenizer(reader.readLine());
        for (int i = 0; i < D; i++) {
            oven[i] = Integer.parseInt(st.nextToken());
        }
        int[] pizza = new int[n];
        st = new StringTokenizer(reader.readLine());
        for (int i = 0; i < n; i++) {
            pizza[i] = Integer.parseInt(st.nextToken());
        }
        int last = D-1;

        for(int i=1;i<D;i++){
            oven[i] = Math.min(oven[i], oven[i-1]);
        }

        for(int p:pizza){
            while(last>=0 && oven[last]<p){
                last--;
            }
            if(last < 0){
                System.out.println(0);
                return;
            }
            last--;
        }


        System.out.println(last+2);


    }
}