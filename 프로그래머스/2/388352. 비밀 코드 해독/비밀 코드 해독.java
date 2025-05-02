import java.util.*;
class Solution {
    static int n;
    static int[][] q;
    static int[] ans;
    static int m;
    static int answer;
    public int solution(int n, int[][] q, int[] ans) {
        this.n  = n;
        this.q = q;
        this.ans = ans;
        this.m = q.length;
        this.answer = answer;
        answer = 0;
        
        
        combination(1, new ArrayList<>());
        
        return answer;
    }
    public static void combination(int L, List<Integer> arr){
        if(arr.size()==5){
            if(check(arr)){
                answer++;
            }
            return;
        }
        
        for(int i=L;i<=n;i++){
            arr.add(i);
            combination(i+1,arr);
            arr.remove(arr.size()-1);
        }
        
    }
    public static boolean check(List<Integer> arr){
        for(int i=0; i<m; i++){
            int cnt =0;
            for(int j =0; j<q[i].length;j++){
                if(arr.contains(q[i][j])) cnt++;
            }
            if(cnt!=ans[i]) return false;
        }
        return true;
    }
    
}