import java.util.*;
class Solution {
    public int solution(int x, int y, int n) {
        int answer = -1;
        
        Queue<int[]> q = new LinkedList<>(); 
        q.add(new int[]{x,0});
        Set<Integer> set = new HashSet<>();
        set.add(x);
        while(!q.isEmpty()){
            int[] arr = q.poll();
            if(arr[0] == y){
                answer = arr[1];
                break;
            }
            int num = arr[0]+n;
            if(num <= y && !set.contains(num)){
                q.add(new int[]{num,arr[1]+1});
                set.add(num);
            }
            num = arr[0]*2;
            if(num <= y && !set.contains(num)){
                q.add(new int[]{num,arr[1]+1});
                set.add(num);
        }
            num = arr[0]*3;
            if(num <= y && !set.contains(num)){
                q.add(new int[]{num,arr[1]+1});
                set.add(num);
        }
        
        }
        return answer;
    }
}