import java.util.*;
class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;
        Queue<Integer> bridge = new LinkedList<>();
        int n= truck_weights.length;
        for(int i=0;i<bridge_length;i++){
            bridge.offer(0);
        }
        int l = 0;
        int time = 0;
        int totalWeight = 0;
        while(l<n){
            time++;
            totalWeight -= bridge.poll();
            if(totalWeight + truck_weights[l] <= weight ){
                bridge.offer(truck_weights[l]);
                totalWeight += truck_weights[l];
                l++;
            }else{
                bridge.offer(0);
            }
        }
        
        return time+bridge_length;
    }
}