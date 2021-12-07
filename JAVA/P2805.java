package DAY02;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class P2805 {

    static int N, M;
    static int[] trees;

    public static void main(String[] args) throws Exception {
        System.setIn(new FileInputStream("src\\DAY02\\P2805\\input.txt"));

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        trees = new int[N];

        System.out.println(N + ", " + M);

        st = new StringTokenizer(br.readLine());
        int max = 0;
        for (int i = 0; i < N; i++) {
            trees[i] = Integer.parseInt(st.nextToken());
            max = Math.max(trees[i], max);
        }

        System.out.println(Arrays.toString(trees));
        System.out.println(max);

        int s = 0;
        int e = max;
        int mid;
        long sum = 0;
        int result = 0;
        while (true) {
            mid = (s + e) / 2;
            // sum = ���� ������ ��;
            sum = calc(mid);
            // sum == M : �� �߰�
            if (sum == M) {
                result = mid;
                break;
            }
            // sum < M : ���� ����
            else if (sum < M) {
                e = mid - 1;
            }
            // sum > M : ���� ����
            else {
                result = mid;
                s = mid + 1;
            }
            // ��Ȯ�� ���� �߰����� ������ ���
            if (s > e) {
                break;
            }
        }
        System.out.println(result);
    }

    static long calc(int value) {
        long result = 0;
        for (int i = 0; i < trees.length; i++) {
            if (trees[i] > value) {
                result += trees[i] - value;
            }
        }
        return result;
    }
}