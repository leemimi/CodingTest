import java.util.*;
class Solution {
    public String solution(int n, int t, int m, String[] timetable) {
        String answer = "";
        
        List<Integer> times = new ArrayList<>();
        for(String tt: timetable){
            times.add(timeToMinute(tt));
        }
        Collections.sort(times);
        Queue<Integer> q = new LinkedList<>();
        int start = timeToMinute("09:00");
        int crew = 0;
        int last = 0;
        for(int i=0; i<n;i++){
            int cnt = 0;
            while(crew < times.size() && times.get(crew) <= start && cnt <m){
                last = times.get(crew);
                crew++;
                cnt++;
            }
            if(i==n-1){
                if(cnt<m){
                    answer = minuteToTime(start);
                }else{
                    answer = minuteToTime(last - 1);
                }
            }
            start+= t;
        }
        
        
        return answer;
    }
    public static int timeToMinute(String time){
        String[] tmp = time.split(":");
        return Integer.parseInt(tmp[0])*60+Integer.parseInt(tmp[1]);
    }
    public static String minuteToTime(int m) {
        int hour = m / 60;
        int min = m % 60;
    return String.format("%02d:%02d", hour, min);
}
}