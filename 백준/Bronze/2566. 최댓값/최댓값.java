import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[][] arr = new int[9][9];
        int max = 0;
        int r = 0;
        int c = 0;
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                arr[i][j] = sc.nextInt();
                if (max <= arr[i][j]){
                    max = arr[i][j];
                    r = i + 1;
                    c = j + 1;
                }
            }
        }
        System.out.println(max);
        System.out.print(r + " " + c);
    }
}
