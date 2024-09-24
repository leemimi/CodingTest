import java.util.*;
class Solution {
    static int n;
    public int solution(int cacheSize, String[] cities) {
        int answer = 0;
        
        n = cities.length;
        Queue<String> q = new LinkedList<>();
        if(cacheSize == 0){
            return cities.length*5;
        } 
        
        for(String c: cities){
            c = c.toLowerCase();
            
            if(q.contains(c)){
                q.remove(c);
                q.offer(c);
                answer+=1;
            }else{
                if(q.size()==cacheSize){
                    q.poll();
                    q.offer(c);
                    answer+=5;
                }else{
                    q.offer(c);
                    answer+=5;
                }
            }
            
        }
        
        return answer;
    }
}