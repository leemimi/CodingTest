import java.util.*;
class Solution {
    public String solution(int n) {
        
        String answer = "";
        String[] numbers = {"4","1","2"};

        
        while(n>0){
            answer+=numbers[n%3];
            if (n%3==0){--n;}
            n=n/3;
        }
        System.out.println(answer);
        StringBuffer sb = new StringBuffer(answer);
        sb.reverse();
        return sb.toString();
    }
}