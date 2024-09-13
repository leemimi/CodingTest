class Solution {
    public static int answer;
    public static boolean[] visited;
    public int solution(int k, int[][] dungeons) {
        answer = 0;
        visited = new boolean[dungeons.length];
        dfs(0,k,dungeons);
        
        return answer;
    }
    public void dfs(int L, int k, int[][]dungeons){
            for(int i=0;i<dungeons.length;i++){
                if(!visited[i]&&dungeons[i][0]<=k){
                    visited[i] = true;
                    dfs(L+1, k-dungeons[i][1], dungeons);
                    visited[i] = false;
                }
        }
        answer = Math.max(answer, L);
    }
}