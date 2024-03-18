import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int Number[] = new int[sc.nextInt()];
        int M = sc.nextInt();

        for (int i = 0; i < M ; i++){
            int sp = sc.nextInt()-1;
            int ep = sc.nextInt()-1;
            int num = sc.nextInt();
            for (int j = sp; j <= ep; j++){
                Number[j] = num;
            }
        }
        for ( int num : Number){
            System.out.print(num + " ");
        }

    }
}
