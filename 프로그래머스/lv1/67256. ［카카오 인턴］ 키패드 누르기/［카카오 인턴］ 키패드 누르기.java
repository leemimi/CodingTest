import java.util.*;
import java.lang.Math;
class Solution {
    public String solution(int[] numbers, String hand) {
        String answer = "";
        int before_left = 10;
        int before_right = 12;

        for(int tmp : numbers){
            if(tmp == 1 ||tmp== 4||tmp== 7){
                answer+="L";
                before_left = tmp;
            }
            else if(tmp == 3 ||tmp== 6 ||tmp== 9){
                answer+="R";
                before_right = tmp;
            }
            else if(tmp ==2 ||tmp== 5 ||tmp== 8||tmp ==0){{
                if(tmp == 0) tmp =11;
                int a = Math.abs(before_left-tmp)/3 + Math.abs(before_left-tmp)%3 ;
                int b = Math.abs(before_right-tmp)/3 + Math.abs(before_right-tmp)%3;
                if(a<b){
                    answer+="L";
                    before_left = tmp;
                }else if(b<a){
                    answer+="R";
                    before_right = tmp;
                    
                }
                else{
                    if(hand.equals("left")){
                        answer+="L";
                        before_left = tmp;
                    }else{
                        answer+="R";
                        before_right = tmp;
                    }
                }
                
                
                }
            }
        }
        
        
        return answer;
    }
}