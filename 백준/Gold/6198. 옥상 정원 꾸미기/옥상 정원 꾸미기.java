import java.io.*;
import java.util.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        
        int[] heights = new int[n];
        
        for (int i = 0; i < n; i++) {
            heights[i] = Integer.parseInt(br.readLine());
        }
        Stack<Integer> stack = new Stack<>();
        long answer = 0;
        for(int i =0 ;i<n;i++){
            while(!stack.isEmpty()&& stack.peek()<=heights[i]){
                stack.pop();                
            }
            answer += stack.size();
            stack.push(heights[i]);
        }
        System.out.println(answer);

    }
}