class Solution {
    public String solution(int n) {
        String answer = "";
        String [] rep = {"수","박"};
        for(int i=0;i<n;i++){
            if(i%2==0){
                answer += rep[0];
            }else{
                answer+=rep[1];
            }
        
    }return answer;
}
}