import java.util.*;
class Solution {
    public String solution(String video_len, String pos, String op_start, String op_end, String[] commands) {
        String answer = "";
        int pre = 10;
        int n = commands.length;
        
        int start = calc(op_start);
        int end = calc(op_end);
        int vlen = calc(video_len);
        int now = calc(pos);
        
        if(now>=start && now<=end){
            now = end;
        }
        for(int i=0; i<n; i++){
            if(commands[i].equals("next")){
                now+=10;
                if(vlen-now<10){
                    now=vlen;
                }
            }else if(commands[i].equals("prev")){
                now-=10;
                if(now<10){
                    now=0;
                }
            }
            if(now>=start && now<=end){
                now = end;
            }
        }
        
        
        answer =  String.format("%02d:%02d", now/60, now%60);
        
        return answer;
    }
    static int calc(String s){
        return Integer.parseInt(s.substring(0,2))*60 + Integer.parseInt(s.substring(3,5));
    }
}