import java.util.*;
class Solution {
    public int solution(int[] topping) {
        int answer = 0;
        int n = topping.length;
        Map<Integer,Integer> map = new HashMap<>();
        Set<Integer> lt = new HashSet<>();
        for(int i=0; i<n;i++){
            map.put(topping[i], map.getOrDefault(topping[i],0)+1);
        }
        
        for(int i=0;i<n;i++){
            int t = topping[i];
            
            lt.add(t);
            map.put(t, map.get(t)-1);
            if(map.get(t)==0){
                map.remove(t);
            }
            if(map.size() == lt.size()) answer++;
        }
        
        return answer;
    }
}