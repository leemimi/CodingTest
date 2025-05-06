import java.util.*;
class Solution {
    public int solution(int n, int[] stations, int w) {
        int answer = 0;
        int idx = 1;
        int wide = w*2+1;
        for(int station: stations){
            int lt = station-w;
            int rt = station+w;
            int uncover = lt-idx;
            if(uncover>0){
                answer += (uncover+wide-1)/wide;
            }
            idx = rt+1;
        }
        if(idx <= n){
            int uncover = n - idx +1;
            answer += (uncover+wide-1)/wide;
        }

        return answer;
    }
}