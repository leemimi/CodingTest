import java.io.*;
import java.util.*;
class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        PriorityQueue<Integer> pq = new PriorityQueue<>(
            Comparator.comparingInt((Integer num) -> num%10)
            .thenComparing(num -> num));

        int cnt = 0;
        st = new StringTokenizer(br.readLine());
        for(int i=0; i<N; i++) {
            int num = Integer.parseInt(st.nextToken());
            if (num == 10){
                cnt++;
                continue;
            }
            if (num <10 ){
                continue;
            }
            pq.add(num);
        }
        while(M>0&&!pq.isEmpty()){
            int num = pq.poll();
            if(num -10 == 10){
                cnt++;
            }
            if(num - 10> 10){
                pq.add(num-10);
            }
            cnt++;
            M--;
        }
        
        System.out.println(cnt);
        
    }
}