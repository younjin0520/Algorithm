package DAY1_1759_��ȣ�����;

import java.util.Arrays;
import java.util.Scanner;

public class Main {
	static int L;
	static int C;
	static char[] array;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		//��ȣ�� ���� L
		L = sc.nextInt();
		//C������ ���ĺ����� ����
		C =sc.nextInt();
		array = new char[C];
		
		for(int i=0;i<C;i++) {
			array[i] = sc.next().charAt(0); //�� ���ھ� �ޱ�
		}

		Arrays.sort(array);
		
		for(int i=0;i<C;i++) {
			if(array[i]=='a'||array[i]=='e'||array[i]=='i'||array[i]=='o'||array[i]=='u') {
				dfs(1,0,1,i,array[i]+"");
			}else {
				dfs(1,1,0,i,array[i]+"");
			}
		}
		//�ּ� �� ���� ������ �� ���� ����
		
	
		//�������� ����
	}
	public static void dfs(int length, int con, int vow,int index, String pwd) {
		// 1.üũ�� (��������)
		// 2.�������ΰ�?
		if(length==L) {
			if(con>=2&&vow>=1) {
				System.out.println(pwd);
				return;
			}
		}else if (length <L){
			// 3.�� �� �ִ� ���� ��ȸ
			
			
			for(int j=index+1;j<C;j++) {
				if(array[j]=='a'||array[j]=='e'||array[j]=='i'||array[j]=='o'||array[j]=='u') {
					dfs(length+1, con, vow+1,j, pwd+array[j]);
				}else {
					dfs(length+1,con+1, vow,j, pwd+array[j]);
				}
			}
		}else {
			return;
		}
		
		// 4.�� �� �ִ°�? - ����
		// 5.���� dfs(next)

		// 6.üũ�ƿ�(��������)
	}
}