import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        ArrayList<Integer> answer = new ArrayList<>(); 
        int n = progresses.length;
        
        Stack<Integer> stack = new Stack<>();
        for(int i=0; i<n;i++){
            int day = 0;
            day = (100 - progresses[i])/speeds[i];
            int p = progresses[i] + speeds[i]*day;
            if(p<100){
                day+=1;
            }
            if(!stack.isEmpty()){
                if(stack.peek()>day){
                    stack.push(stack.peek());
                    continue;
                }else{
                    stack.push(day);
                }
            }else{
                stack.push(day);
            }
            
        }
        
        Integer[] list = stack.toArray(new Integer[0]);
        
        
        int prev = list[0];
        int cnt = 1;
        for(int i=1; i<list.length; i++){
            if(list[i] != prev){
                answer.add(cnt);
                cnt = 1;
                prev = list[i];
            }else{
            cnt++;
        }
    }
        answer.add(cnt);
        int[] arr = answer.stream().mapToInt(i->i).toArray();
        return arr;
    }
}