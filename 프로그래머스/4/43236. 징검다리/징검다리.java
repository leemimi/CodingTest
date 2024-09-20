import java.util.*;
class Solution {
    public int solution(int distance, int[] rocks, int n) {
        int answer = 0;
        
        Arrays.sort(rocks);
        
        int lt = 1;
        int rt = distance;
        
        
        int[] dis = new int[rocks.length+1];
        dis[0] = rocks[0];
        dis[rocks.length] = distance - rocks[rocks.length-1];
        for(int i=1; i<rocks.length;i++){
            dis[i] = rocks[i] - rocks[i-1];
        }
        
        while(lt<=rt){
            int mid = (lt+rt)/2;
            
            int rStone = 0;
            int sum = 0;
            for(int j=0; j<rocks.length+1;j++){
                sum+=dis[j];
                if(sum < mid){
                    rStone++;
                    continue;
                }
                sum = 0;
                if(rStone>n){
                    break;
                }
            }
            if(rStone>n){
                rt = mid -1;
            }else{
                lt = mid +1;
                answer = mid;
            }
            
        }
        
        return answer;
    }
}