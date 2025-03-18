import java.util.*;
class Solution {
    public int solution(String[] board) {
        int answer = 1;
        
        int ocount = 0;
        int xcount = 0;
        
        for(int i=0; i<3;i++){
            for (int j=0; j<3; j++){
                if(board[i].charAt(j)=='O') ocount++;
                if(board[i].charAt(j)=='X') xcount++;
            }
        }
        if(ocount!=xcount && ocount != xcount +1) return 0;
        
        boolean owin = tictakto(board, 'O');
        boolean xwin = tictakto(board, 'X');
        
        if(owin && xwin) return 0;
        if(owin && ocount != xcount+1) return 0;
        if(xwin && ocount != xcount) return 0;
        return 1;
    }
    
public static boolean tictakto(String[] board, char player) {

        for (int i = 0; i < 3; i++) {
            if (board[i].charAt(0) == player && board[i].charAt(1) == player && board[i].charAt(2) == player)
                return true; 
            if (board[0].charAt(i) == player && board[1].charAt(i) == player && board[2].charAt(i) == player)
                return true; 
        }

        if (board[0].charAt(0) == player && board[1].charAt(1) == player && board[2].charAt(2) == player)
            return true;
        if (board[0].charAt(2) == player && board[1].charAt(1) == player && board[2].charAt(0) == player)
            return true;

        return false;
    }

}