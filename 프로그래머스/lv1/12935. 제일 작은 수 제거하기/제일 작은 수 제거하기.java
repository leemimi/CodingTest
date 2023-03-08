import java.util.*;
import java.util.ArrayList;
class Solution {
    public int[] solution(int[] arr) {
        
        int min=arr[0];

        
        if(arr.length == 1){
            int[] answer = {-1};
            return answer;
        }
        int[] answer = new int[arr.length-1];
        for(int i=0; i<arr.length;i++){
            if(min>arr[i]){
                min=arr[i];
            }
        }
        int index=0;
        for(int i=0; i<arr.length;i++){
            if(arr[i]==min){
                continue;
            }
            answer[index++] = arr[i]++;
        }
        return answer;

    }
}