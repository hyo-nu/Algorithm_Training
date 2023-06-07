import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int A = sc.nextInt();
		int B = sc.nextInt();
		
		int first = A * (B % 10);
		int second = A * ((B / 10)%10);
		int third = A * (B/100);
		
		System.out.println(first);
		System.out.println(second);
		System.out.println(third);
		System.out.println(first + (second*10) + (third*100));	
	}
}