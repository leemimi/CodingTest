import java.util.*;
class Solution {
    public int solution(int[] bandage, int health, int[][] attacks) {
        int answer = 0;
        
        int time = 0;
        int v = 0;
        int n = attacks.length;
        int cnt = 0;
        
        Queue<Integer[]> q = new LinkedList<>();
        for(int i=0; i<n;i++){
            q.add(new Integer[]{attacks[i][0], attacks[i][1]});
        }
        
        int maxh = health;
        
        Integer[] a;
        
        while(!q.isEmpty()){
            a = q.peek();
            time++;
            
            System.out.println(time);
            if(time == a[0]){
                v=0;//초기화
                health -= a[1];
                q.poll();
                if(health<=0){
                    health = -1;
                    break;
                }
                continue;
            }
            health+=bandage[1];
            if(health>maxh) {
                health = maxh;
            }
            
            v++;
            if(v==bandage[0]){
                v=0;
                health+= bandage[2];
                if(health>maxh){
                    health = maxh;
                }
            }
        }

        return health;
    }
}