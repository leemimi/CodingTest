import java.util.*;
class Solution {
    static HashMap<String, Integer> map;
    static HashMap<String, Integer> wmap;
    static List<String> keys;
    public int solution(String[] want, int[] number, String[] discount) {
        int answer = 0;
        
        map = new HashMap<>();
        wmap = new HashMap<>();
        for(int i=0; i<10;i++){
            map.put(discount[i], map.getOrDefault(discount[i],0)+1 );
        }
        
        for(int i=0; i<want.length;i++){
            wmap.put(want[i], number[i]);
        }
        
        keys = Arrays.asList(want);
        if(solve())answer++;
        for(int i=10; i<discount.length;i++){
            map.put(discount[i-10], map.get(discount[i-10])-1);
            map.put(discount[i], map.getOrDefault(discount[i],0)+1);
            if(solve())answer++;
        }
        
        
        return answer;
    }
    public static boolean solve(){
        for(String key: keys){
            if(map.getOrDefault(key,0)<wmap.get(key))return false;
        }
            return true;
    }
}