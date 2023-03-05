class Solution {
    public String solution(String my_string, int num1, int num2) {
        String answer = "";
        
        char[] str= my_string.toCharArray();
        
        char tmp = str[num2];
        str[num2] = str[num1];
        str[num1] = tmp;
        
        for(int i=0;i<str.length;i++){
            answer +=str[i];
        }
        return answer;
    }
}