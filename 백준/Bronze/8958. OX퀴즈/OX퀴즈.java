import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = Integer.parseInt(sc.nextLine());
        for ( int i = 0; i < N ; i++){
            String[] str = sc.nextLine().split("X");
            int total = 0;
            for( int j= 0; j < str.length; j++){
                int score = 1;
                for ( int k = 0; k < str[j].length(); k++){
                    total += score++;
                }
            }
            System.out.println(total);
        }
    }
}