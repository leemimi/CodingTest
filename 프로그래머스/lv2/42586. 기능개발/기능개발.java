import java.util.*;
class Solution {
    public int[] solution(int[] progresses, int[] speeds) {

        Stack <Integer> stack = new Stack<>();
        List<Integer> ans = new ArrayList<>();
        
        int[] days= new int[progresses.length];
        
        for(int i=0;i<progresses.length;i++){
            int time = 100-progresses[i];
            int a = time/speeds[i];
            if(speeds[i]*a<time){
                days[i] = a+1;
            }else{
                days[i] = a;
            }
        }
        //System.out.println(Arrays.toString(days));
        
        stack.push(days[0]);
        int cnt =0;
        for(int i=1;i<days.length;i++){
            while(!stack.isEmpty()&&stack.peek()<days[i]){
                stack.pop();
                cnt++;
            }if(stack.isEmpty()){
                ans.add(cnt);
                cnt=0;
            }
            stack.push(days[i]);
        }
        
        if(!stack.isEmpty()){
            ans.add(stack.size()+cnt);
        }
        
        int[] answer = new int[ans.size()];
        for(int i=0;i<answer.length;i++){
            answer[i] = ans.get(i);
        }
        return answer;
        
    }
}
    
    