import java.util.*;
class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        
        HashMap<String, Integer> dict = new HashMap<>();
        for(String par : participant){
            dict.put(par, dict.getOrDefault(par,0)+1);
        }
        
        for(String com : completion){
            if(dict.get(com)>0){
                dict.put(com, dict.get(com)-1);
            }
        }
        
        for(Map.Entry<String,Integer> entry:dict.entrySet() ){
            if(entry.getValue() > 0){
                answer = entry.getKey();
                break;
            }
        }
        
        return answer;
    }
}