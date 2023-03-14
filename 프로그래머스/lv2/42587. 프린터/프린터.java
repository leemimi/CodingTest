import java.util.*;
class Solution {
    public int solution(int[] priorities, int location) {
        PriorityQueue<Integer> q = new PriorityQueue<>(Collections.reverseOrder());
        //큐에 전부 넣기
        for(int i=0;i<priorities.length;i++){
            q.add(priorities[i]);
        }
        int cnt =0;
    
        while(!q.isEmpty()){
            for(int i =0; i<priorities.length;i++){
                if(priorities[i]==q.peek()){
                    if(location == i){
                        cnt++;
                        return cnt;
                }
                q.poll();
                cnt++; 
            }
        }
    }
        return -1;
    }   
}
