import java.util.*;
class Solution {
    public int[][] solution(int[][] data, String ext, int val_ext, String sort_by) {

        List<int[]> lst = new ArrayList<>();
        //추출
        if(ext.equals("code")){
            for(int[] d : data){
                if(d[0]<val_ext){
                    lst.add(d);
                }
            }
                        
        }else if(ext.equals("date")){
            for(int[] d : data){
                if(d[1]<val_ext){
                    lst.add(d);
                }
            }
            
        }else if(ext.equals("maximum")){
            for(int[] d : data){
                if(d[2]<val_ext){
                    lst.add(d);
                }
            }
            
            
        }else if(ext.equals("remain")){
            for(int[] d : data){
                if(d[3]<val_ext){
                    lst.add(d);
                }
            }
            
        }
        
        //정렬
        if(sort_by.equals("date")){
            Collections.sort(lst, (a,b)->a[1]-b[1]);
        }else if(sort_by.equals("remain")){
            Collections.sort(lst, (a,b)->a[3]-b[3]);
        }else if(sort_by.equals("maximum")){
            Collections.sort(lst, (a,b)->a[2]-b[2]);
        }else{
            Collections.sort(lst, (a,b)->a[0]-b[0]);
        }
        int[][] answer = new int[lst.size()][];
        for (int i = 0; i < lst.size(); i++) {
            answer[i] = lst.get(i);
        }

        return answer;
    }
}