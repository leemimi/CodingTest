import java.util.*;
class Solution {
    public int solution(int[] A, int[] B) {
        int answer = 0;
        PriorityQueue<Integer> pq = new PriorityQueue<>((a,b)-> b-a);
        PriorityQueue<Integer> apq = new PriorityQueue<>((a,b)-> b-a);
        for(int i=0;i<B.length;i++){
            pq.offer(B[i]);
        }
        for(int i=0; i<A.length;i++){
            apq.offer(A[i]);
        }
        
        for(int i=0; i<A.length;i++){
            int b = pq.poll();
            int a = apq.poll();
            if(a<b) answer ++;
            else if(a >= b){
                pq.offer(b);
            }
        }
        
        
        return answer;
    }
}