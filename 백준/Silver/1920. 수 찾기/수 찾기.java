import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader( new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(arr);

        int m = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        for (int i = 0 ; i < m; i++){
            int answer = 0;
            int start = 0, end = n - 1;
            int target = Integer.parseInt(st.nextToken());

            while (start <= end){
                int mid = (start + end) / 2;
                if(arr[mid] == target) {
                    answer = 1;
                    break;
                }
                if (arr[mid] > target) end = mid - 1;
                else  start = mid + 1;
            }
            System.out.println(answer);
        }
    }
}
