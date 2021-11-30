import java.util.Scanner;
public class p8393_гу {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc=new Scanner(System.in);
		int n=sc.nextInt();
		int result=0;
		for(int i=1;i<=n;i++) {
			result+=i;
		}
		System.out.println(result);
	}

}
