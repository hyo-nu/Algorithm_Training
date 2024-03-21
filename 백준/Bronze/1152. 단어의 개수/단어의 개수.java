import java.util.Scanner;
import java.util.Set;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine().trim();
        String[] arr = str.split(" ");
        
        if (str.equals("")){
            System.out.println(0);
        }else{
            System.out.println(arr.length);
        }
    }
}
