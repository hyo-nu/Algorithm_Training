import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        int[] lst = new int[N];

        for(int i = 0; i < N; i++) {
            lst[i] = i+1;
        }

        for (int i = 0; i < M; i++) {
            int sp = sc.nextInt();
            int ep = sc.nextInt();

            for (int j = 0; j < (int)((ep-sp + 1) / 2)  ; j++){
                int tmp = lst[sp+j-1];
                lst[sp+j-1] = lst[ep-j-1];
                lst[ep-j-1] = tmp;
            }
        }
        for (int num : lst) System.out.print(num+" ");
    }
}
