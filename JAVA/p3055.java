package DAY1_3055;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Scanner;

public class Main {
	//좌, 우 , 상, 하 순서
	static int[] mx = {-1,1,0,0}; //x축 조이스틱
	static int[] my = {0,0,-1,1}; //y축 조이스틱
	static int R,C;
	static char[][] map;
	static Queue<Point> queue;
	static int[][] dp;
	static int time=0;
	static Point current;
	static boolean answer;
	
	public static void main(String[] args) throws Exception {

		// TODO Auto-generated method stub
			//System.setIn(new FileInputStream("src\\DAY01_3055\\input.txt"));
			
			Scanner sc = new Scanner(System.in);
			
			R= sc.nextInt();
			C=sc.nextInt();
			
			dp=new int[R][C];
			map= new char[R][C];
			queue = new LinkedList<>();
			
			List<Point> waterList = new ArrayList<>();
			for(int r =0;r<R;r++) {
				String line = sc.next();
				//System.out.println(line);
				for(int c=0;c<C;c++) {
					map[r][c]=line.charAt(c);
					if(map[r][c]=='S') {
						queue.add(new Point(r,c,'S'));
					} else if (map[r][c]=='*') {
						waterList.add(new Point(r,c,'*'));
					}
				}
			}
	
			queue.addAll(waterList);
			
		//	for(int r=0;r<R;r++) {
		//		System.out.println(Arrays.toString(map[r]));
		//	}

		//	System.out.println(queue);
			
			while(!queue.isEmpty()) {
				//1.큐에서 꺼내옴
				Point p = queue.poll();
				//2.목적지인가 if(p==d)
				if(p.type=='D') {
					//목적지 도착
					System.out.println(dp[p.y][p.x]);
					answer= true;
					break;
				}
				//3.갈 수 있는 곳을 순회 (상하좌우)
				for(int i=0;i<4;i++) {
					int ty= p.y+my[i];
					int tx=p.x+mx[i];
				
				//4.갈수있는가 (맵을 벗어나지 않고, x아니고 물아닐때)
				if(0<=ty&& ty<R && 0<=tx&&tx<C){
					if(p.type=='.'||p.type=='S') {
						if (dp[ty][tx]==0&&checkSafe(ty,tx)) {
							dp[ty][tx]=dp[p.y][p.x]+1;
							queue.add(new Point(ty,tx,map[ty][tx]));
						}
					}else if (p.type =='*' && map[ty][tx]=='.') {
						queue.add(new Point(ty,tx,'*'));
						map[ty][tx]='*';
					}
				}
			//Point p = new Point(0,0,'*');
			
			//queue.add(p);
			//System.out.println(queue.peek()); 확인만 하는 것
			//System.out.println(queue.poll()); 완전히 꺼내서 확인하는 것
			//queue.poll();
			//System.out.println(p);
			}
		
		}
	if(answer==false) {
		System.out.println("KAKTUS");
	}
}


//4.갈수있는가 (맵을 벗어나지 않고, x아니고 물아닐때)
static boolean checkSafe(int y, int x) {
	if(map[y][x]=='D') {
		return true;
	}else if(map[y][x]=='.') {
		for(int i=0;i<4;i++) {
			int ty=y+my[i];
			int tx=x+mx[i];
			if(0<=ty&&ty<R&&0<=tx&&tx<C&&map[ty][tx]=='*') {
				return false;
				}
			}
		return true;
		}else {
			return false;
		}
	}
}

class Point{
	int y;
	int x;
	char type;
	public Point(int y, int x, char type) {
		super();
		this.y = y;
		this.x = x;
		this.type = type;
	}
	
	@Override
	public String toString() {
		return "[y=" + y + ", x=" + x + ", type=" + type + "]";
	}
}