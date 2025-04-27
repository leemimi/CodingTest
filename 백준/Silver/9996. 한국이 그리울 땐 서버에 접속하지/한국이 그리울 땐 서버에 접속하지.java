import java.io.*;
import java.util.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(reader.readLine());
        String pattern = reader.readLine();

        int start = pattern.indexOf("*");
        String prefix = pattern.substring(0,start);
        String suffix = pattern.substring(start+1);
        
        for (int i = 0; i < n; i++) {
            String fileName = reader.readLine();
            if(fileName.length() < prefix.length()+ suffix.length()){
                System.out.println("NE");
                continue;
            }
            if(fileName.startsWith(prefix)&&fileName.endsWith(suffix)){
                System.out.println("DA");
            }else{
                System.out.println("NE");
            }
        }
    }
}