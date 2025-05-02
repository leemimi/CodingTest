import java.io.*;
import java.util.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(reader.readLine());
        String[] arr = new String[n];

        for (int i = 0; i < n; i++) {
            arr[i] = reader.readLine();
        }
        HashMap<Character,Integer> map = new HashMap<>();
        for(String word: arr){
            int len = word.length();
            for(int i=0; i<len;i++){
                char c = word.charAt(i);
                map.put(c, map.getOrDefault(c,0)+ (int) Math.pow(10,len-i-1));
            }
        }
        List<Integer> weight = new ArrayList<>(map.values());
        weight.sort((a,b)->(b-a));
        int p = 9;
        int answer = 0;
        for(int w: weight){
            answer += p*w;
            p--;
        }
        System.out.println(answer);
    }
}