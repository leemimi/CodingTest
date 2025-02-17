import java.util.*;
class Solution {
    public int solution(String[] babbling) {
        int answer = 0;
        
        String[] vaild = {"aya", "ye", "woo", "ma"};
        
        for(String word: babbling){
            boolean isVaild = true;
            String prev = "";
            
            for(String s: vaild){
                if(word.contains(s+s)){
                    isVaild = false;
                    break;
                }
                word = word.replace(s," ");
            }
            if(isVaild&&word.trim().isEmpty()){
                answer++;
            }
        }
        
        return answer;
    }
}