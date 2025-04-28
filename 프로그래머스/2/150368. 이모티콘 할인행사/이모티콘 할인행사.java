import java.util.*;
class Solution {
    static int n;
    static int[] emoticons;
    static int[][] users;
    static int[] sales = {10,20,30,40};
    static int[] answer = new int[2];
    
    public int[] solution(int[][] users, int[] emoticons) {
        this.users = users;
        this.emoticons = emoticons;
        int[] rates = new int[emoticons.length];
        
        dfs(0,rates);    
        
        return answer;
    }
    public static void dfs(int L, int[] rates){
        if (L == rates.length ){
            calc(rates);
            return;
        }
        for(int i=0; i<sales.length;i++){
            rates[L] = sales[i];
            dfs(L+1, rates);
        }        
    }
    public static void calc(int[] rates){
        int[] ans = new int[2];
        for(int i=0; i<users.length;i++){
            int total = 0;
            for(int j=0; j<emoticons.length; j++){
                if(users[i][0]<=rates[j]){
                    total += emoticons[j]*(100-rates[j])/100;
                }
            }
            if(total >= users[i][1]){
                ans[0] ++;
            }else{
                ans[1]+=total;
            }
        }
        if(ans[0]>answer[0]){
            answer[0] = ans[0];
            answer[1] = ans[1];
        }
        if(ans[0] == answer[0] && ans[1] > answer[1]){
            answer[0] = ans[0];
            answer[1] = ans[1];
        }
        
    }
    
}