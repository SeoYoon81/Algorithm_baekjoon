package y_2025.w_28th_week;
import java.util.Scanner;

public class b_27433 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        long res = 1;
            for(int i = 1 ; i <= n ; i ++){
                res *= i;
            }
            System.out.println(res);
    }
}
