import java.util.Scanner;

public class Main {
   public static void main(String[] args) {
	   Scanner sc = new Scanner(System.in);
	   int number = Integer.parseInt(sc.nextLine());
	   
	   for (int i = 1; i < number; i++) {
		   for (int j = 1; j <= i; j++) {
			   System.out.print("*");
		   }
		   for (int j = 1; j <= (number - i) * 2; j++) {
			   System.out.print(" ");
		   }
		   for (int j = 1; j <= i; j++) {
			   System.out.print("*");
		   }
		   System.out.println();
	   }
	   
	   for (int i = number; i >= 1; i--) {
		   for (int j = 1; j <= i; j++) {
			   System.out.print("*");
		   }
		   for (int j = 1; j <= (number - i) * 2; j++) {
			   System.out.print(" ");
		   }
		   for (int j = 1; j <= i; j++) {
			   System.out.print("*");
		   }
		   System.out.println();
	   }
   }
}