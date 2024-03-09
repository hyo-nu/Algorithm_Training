import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int A = Integer.parseInt(sc.nextLine());
		int B = Integer.parseInt(sc.nextLine());
		
		int one = A * (B % 10);
		System.out.println(one);
		
		int two = A * ((B % 100) / 10);
		System.out.println(two);
		
		int three = A * (B / 100) ;
		System.out.println(three);
		
		System.out.println(one + two*10 + three*100);
	}
}
