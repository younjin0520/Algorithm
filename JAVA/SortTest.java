package DAY1_sort;

import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

public class SortTest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Point[] array = new Point[5];
		
		array[0] = new Point(0,0,1);
		array[1] = new Point(0,1,3);
		array[2] = new Point(0,2,4);
		array[3] = new Point(3,0,5);
		array[4] = new Point(4,0,2);
		
		System.out.println(Arrays.toString(array));
		
		Arrays.sort(array, new Comparator<Point>() {
			@Override
			public int compare(Point arg0, Point arg1) {
				//-1 데이터를 바꾸지 않음
				if(arg0.y<arg1.y) {
					return -1;
					//y에 대한 오름차순
				}else if (arg0.y==arg1.y) {
					if (arg0.value <arg1.value) {
						return -1;
					}else if (arg0.value==arg1.value) {
						return 0;
					}else {
						return 1;
					}
				}else {
					return 1;
				}
				//0 같음
				//1 데이터를 바꿈
			}
		});
		System.out.println(Arrays.toString(array));
		Arrays.sort(array);
		
		List<Point> list = new ArrayList<>();
		for(int i=0; i<array.length;i++) {
			list.add(array[i]);
		}
		
		System.out.println(list);
		Collections.sort(list);
		Collections.sort(list, new Comparator<Point>() {

			@Override
			public int compare(Point arg0, Point arg1) {
				// TODO Auto-generated method stub
				return 0;
			}
			
		});
	}
	
}


class Point implements Comparable<Point>{ //기본적인 정렬 값으로 설정
	int x;
	int y;
	int value;
	
	public Point(int x, int y, int value) {
		super();
		this.x = x;
		this.y = y;
		this.value = value;
	}
	
	@Override
	public String toString() {
		return "Point [x=" + x + ", y=" + y + ", value=" + value + "]";
	}

	@Override
	public int compareTo(Point arg0) {
		if(x>arg0.x) {
			return -1;
		}else if (x==arg0.x) {
			return 0;
		}else {
			return 1;
		}
	}
}