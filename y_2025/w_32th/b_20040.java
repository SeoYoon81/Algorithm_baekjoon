import java.util.Scanner;

public class b_20040 {
    static int[] parent;

    public static int find_p(int x){
        if (x != parent[x]) {
            parent[x] = find_p(parent[x]);
        }
        return parent[x];
    }


    public static boolean union(int x, int y) {
        int a = find_p(x);
        int b = find_p(y);
        if (a == b) {
            return true;
        } else {
            parent[b] = a;
            return false;
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();

        parent = new int[n];
        for (int i = 0 ; i < n ; i ++){
            parent[i] = i;
        }

        boolean result = false;
        for ( int k = 0 ; k < m; k ++) {
            int x = sc.nextInt();
            int y = sc.nextInt();

            result = union(x, y);
            if (result) {
                System.out.println(k +1);
                return;
            }
        }
        if (!result) {
            System.out.println(0);
        }
    }
}


