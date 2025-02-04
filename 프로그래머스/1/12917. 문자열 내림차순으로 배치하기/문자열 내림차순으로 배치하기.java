import java.util.*;
import java.util.Collections;
class Solution {
    public String solution(String s) {
        String answer = "";
        
        String[] str = s.split("");
        Arrays.sort(str,Collections.reverseOrder());
    
        
        return String.join("", str);
    }
}