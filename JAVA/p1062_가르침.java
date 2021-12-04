package DAY1_1062_����ħ;

import java.util.Scanner;

public class Main {
	static int N,K,max,selectCount;
	static String[] word;
	static boolean[] isvisited;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		K = sc.nextInt();
		word = new String[N];
		isvisited = new boolean[26];

		for(int i=0;i<N;i++) {
			word[i]=sc.next().replaceAll("[antic]", "");
		}
		
		isvisited[0] = true;
		isvisited[2] = true;
		isvisited[8] = true;
		isvisited[13] = true;
		isvisited[19] = true;
		
		if(K<5) {
			System.out.println(0);
			return;
		}else if(K==26) {
			System.out.println(N);
			return;
		}

		selectCount =5;
		max = countWords();
		
		for(int k =0;k<26;k++) {
			if(isvisited[k]==false) {
				dfs(k);
			}
		}
		
		System.out.println(max);
		
	}

	public static void dfs(int index) {
		//1.üũ��
		isvisited[index]=true;
		selectCount++;
		//2.�������ΰ�
		if(selectCount ==K) {
			max = Math.max(countWords(), max);
		}else {
			//3.�����ִ°� ��ȸ
			for(int i=index+1;i<26;i++) {
				//4.�����ִ°�
				if(isvisited[i]==false)
					//5.����.
					dfs(i);
			}
		}
		//6.üũ�ƿ�
		isvisited[index]=false;
		selectCount--;
		
	}
	
	public static int countWords(){
		int count =0;
		String readWord;
		boolean isPossible;
		for(int i=0;i<N;i++) {
			isPossible=true;
			readWord = word[i];
			for(int j=0;j<readWord.length();j++) {
				if(isvisited[readWord.charAt(j)-'a']==false) {
					isPossible = false;
					break;
				}
			}
			
			if(isPossible==true) {
				count++;
			}
		}
		return count;
	}
	
	
}
