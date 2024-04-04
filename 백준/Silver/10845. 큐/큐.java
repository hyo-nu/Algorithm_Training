import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.rmi.dgc.Lease;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Queue<Integer> queue = new LinkedList<Integer>();
        int N = Integer.parseInt(br.readLine());

        for(int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String S = st.nextToken();

            switch (S) {
                case "push":
                    int num = Integer.parseInt(st.nextToken());
                    queue.offer(num);
                    break;

                case "pop":
                    if (queue.isEmpty()) {
                        System.out.println(-1);
                        break;
                    }
                    System.out.println(queue.poll());
                    break;

                case "size":
                    System.out.println(queue.size());
                    break;

                case "empty":
                    if (queue.isEmpty()) {
                        System.out.println(1);
                        break;
                    }
                    else System.out.println(0);
                    break;

                case "front":
                    if (queue.isEmpty()) {
                        System.out.println(-1);
                        break;
                    }
                    System.out.println(queue.peek());
                    break;

                case "back":
                    if (queue.isEmpty()) {
                        System.out.println(-1);
                        break;
                    }
                    else {
                        int lastElement = -1;
                        for (int element : queue) {
                            lastElement = element;
                        }
                        System.out.println(lastElement);
                    }
                    break;
            }
        }
    }
}