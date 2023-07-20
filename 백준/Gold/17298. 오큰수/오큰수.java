import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Scanner;
import java.util.Stack;
import java.util.StringTokenizer;


public class Main {
    public static void main (String[] args) throws IOException {

        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(bf.readLine());

        StringTokenizer st = new StringTokenizer(bf.readLine());
        int[] ans = new int[N];
        int[] arr = new int[N];


        for(int i= 0; i<N;i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }

        Stack<Integer> stack = new Stack<>();

        for (int i = 0; i < N; i++) {
            while (!stack.isEmpty()&&arr[stack.peek()]<arr[i]) {
                    ans[stack.peek()] = arr[i];
                    stack.pop();
            }
            stack.push(i);
        }

        while(!stack.isEmpty()){
            ans[stack.peek()] = -1;
            stack.pop();
        }


        StringBuilder sb = new StringBuilder();
        for(int i=0; i<N; i++){
            sb.append(ans[i]).append(" ");
        }

        System.out.println(sb.toString());
    }
}
