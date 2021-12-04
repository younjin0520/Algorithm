package DAY1_1759_암호만들기;

import java.util.Arrays;
import java.util.Scanner;

public class Main {
	static int L;
	static int C;
	static char[] array;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		//암호의 길이 L
		L = sc.nextInt();
		//C종류의 알파벳으로 구성
		C =sc.nextInt();
		array = new char[C];
		
		for(int i=0;i<C;i++) {
			array[i] = sc.next().charAt(0); //한 문자씩 받기
		}

		Arrays.sort(array);
		
		for(int i=0;i<C;i++) {
			if(array[i]=='a'||array[i]=='e'||array[i]=='i'||array[i]=='o'||array[i]=='u') {
				dfs(1,0,1,i,array[i]+"");
			}else {
				dfs(1,1,0,i,array[i]+"");
			}
		}
		//최소 한 개의 모음과 두 개의 자음
		
	
		//오름차순 정렬
	}
	public static void dfs(int length, int con, int vow,int index, String pwd) {
		// 1.체크인 (생략가능)
		// 2.목적지인가?
		if(length==L) {
			if(con>=2&&vow>=1) {
				System.out.println(pwd);
				return;
			}
		}else if (length <L){
			// 3.갈 수 있는 곳을 순회
			
			
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
		
		// 4.갈 수 있는가? - 생략
		// 5.간다 dfs(next)

		// 6.체크아웃(생략가능)
	}
}