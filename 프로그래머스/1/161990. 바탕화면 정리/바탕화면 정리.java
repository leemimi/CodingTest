import java.util.*;
class Solution {
    public int[] solution(String[] wallpaper) {

        int n = wallpaper.length;
        int m = wallpaper[0].length();
        char[][] arr = new char[n][m];

        for (int i = 0; i < n; i++) {
            arr[i] = wallpaper[i].toCharArray();
        }
        int x1 = n;
        int y1 = m;
        int x2 =0;
        int y2=0;
        
        for(int i=0; i<n;i++){
            for(int j=0;j<m;j++){
                if(arr[i][j] == '#'){
                    x1 = Math.min(x1,i);
                    y1 = Math.min(y1,j);
                    x2 = Math.max(x2,i);
                    y2= Math.max(y2,j);
                }
            }
        }
        
        int[] answer = {x1,y1,x2+1,y2+1};
        
        return answer;
    }
}