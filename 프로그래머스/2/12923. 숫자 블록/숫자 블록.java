import java.util.*;
class Solution {
    public int[] solution(long begin, long end) {
        int be = (int)begin;
        int en = (int)end;
        int[] answer = new int[en-be+1];
        Arrays.fill(answer,1);
        for(int i=be;i<en+1;i++){
            answer[i-be] = calc(i);
        }
        if(be==1) answer[0] = 0;
        return answer;
    }
    public static int calc(int start){
        int max = 1;
        for(int i=2; i*i<=start;i++){
            if(start%i==0){
                max = i;
                if(start/i<= 10000000)
                return start/i;
            }
        }
        return max;
    }
}