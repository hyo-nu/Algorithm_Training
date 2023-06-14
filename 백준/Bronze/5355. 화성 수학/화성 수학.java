import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T  = sc.nextInt();
		
		for(int i=0; i<T; i++) {
			double num = sc.nextDouble();
			String[] ss = sc.nextLine().split(" ");
			
			for(String s : ss) {
				if (s.equals("@")) {
					num *= 3;
				}
				else if (s.equals("%")) {
					num += 5;
				}
				else if (s.equals("#")) {
					num -= 7;
				}
			}
			System.out.printf("%.2f\n" ,num);
		}
	}
}
