import java.util.*;
class Solution {
    public int[] solution(String[] gems) {
        int[] answer = {0, gems.length-1};
        HashSet<String> set = new HashSet<>(Arrays.asList(gems));
        Map<String, Integer> map = new HashMap<>();
        int n = gems.length;

        int total= set.size();
        int lt=0;
        int rt=0;
        int min = n;
        while(rt<n){
            map.put(gems[rt], map.getOrDefault(gems[rt],0)+1);
            rt++;
            while(map.size()  == total){
                if(rt-lt < min){
                    min = rt-lt;
                    answer[0] = lt;
                    answer[1] = rt-1;
                }
                map.put(gems[lt], map.get(gems[lt])-1);
                if(map.get(gems[lt])==0){
                    map.remove(gems[lt]);
                }
                lt++;
            }
            
        }
        
        return new int[]{answer[0]+1, answer[1]+1};
    }
}