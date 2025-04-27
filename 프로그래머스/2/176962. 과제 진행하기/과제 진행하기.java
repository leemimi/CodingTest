import java.util.*;
class Solution {
    public String[] solution(String[][] plans) {
        String[] answer = {};
        
        Arrays.sort(plans, (a,b) -> time(a[1]) - time(b[1]));
        
        for(String[] p: plans){
            System.out.println(p[1]);
        }
        Queue<String[]> q = new LinkedList<>();
        int n = plans.length;
        
        for(int i =0; i<n; i++){
            plans[i][1] = String.valueOf(time(plans[i][1]));
            q.offer(plans[i]);
        }
        
        Stack<String[]> stack = new Stack<>();
        int nowTime = Integer.parseInt(q.peek()[1])+Integer.parseInt(q.peek()[2]);
        List<String> res = new ArrayList<>();
        while(!q.isEmpty()){
            String[] now = q.poll();
            String name = now[0];
            int st = Integer.parseInt(now[1]);
            int d = Integer.parseInt(now[2]);
            
            if(!q.isEmpty()){
                int nextTime = Integer.parseInt(q.peek()[1]);
                
                if(st+d <= nextTime){
                    res.add(name);
                    nowTime = st+d;
                    
                    while(!stack.isEmpty()){
                        String[] p = stack.pop();
                        String pname = p[0];
                        int ptime = Integer.parseInt(p[1]);
                        
                        if(nowTime+ptime <= nextTime){
                            res.add(pname);
                            nowTime += ptime;
                        }else{
                            p[1] = String.valueOf(ptime-(nextTime - nowTime));
                            stack.push(p);
                            break;
                        }
                    }
                }else{
                    String[] p = new String[]{name, String.valueOf(d- (nextTime-st))};
                    stack.push(p);
                }
            }else{
                res.add(name);
                while (!stack.isEmpty()) {
                    res.add(stack.pop()[0]);
                }
            }
            
        }
        
        
        return res.toArray(new String[0]);
    }
    private static int time(String t){
        String[] tt = t.split(":");
        return Integer.parseInt(tt[0])*60 + Integer.parseInt(tt[1]);
    }
}