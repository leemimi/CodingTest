import java.util.*;
class Solution {
    static int[] cards;
    public int solution(int[] cards) {
        this.cards = cards;
        int answer = 0;
        int n = cards.length;
        for(int i=0;i<n;i++){
            boolean[] visited = new boolean[n];

            int a = makeBox(cards[i], visited);
            for(int j=0; j<n;j++){
                if(!visited[j]){
                    int b = makeBox(cards[j],visited);
                    answer = Math.max(answer, a*b);
                }
            }
            
            
            
        }
        
        
        return answer;
    }
    public static int makeBox(int num, boolean[] visited){
        int cnt = 0;
        
        while(!visited[num-1]){
            visited[num-1] = true;
            num = cards[num-1];
            cnt++;
        }
        return cnt;
    }
}