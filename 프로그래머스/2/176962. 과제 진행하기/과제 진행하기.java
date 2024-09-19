import java.util.*;
class Solution {
    static Queue<Integer> q;
    static LinkedList<Task> task;
    
    
    public String[] solution(String[][] plans) {
        String[] answer = {};
        
        q = new LinkedList<>();
        task = new LinkedList<>();
        
        
        for(int i=0; i < plans.length; i++){
            int start = convert(plans[i][1]);
            int time = Integer.parseInt(plans[i][2]);
            task.add(new Task(plans[i][0], start, time));
        }
        
        task.sort((a,b)->a.start-b.start);
        
        Stack<Task> stack = new Stack<>();
        List<String> endTask = new ArrayList<>();
        Task now = task.poll();
        int time = now.start;
        
        
        while(!task.isEmpty()){
            time += now.left;
            
            Task next = task.peek();
            
            if(time>next.start){
                now.left = time - next.start;
                stack.push(now);
            }else{
                endTask.add(now.name);
                if(!stack.isEmpty()){
                    now = stack.pop();
                    continue;
                }
            }
            now = task.poll();
            time = now.start;
        }
        endTask.add(now.name);
        while(!stack.isEmpty()){
            endTask.add(stack.pop().name);
        }
        
        
        return endTask.toArray(new String[1]);
    }
    static Integer convert(String time){
        return Integer.parseInt(time.substring(0,2))*60 + Integer.parseInt(time.substring(3,5));
    }
    
    class Task{
        String name;
        int start;
        int left;
        
        Task(String name, int start, int left) {
            this.name = name;
            this.start = start;
            this.left = left;
        }
    }
}