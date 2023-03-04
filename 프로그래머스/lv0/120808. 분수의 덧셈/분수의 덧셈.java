class Solution {
    public int[] solution(int numer1, int denom1, int numer2, int denom2) {
        int[] answer = new int[2];
        
        int denom;
        int numer,numerL,numerR;
        
        denom = denom1*denom2;
        numerL = numer1*denom2;
        numerR = numer2*denom1;
        
        numer = numerL+numerR;
        
        int max=1;
        //최대공약수로 나눠주기
        for(int i=1;i<=denom && i<=numer;i++){
            if(denom%i==0 && numer%i==0){
                max = i;
            }
        }
        numer = numer/max;
        denom = denom /max;
        
        answer[0] = numer;
        answer[1] = denom;
        
        
        return answer;
    }
}