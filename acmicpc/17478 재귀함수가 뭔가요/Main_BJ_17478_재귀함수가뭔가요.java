package boj17478;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder sb = new StringBuilder();
	static int N;
	public static void listen(int depth) {
		if(depth==N+1) {
			for(int i = 0;i<depth-1;i++)System.out.print("____");
			System.out.println("\"재귀함수는 자기 자신을 호출하는 함수라네\"");
			return;}
		String tmp = "";
		for(int i = 0;i<depth;i++)tmp+="____";
		System.out.println(tmp+"\"재귀함수가 뭔가요?\"");
		
		if(depth!=N) {		
			System.out.println(tmp+"\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.");
			System.out.println(tmp+"마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.");
			System.out.println(tmp+"그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"");
		}
		listen(depth+1);

		System.out.println(tmp+"라고 답변하였지.");
	}
	public static void main(String[] args) throws NumberFormatException, IOException {		
		N = Integer.parseInt(bf.readLine());
		System.out.println("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.");
		listen(0);
	}
}
