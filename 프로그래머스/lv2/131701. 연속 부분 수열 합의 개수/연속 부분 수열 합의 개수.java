import java.util.*;
class Solution {
    public int solution(int[] elements) {

        Set <Integer> arr = new HashSet<>();
    for(int k =1; k<=elements.length;k++){
        for(int i=0;i<elements.length;i++){
            int sum =0;
            for(int j=i;j<i+k;j++){
                sum+=elements[j%elements.length]; //나눈이유는 0~5까지범위만!!
            }
            arr.add(sum);
        }
    }
        return arr.size();
    }
}