import java.util.*;
class Solution
{   static String s;
    public int solution(String s)
    {
        
        int answer = 1;
        
        for(int i=0;i<s.length();i++){
            answer = Math.max(answer, find(s, i, i));
            answer = Math.max(answer, find(s,i,i+1));
            
        }

        return answer;
    }
 public static int find(String s, int lt, int rt){
     while(lt>=0 && rt<s.length()&& s.charAt(lt)== s.charAt(rt)){
            lt--;
            rt++;
        }
     return rt-lt-1;
 }
 }