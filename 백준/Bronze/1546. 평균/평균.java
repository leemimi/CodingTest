import java.util.Scanner;
import java.util.Arrays;
public class Main {
    public static void main (String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int[] test = new int[N];
        for (int i = 0; i < N; i++) {
            test[i] = sc.nextInt();
        }
        Arrays.sort(test);
        long max = test[N - 1];
        long sum = 0;
        for (int i = 0; i < N; i++) {
            sum += test[i];
        }
        System.out.println(sum * 100.0 / max / N);
    }
}

