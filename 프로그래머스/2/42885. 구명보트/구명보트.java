import java.util.*;
class Solution {
    public int solution(int[] people, int limit) {
        int answer = 0;
        Integer[] sp = new Integer[people.length];
        
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        
        for(int i=0; i<people.length;i++){
            sp[i] = people[i];
        }
        Arrays.sort(sp,Collections.reverseOrder());
        
        for(int p:sp){
            if(pq.isEmpty()){
                if((limit-p)>=40)pq.add(limit-p);
                answer++;
            }else{
                if(pq.peek()>=p){
                    pq.poll();
                }else{
                    if((limit-p)>=40)pq.add(limit-p);
                    answer++;
                }
            }
        }
        
        
        return answer;
    }
}