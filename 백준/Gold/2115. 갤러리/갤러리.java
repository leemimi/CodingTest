import java.io.*;
import java.util.*;

class Main {
    static int M, N;            // 세로, 가로 크기
    static char[][] gallery;    // 갤러리 배열
    
    public static void main(String[] args) throws IOException {
        // 입력 설정
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        // 갤러리 크기 입력
        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        gallery = new char[M][N];
        
        // 갤러리 상태 입력 ('.' 빈 공간, 'X' 벽)
        for (int i = 0; i < M; i++) {
            String line = br.readLine();
            gallery[i] = line.toCharArray();
        }
        
        br.close();


        int f1 =0, f2 = 0; // 각각의 벽의 개수
        // 벽의 개수 세기
        int res = 0;
        for (int i = 0; i < M-1; i++) {
            for (int j = 0; j < N; j++) {
                if (gallery[i][j] == 'X' && gallery[i+1][j]=='.') {
                    f1++;
                }else{
                    res+= f1/2;
                    f1 =0;
                }
                if(gallery[i][j]=='.'&&gallery[i+1][j]=='X') f2++;
                else{
                    res+= f2/2;
                    f2 =0;
                }
            }
        }
        f1 = 0; f2 = 0; // 초기화
        for(int i=0; i<N-1;  i++){
            for(int j=0; j<M;j++ ){
                if(gallery[j][i]=='X' && gallery[j][i+1]=='.') f1++;
                else{
                    res+= f1/2;
                    f1 =0;
                }
                if(gallery[j][i]=='.' && gallery[j][i+1]=='X') f2++;
                else{
                    res+= f2/2;
                    f2 =0;
                }
            }
        }

        // 결과 출력
        System.out.println(res);
    }
}