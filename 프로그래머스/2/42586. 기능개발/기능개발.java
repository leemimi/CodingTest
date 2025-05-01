import java.util.*;
class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        List<Integer> answer = new ArrayList<>();
        int n = speeds.length;
        List<Integer> res = new ArrayList<>();
        for(int i=0; i<n ;i++){
            int a = (100 - progresses[i])/speeds[i];
            int b = (100 - progresses[i])%speeds[i];
            if(b>0) a+=1;
            res.add(a);
            
        }
        int now = res.get(0);
        int cnt = 0;
        for(int i=0;i<res.size();i++){
            if(res.get(i) > now){
                answer.add(cnt);
                cnt = 1;
                now = res.get(i);
            }else{
                cnt+=1;
            }
        }
        answer.add(cnt);
        
        
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}