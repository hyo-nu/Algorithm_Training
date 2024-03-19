import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] scores = new int[N];
        int max = 0;
        for (int i = 0; i < N ; i++){
            scores[i] = sc.nextInt();
            max = (max < scores[i]) ? scores[i] : max;
        }
        float sum = 0;
        for (float score : scores){
            sum += score / (float)max * 100;
        }
        System.out.println(sum / N);
    }
}
