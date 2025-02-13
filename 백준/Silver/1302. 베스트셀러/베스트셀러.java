import java.io.*;   
import java.util.*;
class Main {
    static int N;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        int max = 0;
        Map<String, Integer> map = new HashMap<>();

        for(int i=0; i<N; i++) {
            String s = br.readLine();
            map.put(s, map.getOrDefault(s,0)+1);
            max = Math.max(max, map.get(s));
        }

        List<String> list = new ArrayList<>();
        for(Map.Entry<String, Integer> entry : map.entrySet()){
            if(entry.getValue() ==max){
                list.add(entry.getKey());

            }
        }
        Collections.sort(list);
        System.out.println(list.get(0));
    }
}