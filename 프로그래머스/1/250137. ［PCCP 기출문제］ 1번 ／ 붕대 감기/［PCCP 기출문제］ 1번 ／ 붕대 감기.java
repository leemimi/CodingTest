import java.util.*;
class Solution {
    public int solution(int[] bandage, int health, int[][] attacks) {
        int answer = 0;
        int time = 0;
        int cnt =0;
        int nowHealth = health;
        for(int i=0; i<attacks.length;i++){
            int[] attack = attacks[i];
            while(time<attack[0]){
                time++;
                if(nowHealth < health){
                    cnt++;
                    nowHealth+=bandage[1];
                    if(nowHealth>health) nowHealth = health;
                    if(cnt==bandage[0]){
                        nowHealth+=bandage[2];
                        cnt=0;
                        if(nowHealth>health) nowHealth = health;
                    }
                }                
            }
            
            nowHealth -= attack[1];
            cnt=0;
            if(nowHealth <=0){
                return -1;
            }
            time++;
        }
        
        
        return nowHealth;
    }
}