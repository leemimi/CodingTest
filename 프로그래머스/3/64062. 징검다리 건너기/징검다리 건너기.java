import java.util.*;
class Solution {
    public int solution(int[] stones, int k) {
        int answer = 0;
        int lt = 0;
        int rt = Arrays.stream(stones).max().getAsInt()+1;
        
        while(lt<rt-1){
            int mid = (lt+rt)/2;
            
            boolean flag = true;
            int go = 0;
            for(int stone: stones){
                if(stone < mid){
                    go++;
                }else if(stone >= mid){
                    go = 0;
                }
                if(go == k){
                    flag = false;
                    break;
                }
            }
            if(!flag){
                rt = mid ;
            }else{
                lt = mid;
            }
        }
        
        
        return lt;
    }
}