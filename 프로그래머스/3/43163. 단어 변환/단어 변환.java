import java.util.*;
class Solution {
    static int n;
    static boolean[] visited;
    static int answer;
    public int solution(String begin, String target, String[] words) {
        answer = 51;
        n = words.length;
        
        if(!Arrays.asList(words).contains(target)){
            return 0;
        }
        visited = new boolean[n];
        dfs(begin,0,words,target,0);
        
        
        return answer;
    }
    static void dfs(String now, int L, String[] words,String target, int cnt){
        
        if(now.equals(target)){
            answer = Math.min(cnt, answer);
            return;
        }
        
        
        for(int i=0; i<n;i++){

            if(!visited[i]&&canTransform(now,words[i])){
                visited[i] = true;
                dfs(words[i], L+1, words, target, cnt+1);
                visited[i] = false;
            }
        }
        
    }
    static boolean canTransform(String now, String word){
        int  diff =0;
        for(int j=0; j<now.length();j++){
            if(now.charAt(j) != word.charAt(j) ){
                diff++;
            }
            if(diff>1){
                return false;
            }
        }
        return diff==1;
}
}