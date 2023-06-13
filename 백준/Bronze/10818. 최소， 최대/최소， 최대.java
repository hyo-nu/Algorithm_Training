import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int Max = -1000000;
		int Min = 1000000;
		for(int i=0; i<N; i++) {
			int num = sc.nextInt();
			if(Max < num) {
				Max = num;
			}
			if(Min > num) {
				Min = num;
			}
		}
		System.out.print(Min + " ");
		System.out.print(Max);
	}
}