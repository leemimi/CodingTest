import java.util.*;
import java.util.stream.Collectors;
class Solution {
    static int nn;
    static int bk;
    static int[] enemys;
    public int solution(int n, int k, int[] enemy) {
        
        enemys = enemy;
        bk = k;
        nn = n;
        
        int lt = 0;
        int rt = enemy.length;
        
        while(lt<rt){
            int mid = (lt+rt)/2;
            
            if(isDefence(mid)){
                lt = mid +1;
            }else{
                rt = mid;
            }
            
        }
        
        return lt;
    }
    static boolean isDefence(int mid){
        List<Integer> em = Arrays.stream(enemys,0,mid+1)
            .boxed()
            .sorted()
            .collect(Collectors.toList());
        int size = em.size();
        
        int num = nn;
        
        for(int i=0; i<size;i++){
            Integer e = em.get(i);
            if(e<=num){
                num -= e;
                continue;
            }
            return bk>=size-i;
        }
        return true;
    }
}