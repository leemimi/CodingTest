import java.util.*;
class Solution {
    public int solution(int[] players, int m, int k) {
        int answer = 0;
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a->a[0]));
        int cnt = 0;
        int now = 0;
        for(int i=0; i<24;i++){
            while(!pq.isEmpty()&&pq.peek()[0]==i){
                now -= pq.poll()[1];
            }
            int need = players[i]/ m;
            int diff = now - need;
            
            if(diff<0){
                diff = -diff;
                now += diff;
                cnt+=diff;
                pq.offer(new int[]{i+k, diff});
                
            }
        }
        
        return cnt;
    }
}
