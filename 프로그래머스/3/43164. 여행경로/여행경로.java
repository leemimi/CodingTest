import java.util.*;
class Solution {
    static int n;
    static boolean[] visited;
    static ArrayList<String> arr;
    static String[][] ticket;
    
    List<String> answer;
    public String[] solution(String[][] tickets) {
        
        n = tickets.length;
        visited = new boolean[n];
        ticket = tickets;
        
        
        Arrays.sort(ticket, (a,b) -> a[1].compareTo(b[1]));
        arr = new ArrayList<>();
        
        
        dfs(0, "ICN", "ICN");
        
        
        
        String[] answer = arr.get(0).split(",");
        
        return answer;
    }
    static void dfs(int L, String target, String path){
        if(L==n){
            arr.add(path);
            return;
        }
        
        for(int i=0; i<n; i++){
            if(!visited[i]&&target.equals(ticket[i][0])){
                visited[i] = true;
                dfs(L+1, ticket[i][1], path + ","+ticket[i][1] );
                visited[i] = false;
            }
        }
    }
}