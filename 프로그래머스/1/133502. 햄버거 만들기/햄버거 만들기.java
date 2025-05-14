import java.util.*;
class Solution {
    public int solution(int[] ingredient) {
        int answer = 0;
        int[] find = {1,2,3,1};
        Stack<Integer> stack = new Stack<>();
        int n = ingredient.length;
        for(int i: ingredient){
            stack.push(i);
            
            if(stack.size()>=4){
                int m = stack.size();
                if(stack.get(m-4)==1 && stack.get(m-3)==2 && stack.get(m-2)==3 && stack.get(m-1)==1){
                    for(int j=0;j<4;j++){
                        stack.pop();
                    }
                    answer++;
                }
                
            }
        }
        
        return answer;
    }
}