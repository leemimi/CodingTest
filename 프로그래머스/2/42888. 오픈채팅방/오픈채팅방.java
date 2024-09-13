import java.util.*;
class Solution {
    public String[] solution(String[] record) {
        String[] answer = {};
        List<String> answerList = new ArrayList<>();
        HashMap<String,String> map = new HashMap<>();
        
        for(int i=0;i<record.length;i++){
            String[] tmp = record[i].split(" ");
            if(tmp[0].equals("Enter")){
                map.put(tmp[1],tmp[2]);
            }else if(tmp[0].equals("Change")){
                map.put(tmp[1],tmp[2]);
            }
        }
        for(int i=0; i<record.length;i++){
            String[] arr = record[i].split(" ");
            if(arr[0].equals("Enter")){
                answerList.add(map.get(arr[1])+"님이 들어왔습니다.");
            }else if(arr[0].equals("Leave")){
                answerList.add(map.get(arr[1])+"님이 나갔습니다.");
            }
        }
        answer = answerList.stream().toArray(String[]::new);
        
    return answer;
    }
}