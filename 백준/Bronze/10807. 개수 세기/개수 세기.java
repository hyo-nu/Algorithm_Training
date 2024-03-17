import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine());
        int[] lst = new int[n];
        
        for (int i = 0 ; i < n; i++) {
            lst[i] = sc.nextInt();
        }
        
        int target  = sc.nextInt();
        int count = 0;

        for (int i = 0; i < n; i++){
            if(target == lst[i]){
                count++;
            }
        }
        System.out.println(count);

    }
}
