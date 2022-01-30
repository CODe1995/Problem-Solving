package swea1970;

/////////////////////////////////////////////////////////////////////////////////////////////
//�⺻ �����ڵ�� ���� �����ص� ���� �����ϴ�. ��, ����� ���� ����
//�Ʒ� ǥ�� ����� ���� �ʿ�� �����ϼ���.
//ǥ�� �Է� ����
//int a;
//double b;
//char g;
//String var;
//long AB;
//a = sc.nextInt();                           // int ���� 1�� �Է¹޴� ����
//b = sc.nextDouble();                        // double ���� 1�� �Է¹޴� ����
//g = sc.nextByte();                          // char ���� 1�� �Է¹޴� ����
//var = sc.next();                            // ���ڿ� 1�� �Է¹޴� ����
//AB = sc.nextLong();                         // long ���� 1�� �Է¹޴� ����
/////////////////////////////////////////////////////////////////////////////////////////////
//ǥ�� ��� ����
//int a = 0;                            
//double b = 1.0;               
//char g = 'b';
//String var = "ABCDEFG";
//long AB = 12345678901234567L;
//System.out.println(a);                       // int ���� 1�� ����ϴ� ����
//System.out.println(b); 		       						 // double ���� 1�� ����ϴ� ����
//System.out.println(g);		       						 // char ���� 1�� ����ϴ� ����
//System.out.println(var);		       				   // ���ڿ� 1�� ����ϴ� ����
//System.out.println(AB);		       				     // long ���� 1�� ����ϴ� ����
/////////////////////////////////////////////////////////////////////////////////////////////
import java.util.Scanner;
import java.io.FileInputStream;

/*
����ϴ� Ŭ�������� Solution �̾�� �ϹǷ�, ������ Solution.java �� ����� ���� �����մϴ�.
�̷��� ��Ȳ������ �����ϰ� java Solution �������� ���α׷��� �����غ� �� �ֽ��ϴ�.
*/
class Solution {
	public static void main(String args[]) throws Exception {
		/*
		 * �Ʒ��� �޼ҵ� ȣ���� ������ ǥ�� �Է�(Ű����) ��� input.txt ���Ϸκ��� �о���ڴٴ� �ǹ��� �ڵ��Դϴ�. �������� �ۼ��� �ڵ带
		 * �׽�Ʈ �� ��, ���Ǹ� ���ؼ� input.txt�� �Է��� ������ ��, �� �ڵ带 ���α׷��� ó�� �κп� �߰��ϸ� ���� �Է��� ������ ��
		 * ǥ�� �Է� ��� ���Ϸκ��� �Է��� �޾ƿ� �� �ֽ��ϴ�. ���� �׽�Ʈ�� ������ ������ �Ʒ� �ּ��� ����� �� �޼ҵ带 ����ϼŵ� �����ϴ�.
		 * ��, ä���� ���� �ڵ带 �����Ͻ� ������ �ݵ�� �� �޼ҵ带 ����ų� �ּ� ó�� �ϼž� �մϴ�.
		 */
//System.setIn(new FileInputStream("res/input.txt"));

		/*
		 * ǥ���Է� System.in ���κ��� ��ĳ�ʸ� ����� �����͸� �о�ɴϴ�.
		 */
		Scanner sc = new Scanner(System.in);
		int T;
		T = sc.nextInt();
		/*
		 * ���� ���� �׽�Ʈ ���̽��� �־����Ƿ�, ������ ó���մϴ�.
		 */
		StringBuffer sb = new StringBuffer();
		int[] wonList = { 50000, 10000, 5000, 1000, 500, 100, 50, 10 };
		for (int test_case = 1; test_case <= T; test_case++) {
			sb.append("#").append(test_case).append("\n");
			int won = sc.nextInt();
			int usedWonList[] = { 0, 0, 0, 0, 0, 0, 0, 0 };
			for(int i = 0 ; i < wonList.length;i++) {
				if(won >= wonList[i]) {
					int cnt = won/wonList[i];
					won -= wonList[i]*cnt;
					usedWonList[i] += cnt;
				}
			}
			for(int i = 0 ; i< wonList.length;i++) {
				sb.append(usedWonList[i]).append(" ");
			}
			sb.append("\n");
		}
		System.out.println(sb);
	}
}