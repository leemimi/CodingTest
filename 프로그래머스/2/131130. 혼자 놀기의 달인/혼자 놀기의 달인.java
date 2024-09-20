import java.util.*;
class Solution {
    public int solution(int[] cards) {
        int answer = 0;
        
        for(int i=0; i<cards.length;i++){
            boolean[] visited = new boolean[cards.length];
            int a = find(cards, visited, cards[i]);
            
            for(int j=0; j<cards.length;j++){
                if(!visited[j]){
                    int b = find(cards, visited, cards[j]);
                    answer = Math.max(a*b, answer);
                }
                
            }
            
        }
        
        
        return answer;
    }
    static int find(int[] cards, boolean[] visited, int now){
        int cnt = 0;
        
        while(!visited[now-1]){
            visited[now-1] = true;
            now = cards[now-1];
            cnt++;
        }
        
        return cnt;
        
    }
    
}