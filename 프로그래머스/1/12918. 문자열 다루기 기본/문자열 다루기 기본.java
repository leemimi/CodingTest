import java.util.*;
class Solution {
    public boolean solution(String s) {
        boolean answer = true;
        
        if(s.length() == 4 || s.length()==6){
            if (s.chars().allMatch(Character::isDigit)){
                return true;
            }
        }
        
        return false;
    }
}