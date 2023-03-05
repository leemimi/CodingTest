import java.util.*;
class Solution {
    public int solution(int[] numbers) {
        int answer = 0;
        
        Arrays.sort(numbers);
        System.out.println(Arrays.toString(numbers));
        
        int max = -2147483648;
        int n = numbers.length;
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
            if (numbers[i]*numbers[n-1-j]>=max&&i!=n-1-j){
                max = numbers[i]*numbers[n-1-j];
                }
            }
        }
        
        return max;
    }
}