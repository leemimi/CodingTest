import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main (String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer stringTokenizer = new StringTokenizer(bufferedReader.readLine());//예제 첫번째 줄을 읽어옴
        int suNo = Integer.parseInt(stringTokenizer.nextToken());
        int quizNo = Integer.parseInt(stringTokenizer.nextToken());

        //덧셈이나 곱셈이 많을때는 long형을 선언해주자!
        long[] S = new long[suNo+1]; //1선언 이유는 0번째 인덱스를 무시하고 질의를 바로바로 쓰고자 +1을 뒤에 씀
        stringTokenizer = new StringTokenizer(bufferedReader.readLine());
        for(int i=1;i<=suNo;i++){
            S[i] = S[i-1] + Integer.parseInt(stringTokenizer.nextToken());
        }

        for(int q =0; q<quizNo;q++){
            stringTokenizer = new StringTokenizer(bufferedReader.readLine());
            int i = Integer.parseInt(stringTokenizer.nextToken());
            int j = Integer.parseInt(stringTokenizer.nextToken());
            System.out.println(S[j]-S[i-1]);
        }
    }
}
