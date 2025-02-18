import java.util.*;
class Solution {
    public String solution(String new_id) {
        String answer = "";
        String id = new_id.toLowerCase();

        StringBuilder sb = new StringBuilder();
        int cnt = 0;
        char prev = ' ';
        for (int i = 0; i < id.length(); i++) {
            char c = id.charAt(i);
            if (Character.isLetter(c) || Character.isDigit(c) || c == '-' || c == '_' || c == '.') {
                if (c == '.' && prev == '.') {
                    continue; // 연속된 .을 방지
                }
                sb.append(c);
                prev = c; // 현재 문자를 prev로 저장
            }
        }
        
        while(sb.length() > 0 && sb.charAt(0)=='.'){
            sb.deleteCharAt(0);
        }

        while(sb.length() > 0&&sb.charAt(sb.length()-1)=='.'){
            sb.deleteCharAt(sb.length() - 1);
        }
        if(sb.length()==0){
            sb.append('a');
        }
        if(sb.length()>=16){
            sb.setLength(15);
        }
        while(sb.length() > 0&&sb.charAt(sb.length()-1)=='.'){
            sb.deleteCharAt(sb.length() - 1);
        }
        if(sb.length()<=2){
            char last = sb.charAt(sb.length()-1);
            while(sb.length() < 3){
                sb.append(last);
            }
        }
        System.out.println(sb);
        
        answer = sb.toString();
        return answer;
    }
}