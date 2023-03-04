class Solution {
    public String solution(String rsp) {
        String answer = "";
        
        
        char[] numC = rsp.toCharArray();
       //가위2 바위0 보5
        for(int i=0;i<rsp.length();i++){
            if(numC[i]=='2'){
                answer+=0;
            }else if(numC[i]=='0'){answer+=5;}
        else{
            answer+=2;}
        }
        return answer;
    }
}