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

        int[] arr = new int[N + 1];
        for (int i = 1; i <= N; i++) {
            arr[i] = Integer.parseInt(bf.readLine());
        }
        //System.out.println(Arrays.toString(arr));

        Stack<Integer> stack = new Stack<>();
        long sum = 0;
        stack.push(arr[1]);
        for (int i = 2; i <= N; i++) {
            while (!stack.isEmpty()&&stack.peek()<=arr[i]) {
                    stack.pop();
                }
            sum += stack.size();
            stack.push(arr[i]);
        }
        System.out.println(sum);
        }
    }