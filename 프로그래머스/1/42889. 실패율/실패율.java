import java.util.*;
class Solution {
    public int[] solution(int N, int[] stages) {
        int[] answer = new int[N];
        
        int n = stages.length;
        Arrays.sort(stages);
        
        HashMap<Integer,Integer> map = new HashMap<>();
        for (int stage : stages) {
            map.put(stage, map.getOrDefault(stage, 0) + 1);
        }
        
        int cnt = n;
        List<double[]> list = new ArrayList<>();
        for(int i=1;i<=N;i++){
            if(cnt == 0){
                list.add(new double[]{i,0});
                continue;
            }
            int c = map.getOrDefault(i,0);
            double k =  (double) c/cnt;
            cnt -= c;
            list.add(new double[]{i,k});
        }

        list.sort((a,b)->{
            if(b[1] == a[1]) return Double.compare(a[0],b[0]);
            return Double.compare(b[1],a[1]);
        });
        
        for(int i=0; i<N;i++){
            answer[i] = (int) list.get(i)[0];
        }
        
        
        return answer;
    }
}