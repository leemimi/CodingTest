import java.util.*;
class Solution {
    public int[] solution(int n, String[] words) {
        int[] answer = new int[2];
        
        HashMap<String,Integer> map = new HashMap<>();
        
        for(int i=0; i<words.length;i++){
            map.put(words[i], map.getOrDefault(words[i],0)+1);
            if(map.get(words[i])>=2){
                answer[0] = (i%n)+1;
                answer[1] = (i/n)+1;
                break;
            }else if(i>=1){
                if(words[i].charAt(0) != words[i-1].charAt(words[i-1].length()-1)){
                    answer[0] = (i%n)+1;
                    answer[1] = (i/n)+1;
                    break;
                }
            }
                
                
        }
        

        return answer;
    }
}