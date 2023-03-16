import java.util.*;
import java.util.Collections;
class Solution {
    public long solution(long n) {
        long answer = 0;
        String s = Long.toString(n);
        int [] digits = new int[s.length()];
        for(int i =0; i<s.length();i++){
            digits[i] = s.charAt(i) - '0';
        }
        Integer[] arrs = Arrays.stream(digits).boxed().toArray(Integer[]::new);
        Arrays.sort(arrs, Collections.reverseOrder());
        
        for(Integer i:arrs){
            answer*=10;
            answer+=i;
        }
        
        
        return answer;
    }
}