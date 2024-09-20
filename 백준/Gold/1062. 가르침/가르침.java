

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.sql.Time;
import java.util.*;

public class Main {
    static int n;
    static int k;
    static String[] arr;
    static int answer;
    static boolean[] isFlag;
    public static void main (String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        arr = new String[n];
        answer = 0;
        for(int i=0; i<n;i++){
            arr[i] = br.readLine();
        }
        if(k<5){
            System.out.println(0);
            return;
        }else if(k == 26){
            System.out.println(n);
            return;
        }

        for(int i=0; i<n;i++){
            arr[i] = arr[i].substring(4, arr[i].length()-4);
        }

        isFlag = new boolean[26];

        isFlag['a'- 'a'] = true;
        isFlag['n'- 'a'] = true;
        isFlag['t'- 'a'] = true;
        isFlag['i'- 'a'] = true;
        isFlag['c'- 'a'] = true;

        dfs(5,0);
        System.out.println(answer);

    }
    static void dfs(int L, int idx){
        if(L==k){
            check();
            return;
        }
        for(int i=idx;i<26;i++){
            if(!isFlag[i]){
                isFlag[i] = true;
                dfs(L+1, i);
                isFlag[i]=false;
            }
        }
    }
    static void check(){
        int cnt = 0;

        for(int i=0; i<n;i++){
            int len = arr[i].length();
            boolean flag = true;
            for(int j=0; j<len;j++){
                if(!isFlag[arr[i].charAt(j)-'a']){
                    flag= false;
                    break;
                }
            }
            if(flag) cnt++;
        }
        answer = Math.max(answer, cnt);
    }

}