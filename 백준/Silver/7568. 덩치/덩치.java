import java.util.*;
import java.io.*;

public class Main {

    public static void main (String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int weight[] = new int[n];
        int height[] = new int[n];
        int rank[] = new int[n];

        for(int i=0; i<n;i++){
            weight[i] = sc.nextInt();
            height[i] = sc.nextInt();
        }

        for(int i=0; i<n;i++){
            int cnt = 1;

            for(int j=0; j<n;j++){
                if (weight[i]<weight[j] && height[i]<height[j]){
                    cnt+=1;
                }
            }
            rank[i] = cnt;
        }

        for(int i =0; i<n; i++){
            System.out.print(rank[i] + " ");
        }
    }
}