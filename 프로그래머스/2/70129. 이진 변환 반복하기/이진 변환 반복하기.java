import java.util.*;
class Solution {
    public int[] solution(String s) {
        int[] answer = new int[2];
        int zeronum = 0;
        int count = 0;
        while(!s.equals("1")){
            int len = s.length();
            s = s.replace("0","");
            zeronum += len - s.length();
            
            s = Integer.toBinaryString(s.length());
            count++;
            
        }
        answer[0] = count;
        answer[1] = zeronum;
        
        return answer;
    }
}