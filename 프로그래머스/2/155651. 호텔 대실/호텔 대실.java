import java.util.*;
class Solution {
    public int solution(String[][] book_time) {
        int answer = 0;
        List<int[]> times = new ArrayList<>();
        for(int i=0; i<book_time.length; i++){
            times.add(new int[]{revertTime(book_time[i][0]),revertTime(book_time[i][1])});
        }
        Collections.sort(times, (a,b)-> a[0]-b[0]);
    
        
        PriorityQueue<Integer> q = new PriorityQueue<>();
        for(int[] time : times){
            int start = time[0];
            int end = time[1];
            
            if(!q.isEmpty()&& q.peek()+10 <= start){
                q.poll();
            }
            q.offer(end);
        }
        
        answer = q.size();
        
        return answer;
    }
    public static int revertTime(String t){
        String[] time = t.split(":");
        return Integer.parseInt(time[0])*60 + Integer.parseInt(time[1]);
    }
}