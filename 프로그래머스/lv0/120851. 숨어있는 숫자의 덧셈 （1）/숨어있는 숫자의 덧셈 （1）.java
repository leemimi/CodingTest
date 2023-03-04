class Solution {
    public int solution(String my_string) {
        int answer = 0;
        String intStr = my_string.replaceAll("[^0-9]","");
        
        
        char[] cNum = intStr.toCharArray();
        
        for (int i=0;i<cNum.length; i++){
            answer +=cNum[i]-'0';
        }
        
        return answer;
    }
}