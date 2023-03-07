class Solution {
    public int solution(int[] absolutes, boolean[] signs) {
        int answer = 123456789;
        
        int []nums = new int[signs.length];
        int sum=0;
        for(int i=0;i<signs.length;i++){
            if(signs[i]==false){
                nums[i]=-(absolutes[i]);
            }
            else{
                nums[i]=absolutes[i];
            }
            sum+=nums[i];
        }
        
        
        return sum;
    }
}