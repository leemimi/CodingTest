class Solution {
    boolean solution(String s) {
        boolean answer = true;
        s = s.toUpperCase();
        
        answer = s.chars().filter(e->'P'==e).count() == s.chars().filter(e->'Y'==e).count();
        

        return answer;
    }
}
