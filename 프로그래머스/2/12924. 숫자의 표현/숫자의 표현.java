import java.util.*;
class Solution {
    public int solution(int n) {
        int answer = 0;
        
        LinkedList<Integer[]> arr = new LinkedList<>();
        
        for(int i=1; i*(i-1)/2<n;i++){ 
            if((n-(i*(i-1)/2))%i==0){
                answer++;
            }
            
                
            }
        
        
        
        
        return answer;
    }
}