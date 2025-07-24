package y_2025.w_30th;
import java.util.Scanner;

public class b_4101 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        while (a + b != 0 ){
            if (a > b) {
                System.out.println("Yes");
            } else {
                System.out.println("No");
            }
            a = sc.nextInt();
            b = sc.nextInt();

        }

    }
    
}
