import java.util.*;
class Solution {
    public String solution(int n) {
        StringBuilder answer = new StringBuilder();
        String alp = "124";
        
        while(n>0){
            int tmp = n%3;
            if(tmp ==0){
                answer.insert(0,"4");
                n = n/3 -1;
            }else{
                answer.insert(0, Integer.toString(tmp));
                n = n/3;
            }
        }     
        
        
        return answer.toString();
    }
}

