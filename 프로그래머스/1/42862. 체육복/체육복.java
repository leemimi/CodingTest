import java.util.*;
class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int answer = 0;
        Arrays.sort(lost);
        Arrays.sort(reserve);
        List<Integer> lostList = new ArrayList<>();

        
        for(int l:lost){
            boolean flag = false;
            for(int i=0; i<reserve.length;i++){
                if(l==reserve[i]){
                    reserve[i] = -1;
                    flag= true;
                    break;
                }
            }
            if(!flag){
                lostList.add(l);
            }
        }
        for(int r: reserve){
            if(r==-1)continue;
            for(int i=0;i<lostList.size();i++){
                int l = lostList.get(i);
                if(Math.abs(l-r)==1){
                    lostList.remove(i);
                    break;
                }
            }
        }
            
        return n-lostList.size();
    }
}