import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] alpha = new int[26];
        String s = sc.nextLine();

        for (int i = 0; i < 26; i++) {
            alpha[i] = -1;
        }

        for (int i = 0; i < s.length(); i++) {
            if (alpha[(int)s.charAt(i)-97] != -1) continue;
            alpha[(int)s.charAt(i)-97] = i;
        }
        for (int i = 0; i < 26; i++) {
            System.out.print(alpha[i] + " ");
        }
    }
}
