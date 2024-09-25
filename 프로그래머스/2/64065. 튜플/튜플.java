import java.util.*;
class Solution {
    public int[] solution(String s) {
        int[] answer = {};
        s = s.substring(2, s.length()-2);
        
        String[] srr = s.split("\\},\\{");

        
        Map<String, Integer> map = new HashMap<>();
        
        for(String r: srr){
            String[] nums = r.split(",");
            for(String num: nums ){
                map.put(num, map.getOrDefault(num,0)+1);
            }
        }
        
        List<String> list = new ArrayList<>(map.keySet());
        
        list.sort((s1,s2)-> map.get(s2)-map.get(s1)); //내림차순
        
        answer = new int[list.size()];
        
        for(int i=0;i<answer.length;i++){
            answer[i] = Integer.parseInt(list.get(i));        
        }
        
        
        return answer;
    }
}