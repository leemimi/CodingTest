import java.util.*;
class Solution {
    public int solution(String[] friends, String[] gifts) {
        int answer = 0;
        int n= friends.length;
        
        HashMap<String,Integer> map =new HashMap<>();
        for(int i=0;i<n;i++){
            map.put(friends[i],i);
        }
        int[] giftDegree = new int[n];
        int[][] giftGraph = new int[n][n];
        
        
        for(String g:gifts){
            String[] gname = g.split(" ");
            giftDegree[map.get(gname[0])]++;
            giftDegree[map.get(gname[1])]--;
            giftGraph[map.get(gname[0])][map.get(gname[1])]++;
            
        }
        for(int i=0;i<n;i++){
            int cnt = 0;
            for(int j=0; j<n;j++){
                if(i==j)continue;
                if(giftGraph[i][j] > giftGraph[j][i] || 
                  (giftGraph[i][j]== giftGraph[j][i] && giftDegree[i]>giftDegree[j])) cnt++;
            }
            if(answer<cnt){
                answer= cnt;
            }
        }
        
        return answer;
    }
}