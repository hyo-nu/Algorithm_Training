import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int A = sc.nextInt();
		int B = sc.nextInt();
		int C = sc.nextInt();
	 
		int h = C / 60;
		int m = C % 60;
		
		h = h + (int)((B + m) / 60);
		B = (B + m) % 60;
		A = (A + h) % 24;
		System.out.println(A + " " + B);		
	}	
}