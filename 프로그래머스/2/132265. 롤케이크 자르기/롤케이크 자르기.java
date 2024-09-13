import java.util.*;
class Solution {
    
    public int solution(int[] topping) {
        int answer = 0;
        
        HashMap<Integer,Integer> map1 = new HashMap<>();
        HashMap<Integer,Integer> map2 = new HashMap<>();
        int n = topping.length;
        
        map1.put(topping[0],1);
        
        for(int i=1;i<n;i++){
            map2.put(topping[i], map2.getOrDefault(topping[i],0)+1);
        }
        int p = 1;
        
        
        while(p<n-1){
            if(map1.size()==map2.size()){
                answer++;
            }
            int key = topping[p];
            map1.put(key, map1.getOrDefault(key, 0)+1);
            
            if(map2.get(key)==1){
                map2.remove(key);
            }else{
                map2.put(key, map2.get(key)-1);
            }
            p++;
        }
        
        return answer;
    }
}