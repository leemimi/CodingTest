import java.util.*;
class Solution {
    public int[] solution(int[] prices) {
        int n= prices.length;
        int[] answer = new int[n];

        Stack<int[]> stack = new Stack<>();
        for(int i=0;i<n;i++){
            for(int[] s:stack){
                answer[s[0]] += 1;
            }
            while(!stack.isEmpty() && stack.peek()[1] > prices[i]){
                stack.pop();
            }
            stack.push(new int[]{i, prices[i]});
        }
        
        return answer;
    }
}