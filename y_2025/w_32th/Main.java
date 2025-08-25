import java.util.Scanner;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = sc.nextInt();

        int[] num_lst = new int[n];
        for (int i = 0; i < n; i ++) {
            num_lst[i] = sc.nextInt();
        }

        Arrays.sort(num_lst);
        
        int i = 0;
        int j = n - 1;
        int cnt = 0;

        while (i < j) {
            int sum = num_lst[i] + num_lst[j];

            if (sum == m){
                cnt ++;
                i ++;
                j --;
            } else if (sum < m) { 
                i ++;
            } else {
                j --;
            }
        }

        System.out.println(cnt);
    }
}