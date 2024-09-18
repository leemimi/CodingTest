import java.util.*;
class Solution {
    public int solution(String[][] clothes) {
        int answer = 1;
        
        HashMap<String,Integer> map = new HashMap<>();
        int n = clothes.length;
        for(int i=0; i<n ;i++){
            map.put(clothes[i][1], map.getOrDefault(clothes[i][1],0)+1);
        }
        for(String key: map.keySet()){
            answer *= (map.get(key)+1);
        }
        
        answer-=1;
        
        return answer;
    }
}