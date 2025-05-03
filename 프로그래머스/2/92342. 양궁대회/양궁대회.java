import java.util.*;
class Solution {
    static int[] rian;
    static int n;
    static int[] info;
    static int[] answer = {-1};
    static int max = Integer.MIN_VALUE;
    public int[] solution(int n, int[] info) {
        this.n = n;
        this.info = info;
        rian = new int[11];
        
        dfs(0, 0, rian);
        if(max == -1){
            int[] res = {-1};
            return res;
        }
        return answer;
    }
    public static void dfs(int L, int start, int[] rian){
        if(L==n){
            int diff = getScore(rian);
            if(max<diff){
                max = diff;
                answer = rian.clone();
            }else if(max == diff){
                int cnt = 0;
                for(int i=10;i>-1;i--){
                    if(answer[i]<rian[i]){
                        answer = rian.clone();
                        break;
                    }
                    if(answer[i]>rian[i]){
                        break;
                    }
                        
                }
            }
            return;
            
        }
        
        for(int i=start; i<11;i++){
            if(info[i] < rian[i]) continue;
            rian[i] ++;
            dfs(L+1,i,rian);
            rian[i]--;
        }
    }
    public static int getScore(int[] arr){
        int cnt = 0;
        int a =0;
        int r = 0;
        for(int i=0; i<11;i++){
            if(info[i] ==0 && arr[i] == 0) continue;
            if(info[i]<arr[i]) r+=10-i;
            else a+=10-i;
        }
        cnt = r-a;
        if(cnt<=0){
            return -1;
        }
        return cnt;
    }
}