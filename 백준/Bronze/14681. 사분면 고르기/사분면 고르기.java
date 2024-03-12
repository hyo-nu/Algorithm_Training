import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x = Integer.parseInt(sc.nextLine());
        int y = Integer.parseInt(sc.nextLine());
        int Quadrant = 0;
        Quadrant = (x > 0) ?
                (y > 0) ?  1 : 4 :
                (y > 0) ?  2 : 3 ;
        System.out.println(Quadrant);
    }
}