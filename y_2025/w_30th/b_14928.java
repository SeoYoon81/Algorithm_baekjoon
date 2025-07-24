package y_2025.w_30th;
// import java.math.BigInteger;
import java.util.Scanner;

public class b_14928 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // BigInteger a = new BigInteger(sc.nextLine());
        // BigInteger r = new BigInteger("20000303");
        // System.out.println(a.remainder(r));
        String a = sc.nextLine();
        long temp = 0;
        for (int i = 0 ; i < a.length() ; i ++){
            temp = (temp * 10 + a.charAt(i) - '0') % 20000303;
        }
        System.out.println(temp);
    }

}

