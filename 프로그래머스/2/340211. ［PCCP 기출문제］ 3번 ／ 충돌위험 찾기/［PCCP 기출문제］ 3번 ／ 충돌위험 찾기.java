import java.util.*;
class Solution {
    static int answer;
    static int[][] points;
    static int[][] routes;
    static List<List<int[]>> paths;
    public int solution(int[][] points, int[][] routes) {
        answer = 0;
        this.points = points;
        this.routes = routes;
        paths = new ArrayList<>();
        //루트 이동 좌표 담기
        for(int[]r : routes){
            List<int[]> path = new ArrayList<>();
            int[] first = points[r[0] - 1];
            path.add(new int[]{first[0], first[1]});
            for (int i = 0; i < r.length - 1; i++) {
                
                goRobot(r[i] - 1, r[i + 1] - 1, path);
            }
            paths.add(path);
        }
        // for(List<int[]> pp: paths){
        //     for(int[] p: pp){
        //         System.out.println(Arrays.toString(p));
        //     }
        // }
        
        
        int max = 0;
        //시간별로 map에 넣어서 충돌 지점 계산하기
        for(List<int[]> pa: paths){
            max = Math.max(max, pa.size());
        }
        for(int t=0; t<max;t++){
            Map<String,Integer> time = new HashMap<>();
            for(int i=0; i<paths.size();i++){
                List<int[]> path = paths.get(i);
                if(t<path.size()){
                    int[] pos = path.get(t);
                    String key = pos[0] + "," + pos[1];
                    time.put(key, time.getOrDefault(key,0)+1);
                }
            }
            for(int cnt: time.values()){
                if(cnt>=2) answer++;
            }
        }
        
        return answer;
    }
    public static void goRobot(int start, int target, List<int[]> path){
        int sx = points[start][0]-1;
        int sy = points[start][1]-1;
        int gx = points[target][0]-1;
        int gy = points[target][1]-1;

        while(sx!=gx){
            sx += (gx>sx)? 1:-1;
            path.add(new int[]{sx,sy});
        }
        while(sy!=gy){
            sy += (gy>sy)? 1:-1;
            path.add(new int[]{sx,sy});
        }
        
    }
}