import java.util.*;
class Solution {
    public int[] solution(String s) {

        //문자열 앞뒤 {{ }} 삭제
        s = s.substring(2);
        s = s.substring(0,s.length()-2);
        
        List<String> arr = new ArrayList<>();
        
        String[] str = s.split("\\},\\{");
        
        //문자열 길이 만큼 정렬해줌
        Arrays.sort(str, Comparator.comparing(String::length));
        
        for(String e:str){
            String[] k = e.split(",");
            // System.out.println(Arrays.toString(k));
            for(int i=0;i<k.length;i++){
                if(arr.contains(k[i])==false){
                    arr.add(k[i]);
                }
            }
        }
        
        int [] A = new int[arr.size()];
        for(int i=0; i<arr.size();i++){
            A[i] = Integer.parseInt(arr.get(i));
        }
        

        
        return A;
    }
}