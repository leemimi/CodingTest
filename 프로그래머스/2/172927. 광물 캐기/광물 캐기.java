import java.util.*;
class Solution {
     private static final int[][] groups = {
            { 1, 1, 1 },
            { 5, 1, 1 },
            { 25, 5, 1 }
    };
    public int solution(int[] picks, String[] minerals) {

        int sum =Arrays.stream(picks).sum()*5;
        if(sum<minerals.length){
            minerals = Arrays.copyOfRange(minerals,0,sum);
        }
        PriorityQueue<int[]> pq = new PriorityQueue<>((a,b)->b[1]-a[1]);
        for(int i=0;i<minerals.length;i+=5){
            int tmp = 0;
            for(int j=i; j<i+5 && j< minerals.length;j++){
                switch(minerals[j]){
                        case "diamond" -> tmp+= groups[2][0];
                        case "iron" -> tmp+=groups[2][1];
                        case "stone" -> tmp+=groups[2][2];
                }
            }
            pq.offer(new int[]{i,tmp});
        }
        int p=0;
        for(int i=0;i<picks.length;i++){
            if(picks[i]>0){
                p=i;
                break;
            }
        }
        int answer = 0;
        while(!pq.isEmpty()){
            int m = pq.poll()[0];
            for(int i=m;i<m+5&&i<minerals.length;i++){
                switch(minerals[i]){
                        case "diamond" -> answer+=groups[p][0];
                        case "iron" -> answer+=groups[p][1];
                        case "stone" -> answer += groups[p][2];
                }
            }
            if(--picks[p]==0){
                p++;
            }
        }

        return answer;
    }
}