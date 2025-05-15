import java.util.*;
class Solution {
    public String solution(String X, String Y) {
        String answer = "";
        int[] xcnt = new int[10];
        int[] ycnt = new int[10];
        
        for(char a: X.toCharArray()){
            xcnt[a-'0']++;
        }
        for(char a:Y.toCharArray()){
            ycnt[a-'0']++;
        }
        StringBuilder sb = new StringBuilder();
        
        for(int i=9;i>-1;i--){
            int cnt = Math.min(xcnt[i],ycnt[i]);
            for(int j=0;j<cnt;j++){
                sb.append(i);
            }
        }
        if(sb.length()==0) return "-1";
        if(sb.charAt(0)=='0') return "0";

        
        return sb.toString();
    }
}