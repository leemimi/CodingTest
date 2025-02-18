import java.util.*;
class Solution {
    public int solution(int[] players, int m, int k) {
        PriorityQueue<int[]> q = new PriorityQueue<>((o1,o2)-> o1[0] - o2[0]);
        int answer = 0;
        
        int now = 0; //현재 서버 갯수
        for(int i=0; i<24;i++){
            while(!q.isEmpty()&&q.peek()[0]==i){
                now -= q.poll()[1];
            }
            int need = players[i]/m;
            int more = now - need;
            if(more<0){
                more = -more;
                now += more;
                answer += more;
                q.add(new int[]{i+k, more});
            }
        }
        return answer;
    }
}