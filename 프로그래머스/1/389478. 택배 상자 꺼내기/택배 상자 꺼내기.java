import java.util.*;
class Solution {
    public int solution(int n, int w, int num) {
        int answer =0;
        int i = 1;
        List<List<Integer>> arrs = new ArrayList<>();
        boolean leftToRight = true;
        
        int realN = n;
        if(n%w!=0){
            n+=((n/w)+1)*w-n;
        }
        while(i<=n){
            List<Integer> arr = new ArrayList<>();
            for (int j = 0; j < w && i <= n; j++) {
                arr.add(i++);
            }
            if (!leftToRight) Collections.reverse(arr);
            arrs.add(arr);
            if (arr.size() % w == 0) {
                leftToRight = !leftToRight;
            }
            
        }

        int x = -1;
        int y = -1;
        for (int row = 0; row < arrs.size(); row++) {
            List<Integer> a = arrs.get(row);
            for (int col = 0; col < a.size(); col++) {
                if(a.get(col)==num){
                    x=row;
                    y=col;
                    break;
                }
            }
        }
        for(int j=x; j<arrs.size();j++){
            List<Integer> a = arrs.get(j);
            if(a.get(y) <= realN ){
                answer++;
            }
        }
            
            
        return answer;
    }
}
