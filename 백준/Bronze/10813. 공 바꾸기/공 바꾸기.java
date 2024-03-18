import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        int [] basket = new int[N];
        for (int i = 0; i < N; i++) {
            basket[i] = i+1;
        }

        for (int i = 0; i < M ; i++){
            int A = sc.nextInt();
            int B = sc.nextInt();
            int tmp = basket[A-1];
            basket[A-1] = basket[B-1];
            basket[B-1] = tmp;
        }
        for (int i = 0; i < N; i++) {
            System.out.print(basket[i] + " ");
        }
    }
}
