package DAY1_1713_�ĺ���õ;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.Scanner;

public class Main {
	static Student[] student = new Student[101];

	public static void main(String[] args) {

		int N, total, current;

		Scanner sc = new Scanner(System.in);

		N = sc.nextInt();
		total = sc.nextInt();
		
		//���� ����Ʈ
		List<Student> list = new ArrayList<>();

		for (int i = 0; i < total; i++) {
			current = sc.nextInt();
			// ó�� �Ҹ� ��
			if (student[current] == null) {
				student[current] = new Student(false, 0, 0, current);
			}

			if (student[current].isIn == true) {
				student[current].chooseNum++;
			} else {
				// �������
				if (list.size() == N) {
					Collections.sort(list);
					Student p = list.remove(0);
					p.isIn = false;
				}

				student[current].chooseNum = 1;
				student[current].isIn = true;
				student[current].time = i;
				list.add(student[current]);
			}
		}
		Collections.sort(list, new Comparator<Student>() {
			// -1 : ���ϴ� ����, 0 : ����, 1 : ���ϴ� ������ �ƴ�
			@Override
			public int compare(Student arg0, Student arg1) {
				if (arg0.ID < arg1.ID) {
					return -1;
				} else if (arg0.ID == arg1.ID) {
					return 0;
				} else {
					return 1;
				}
			}
		});
		for (Student person : list) {
			System.out.print(person.ID);
			System.out.print(" ");
		}
	}
}

class Student implements Comparable<Student> {
	boolean isIn;
	int chooseNum;
	int time;
	int ID;

	public Student(boolean isIn, int chooseNum, int time, int ID) {
		super();
		this.isIn = isIn;
		this.chooseNum = chooseNum;
		this.time = time;
		this.ID = ID;
	}
	@Override
	public int compareTo(Student arg0) {
		if (chooseNum < arg0.chooseNum) {
			return -1;
		} else if (chooseNum == arg0.chooseNum) {
			// timeStamp ��
			if (time < arg0.time) {
				return -1;
			} else if (time == arg0.time) {
				return 0;
			} else {
				return 1;
			}
		} else {
			return 1;
		}
	}
}