import java.util.*;
class Solution {
    static String[] orders;
    public String[] solution(String[] orders, int[] course) {
        List<String> answer = new ArrayList<>();
        this.orders = orders;
        
        
        for(int c: course){
            HashMap<String,Integer> map = new HashMap<>();
            for(String order: orders){
                char[] or = order.toCharArray();
                Arrays.sort(or);
                dfs(0,new StringBuilder(),map, or,c );
            }
            int max = 0;
            for(int val: map.values()){
                if(val>max){
                    max = val;
                }
            }
            for(String key: map.keySet()){
                if(map.get(key) == max && max>=2 ){
                    answer.add(key);
                }
            }
        }
        Collections.sort(answer);
        
        
        return answer.toArray(new String[0]);
    }
    public static void dfs(int idx, StringBuilder sb, HashMap<String,Integer> map, char[] or, int c){
        if(sb.length() == c ){
            map.put(sb.toString(), map.getOrDefault(sb.toString(),0)+1);
            return;
        }
        for(int i=idx; i<or.length;i++){
            sb.append(or[i]);
            dfs(i+1,sb,map,or,c);
            sb.deleteCharAt(sb.length()-1);
        }
        
    }
}