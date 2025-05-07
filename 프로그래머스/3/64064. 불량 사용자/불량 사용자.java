import java.util.*;
class Solution {
    static boolean[] visited;
    static int n;
    static String[] user_id;
    static String[] banned_id;
    static Set<Set<String>> set;
    public int solution(String[] user_id, String[] banned_id) {
        int answer = 0;
        this.user_id = user_id;
        this.banned_id = banned_id;
        
        List<List<Integer>> ban = new ArrayList<>();
        n = banned_id.length;
        visited = new boolean[user_id.length];
        set = new HashSet<>();
        dfs(0, new HashSet<>());
        
        return set.size();
    }
    public static void dfs(int L, Set<String> cur){
        if(L==n){
            set.add(new HashSet<>(cur));
            return;
        }
        for(int i=0;i<user_id.length;i++){
            if(visited[i]) continue;
            if(isCheck(user_id[i], banned_id[L])){
                visited[i] = true;
                cur.add(user_id[i]);
                dfs(L+1, cur);
                cur.remove(user_id[i]);
                visited[i] = false;
            }
        }
    }
    public static boolean isCheck(String user, String ban){
        if (user.length() != ban.length()) return false;
        for(int i=0; i<user.length(); i++){
            if(ban.charAt(i) != '*' && ban.charAt(i)!= user.charAt(i)){
                return false;
            }
        }
        
        
        return true;
    }
}