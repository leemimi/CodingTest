import java.util.*;
class Solution {
    static String[] member = {"A", "C", "F", "J", "M", "N", "R", "T"};
    static boolean[] visited = new boolean[8];
    static int answer;
    public int solution(int n, String[] data) {
        answer = 0;
        dfs("", data);
        return answer;
    }

    public void dfs(String line, String[] data){
        if(line.length()==8){
            if(check(line, data)){
                answer++;
            }
            return;
        }
        
        for(int i=0; i<8;i++){
            if(!visited[i]){
                visited[i] = true;
                dfs(line+member[i], data);
                visited[i] = false;
            }
        }
    }
    public boolean check(String line, String[] data){
        for(String d: data){
            char m1 = d.charAt(0);
            char m2 = d.charAt(2);
            char op = d.charAt(3);
            int dist = d.charAt(4) - '0';
            
            int pos1 = line.indexOf(m1);
            int pos2 = line.indexOf(m2);
            int nowDist = Math.abs(pos1-pos2)-1;
            
            if(op=='=' && nowDist!=dist) return false;
            if(op =='>' && nowDist<=dist) return false;
            if(op =='<' && nowDist>=dist) return false;
        }
        return true;
    }
}