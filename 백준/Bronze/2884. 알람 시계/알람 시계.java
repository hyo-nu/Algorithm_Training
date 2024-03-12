import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int h = sc.nextInt();
        int m = sc.nextInt();
        h = (m - 45 >= 0) ? h : --h;
        h = (h >= 0) ? h : 23;
        m = (m - 45 >=0 ) ? m - 45 : m + 15;
        System.out.println(h + " " + m);

    }
}