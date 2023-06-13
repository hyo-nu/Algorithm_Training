import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		int sum = 0;
		Scanner sc = new Scanner(System.in);
		for(int i=0; i<5; i++) {
			int num = sc.nextInt();
			if (num < 40){
				num = 40;
			}
			sum += num;
		}
		System.out.println(sum/5);
	}
}