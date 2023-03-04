import java.util.stream.Stream;
import java.util.Arrays;
class Solution {
    public int[] solution(String my_string) {
        
        String arr = my_string.replaceAll("[^0-9]","");
        
        int[] answer = Stream.of(arr.split("")).mapToInt(Integer::parseInt).toArray();
        
        Arrays.sort(answer);
        return answer;
    }
}