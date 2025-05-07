import java.util.*;
class Solution {
    public int[] solution(String[] genres, int[] plays) {
        int[] answer = {};
        List<Integer> lst = new ArrayList<>();
        Map<String, Integer> total = new HashMap<>();
        Map<String, List<int[]>> songs = new HashMap<>();
        for(int i=0;i<plays.length;i++){
            String g = genres[i];
            int play = plays[i];
            
            total.put(g, total.getOrDefault(g, 0)+play);
            songs.putIfAbsent(g, new ArrayList<>());
            songs.get(g).add(new int[]{i, play});
        }
        System.out.println(songs);
        List<String> sortedGenres = new ArrayList<>(total.keySet());
        System.out.println(sortedGenres);
        sortedGenres.sort((a,b)-> total.get(b)-total.get(a));
        
        List<Integer> ans = new ArrayList<>();
        for(String name: sortedGenres){
            List<int[]> song = songs.get(name);
            song.sort((a,b)-> {
                     if(b[1]==a[1]) return a[0]-b[0];
                     return b[1]-a[1];
            });
            for(int i=0; i<Math.min(2, song.size()); i++){
                ans.add(song.get(i)[0]);
            }
            
        }
        
        
        return ans.stream().mapToInt(i->i).toArray();
    }
}