import java.util.*;
class Solution {
    public int solution(int[] order) {
        int answer = 0;
        int now =0;
        Stack<Integer> container = new Stack<>();
        for(int i=1;i<=order.length;i++){
            if(i!=order[now]){
                container.push(i);
            }else if(i==order[now]){
                answer+=1;
                now +=1;
            }
            if(!container.isEmpty()&& container.peek() == order[now]){
                    container.pop();
                    answer+=1;
                    now+=1;
            }
        }
        while(true){
            if(!container.isEmpty()&&container.peek()==order[now]){
                container.pop();
                answer+=1;
                now+=1;
            }
            else{
                break;
            }
        }
        
        
        return answer;
    }
}