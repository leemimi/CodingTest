import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {
    public static void main (String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        int answer = 0;
        int n = s.length();
        Stack<Character> stack = new Stack<>();
        for(int i=0; i<n;i++){
            if(s.charAt(i)=='('){
                stack.push('(');
            } else if (s.charAt(i)==')') {
                if(s.charAt(i-1) =='('){
                    stack.pop();
                    answer+=stack.size();
                }
                else{
                    stack.pop();
                    answer+=1;
                }
            }
        }


        System.out.println(answer);

    }
}