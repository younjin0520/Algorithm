package DAY2_2003_수들의합2;

import java.util.Arrays;
import java.util.Scanner;

public class Main {
	static int N;
	static int M;
	static int[] array;

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int count = 0, low = 0, high = 0,sum;
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		M = sc.nextInt();
		array = new int[N+1];
		for (int i = 0; i < N; i++) {
			array[i] = sc.nextInt();
		}
		
		
		
		sum = array[0];
		while(low<=high && high <N) {
			//합과 같을 떄
			if(M == sum) {
				count++;
				high++;
				sum +=array[high];
			}else if(M>sum) {
				//합보다 작을 떄
				high++;
				sum += array[high];
			}else {
				//합보다 클 때
				sum -= array[low++];
			}
		}
		
		System.out.println(count);
	}

}
