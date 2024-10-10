import java.util.*;
class Solution {
    boolean solution(String s) {
        boolean answer = true;
        
        Stack<Character> stack = new Stack<>();
        for(Character k:s.toCharArray()){
            if(k == '(') stack.push('(');
            else{
                if(stack.isEmpty()) return false;
                stack.pop();
            }
        }
        if(!stack.isEmpty()) answer = false;

        return answer;
    }
}