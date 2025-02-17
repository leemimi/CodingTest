import java.util.*;
class Solution {
    public int solution(int n, int m, int[] section) {
        int answer = 0;
        
        int[] arr = new int[n];
        
        int now = section[0];
        for(int i =0; i<section.length;i++){
            if(section[i] > now + m -1){

                now = section[i];
                answer++;
            }
        }
        answer++;
        
        
        
        return answer;
    }
}