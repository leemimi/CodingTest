import java.util.*;
class Solution {
    static String target;
    static String[] words;
    static int answer;
    static boolean[]  visited;
    static int min = Integer.MAX_VALUE;
    public int solution(String begin, String target, String[] words) {
        
        this.target = target;
        this.words = words;
        answer = 0;
        visited = new boolean[words.length];
        if(!Arrays.asList(words).contains(target)) return 0;
        dfs(0,begin);
        
        return min;
    }
    public static void dfs(int L, String start){
        if(start.equals(target)){
            min = Math.min(min, L);
            return;
        }
        for(int i=0; i<words.length;i++){
            if(!visited[i] && check(start, words[i])){
                visited[i] = true;
                dfs(L+1,words[i]);
                visited[i] = false;
            }
        }
    }
    public static boolean check(String s, String w){
        int cnt=0;
        for(int i=0;i<w.length();i++){
            if(s.charAt(i) != w.charAt(i)) cnt++;
            if(cnt >1 ) return false;
        }
        return true;
    }
}