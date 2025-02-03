import java.util.*;
class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        int m=0;
        for(int i=0; i<commands.length;i++){
            int[] command = commands[i];
            int l =0;
            int k = command[1]-command[0] +1;
            int[] tmp = new int[k];
            for(int j=commands[i][0]; j<=commands[i][1];j++){
                tmp[l++] = array[j-1];
            }
            Arrays.sort(tmp);
            answer[m++] = tmp[command[2]-1];
        }
        
        
        return answer;
    }
}