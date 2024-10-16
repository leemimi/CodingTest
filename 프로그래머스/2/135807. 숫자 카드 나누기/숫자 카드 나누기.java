import java.util.*;
class Solution {
    public int solution(int[] arrayA, int[] arrayB) {
        int answer = 0;
        
        int ga = arrayA[0];
        int gb = arrayB[0];
        
        for(int i=1; i<arrayA.length; i++){
            ga = gcd(ga, arrayA[i]);
            gb = gcd(gb, arrayB[i]);
        }
        if(Dis(arrayA, gb)){
            if(answer < gb){
                answer = gb;
            }
        }
        if(Dis(arrayB, ga)){
            if(answer < ga){
                answer = ga;
            }
        }
        
        
        return answer;
    }
    static int gcd(int a, int b){
        if(b==0){
            return a;
        }
        return gcd(b, a%b);
    }
    static boolean Dis(int[] arr, int num){
        for(int n:arr){
            if(n%num==0) return false;
        }
        return true;
    }
}