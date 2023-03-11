class Solution {
    public int[] solution(int[] prices) {
        int [] ans = new int[prices.length];
        for(int i=0;i<prices.length;i++){
            for(int j=i+1;j<prices.length;j++){
                if(prices[i]<=prices[j]){
                    ans[i]+=1;
                }else{
                    ans[i]+=1;
                    break;
                }    
            }
        }
        return ans;
    }
}
