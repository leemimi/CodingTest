import java.util.*;
class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 0;
        
        Queue<int[]> q = new LinkedList<>();
        int n = priorities.length;
        for(int i=0; i<n;i++){
            q.offer(new int[]{i, priorities[i]});
        }
        
        while(!q.isEmpty()){
            
            int[] current = q.poll();
            boolean flag = false;
            for(int[] job: q){
                if (job[1] > current[1]){
                    flag = true;
                }
            }
            
            if(flag){
                q.offer(current);
            }else{
                answer++;
                if(current[0]==location){
                    break;
                }
            }
            
            
        }
        
        
        return answer;
    }
}