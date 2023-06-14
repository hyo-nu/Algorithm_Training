import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int A = sc.nextInt();
		int B = sc.nextInt();
		int C = sc.nextInt();
		int D = sc.nextInt();
		int H,M,S;
		
		S = D % 60;
		M = (D / 60) % 60;
		H = (D / 3600);
		
		M = M + ((C + S) / 60);
		C = (C + S) % 60;
		
		H = H + ((B + M) / 60);
		B = (B + M) % 60;
		
		A = (A + H) % 24;
		
		System.out.println(A + " " + B + " " + C);
		
	}
}
