import java.util.*;
class Solution {
    public int solution(int[] schedules, int[][] timelogs, int startday) {
        int answer = timelogs.length;
        
        
        for (int i = 0; i < schedules.length; i++) {
            int[] timelog = timelogs[i];
            int schedule = calc(schedules[i]);
            int day = startday;
            for(int log: timelog){
                if(day%7==0||day%7==6){
                    day++;
                    continue;
                }
            if(log > schedule){
                answer--;
                break;
            }
            day++;
        }
        
        }
        
        return answer;
    }
    public static int calc(int time) {
        time +=10;
        if(time%100 >=60){
            int h = (time / 100) +1;
            int m = (time%100) -60;
            time = (h*100)+m;
        }
        return time;
    }
}