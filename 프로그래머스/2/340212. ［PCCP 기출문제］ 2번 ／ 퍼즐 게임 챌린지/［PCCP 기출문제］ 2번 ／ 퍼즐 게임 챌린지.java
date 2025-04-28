import java.util.*;
class Solution {
    public int solution(int[] diffs, int[] times, long limit) {
        int answer = 0;
        
        int lt = 1;
        int rt = Arrays.stream(diffs).max().getAsInt() + 1;
        
        while (lt <= rt ){
            int mid = (lt+rt)/2;
            long l = limit;
            
            for(int i=0; i<diffs.length;i++){
                if(diffs[i]<=mid){
                    l -= times[i];
                }else{
                    int cur = diffs[i] - mid;
                    int prev = (i == 0) ? 0 : times[i-1];
                    l -= (long)(prev+times[i])*cur;
                    l -= times[i];
                }
            }
            if(l<0){
                lt = mid +1;
            }else{
                rt = mid-1;
            }
            
        }
            
        return lt;
    }
}