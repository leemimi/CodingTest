import java.util.*;
class Solution {
    public int solution(int[] wallet, int[] bill) {
        int answer = 0;
        int cnt = wallet[0]*wallet[1];
        Arrays.sort(wallet);
        while(true){
            Arrays.sort(bill);
            if(bill[0] <= wallet[0] && bill[1] <=wallet[1]){
                break;
            }
            

            if(bill[0]>bill[1]){
                bill[0] /=2;
                bill[0] = (int)bill[0];
            }else{
                bill[1] /= 2;
                bill[1] = (int) bill[1];
            }
            answer++;
        }
        
        
        return answer;
    }
}