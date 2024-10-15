import java.util.*;
class Solution {
    public String solution(String video_len, String pos, String op_start, String op_end, String[] commands) {
        String answer = "";
        
        int now = time(Integer.parseInt(pos.substring(0,2)), Integer.parseInt(pos.substring(3,5)));
        int st = time(Integer.parseInt(op_start.substring(0,2)), Integer.parseInt(op_start.substring(3,5)));
        int end = time(Integer.parseInt(op_end.substring(0,2)), Integer.parseInt(op_end.substring(3,5)));
        int len = time(Integer.parseInt(video_len.substring(0,2)), Integer.parseInt(video_len.substring(3,5)));
        if(now>=st && now <= end){
            now = end;
        }
        
        for(String command: commands){
            if(command.equals("next")){
                now+=10;
                if(len-now<10){
                    now = len;
                }
            }else{
                now -=10;
                if(now<10){
                    now = 0;
                }
            }
            if(now>=st && now <= end){
                now = end;
            }
            
        }
        
        
        answer = String.format("%02d:%02d", now / 60, now % 60);
        
        
        
        return answer;
    }
    static int time(int a, int b){
        return a*60 + b;
    }
}