import java.util.Scanner;
import java.util.ArrayDeque;
import java.util.Deque;

public class b_4485 {
    static int[] di = {1, 0, -1, 0};
    static int[] dj = {0, 1, 0, -1};

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int cnt = 0;
        while (true){
            cnt ++;
            int n = sc.nextInt();
            if (n == 0) {
                break;
            }

            int[][] matrix = new int[n][n];
            int[][] visit = new int[n][n];

            for (int i = 0; i < n ; i ++){
                for (int j = 0; j < n ; j ++){
                    matrix[i][j] = sc.nextInt();
                    visit[i][j] = -1;
                }
            }

            visit[0][0] = matrix[0][0];
            Deque<int[]> target = new ArrayDeque<> ();
            target.add(new int[]{0,0});

            while (!target.isEmpty()){
                int[] now = target.poll();
                int a = now[0];
                int b = now[1];

                for (int d = 0; d < 4; d ++){
                    int i = a + di[d];
                    int j = b + dj[d];
                    if (i<0|| i >= n|| j < 0 || j >= n){
                        continue;
                    } 
                    if (visit[i][j] == -1){
                        visit[i][j] = visit[a][b] + matrix[i][j];
                        target.add(new int[] {i,j});
                    } else {
                        if (visit[i][j] > visit[a][b] + matrix[i][j]){
                            visit[i][j] = visit[a][b] + matrix[i][j];
                            target.add(new int[] {i, j});
                        }
                    }
                }
            }

            System.out.println("Problem "+cnt+": "+visit[n-1][n-1]);
        }
    }
}
