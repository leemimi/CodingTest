import java.util.*;
class Solution {
    public long solution(int n, int[] works) {
        long answer = 0;
        PriorityQueue<Integer> pq = new PriorityQueue<>((a,b)->b-a);
        
        for(int w : works){
            pq.offer(w);
        }
        while(n>0 && !pq.isEmpty()){
            int x = pq.poll();
            x-=1;
            n-=1;
            if(x>0){
                pq.offer(x);
            }
            
        }
        if(pq.size()>0){
            for(int p:pq){
            answer += Math.pow(p,2);
            }
        }

        
        return answer;
    }
}