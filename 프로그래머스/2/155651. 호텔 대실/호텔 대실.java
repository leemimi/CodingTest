import java.util.*;

class Solution {
    public int solution(String[][] book_time) {
        int answer = 0;
        
        int[][] book = new int[book_time.length][2];
        
        int n = book_time.length;
        for(int i=0; i<n;i++){
            int start = Integer.parseInt(book_time[i][0].replace(":",""));
            int end = Integer.parseInt(book_time[i][1].replace(":",""));
            
            end+=10;
            
            if(end%100>=60){
                end+=40;
            }
            book[i][0] = start;
            book[i][1] = end;
        }
        Arrays.sort(book, (a1,a2)->{return a1[0]-a2[0];});
        
        PriorityQueue<int[]> q = new PriorityQueue<>(Comparator.comparingInt(a -> a[1]));
        for(int[] b : book){
            if(q.isEmpty()){
                q.add(b);
            }else{
                int[] tmp = q.peek();
                int start = tmp[0];
                int end = tmp[1];
                
                if(b[0]>=end){
                    q.poll();
                }
                q.add(b);
            }
        }
        System.out.println(Arrays.deepToString(q.toArray()));
        answer = q.size();
        return answer;
    }
}