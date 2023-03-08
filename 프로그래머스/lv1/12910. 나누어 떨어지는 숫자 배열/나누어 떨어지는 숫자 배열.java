import java.util.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;
class Solution {
    public int[] solution(int[] arr, int divisor) {
        int[] answer = {};
        List<Integer> list = new ArrayList<>();
        for(int e:arr){
            list.add(e);
        }
        List<Integer> ans = new ArrayList<>();
        for(int i=0;i<list.size();i++){
            if(list.get(i) %divisor==0){
                ans.add(list.get(i));
                }
            }
        if(ans.isEmpty()){
            ans.add(-1);
        }        
        Collections.sort(ans);
        
        return ans.stream().mapToInt(i->i).toArray();
    }
}