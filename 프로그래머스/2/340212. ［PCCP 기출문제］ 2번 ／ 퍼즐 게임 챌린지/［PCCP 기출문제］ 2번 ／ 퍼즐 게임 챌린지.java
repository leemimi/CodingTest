import java.util.*;
class Solution {
    public int solution(int[] diffs, int[] times, long limit) {
        int answer = 0;
        
        int lt = 1;
        int rt = Arrays.stream(diffs).max().getAsInt();
        int n = diffs.length;
        while (lt <= rt){
            long lim = limit;
            int mid = (lt+rt)/2;
            
            if(solve(diffs, times, lim, mid)){
                rt = mid-1;
            }else{
                lt = mid +1;
            }
        }
        
        return lt;
    }
    static boolean solve(int[] diffs, int[] times, long limit, int level ){
        long lim = limit;
        int n = diffs.length;
        
        for(int i=0; i<n; i++){
            if(level >= diffs[i]){
                lim -= times[i]; 
            }else{
                int tmp = diffs[i] - level;
                if(i==0){
                    lim -= times[i]*(tmp+1);
                }else{
                    lim -= (times[i]+times[i-1])*tmp + times[i];
                }
            }
            if(lim<0){
                return false;
            }
        }
        return lim>=0;
    }
}