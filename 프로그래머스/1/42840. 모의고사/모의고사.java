import java.util.*;
class Solution {
    public int[] solution(int[] answers) {
        int[] answer = {};
        int[] num1 = {1,2,3,4,5};
        int[] num2 = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] num3 = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        
        int c1 = 0;
        int c2 = 0;
        int c3 = 0;
        
        for(int i =0 ; i<answers.length; i++){
            if(answers[i] == num1[i%num1.length]){
                c1++;
            }
            if(answers[i] == num2[i%num2.length]){
                c2++;
            }
            if(answers[i] == num3[i%num3.length]){
                c3++;
            }
        }
        
        int[] ans = {c1,c2,c3};
        
        int max = Arrays.stream(ans).max().getAsInt();
        
        List<Integer> list = new ArrayList<>();
        for(int i =0 ;i<3;i++){
            if (max == ans[i]){
                list.add(i+1);
            }
        }
        
        return list.stream().mapToInt(Integer::intValue).toArray();
    }
}