import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Stack;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Stack<Integer> stack = new Stack<Integer>();
        int N = Integer.parseInt(br.readLine());

        for (int i = 0; i < N; i++){
            String command = br.readLine();
            if(command.contains("push")){
                String[] str =  command.split(" ");
                stack.push(Integer.parseInt(str[1]));
            }
            else if (command.equals("top")){
                if(stack.size() != 0) System.out.println(stack.peek());
                else System.out.println(-1);
            }
            else if (command.equals("size")){
                System.out.println(stack.size());
            }
            else if (command.equals("empty")){
                if(stack.empty()) System.out.println(1);
                else System.out.println(0);
            }
            else if (command.equals("pop")){
                if (stack.size() != 0) System.out.println(stack.pop());
                else System.out.println(-1);
            }
        }
    }
}
