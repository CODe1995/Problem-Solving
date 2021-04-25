package boj;
import java.util.*;
import java.io.*;

public class Main_boj_2699_격자점컨벡스헐 {
	static StringBuilder sb = new StringBuilder();
	static class Pos{
		int x,y;
		public Pos(int x, int y) {this.x = x;this.y = y;}
	}
	static int ccw(Pos A,Pos B,Pos C) {
		int a = A.x*B.y+B.x*C.y+C.x*A.y;
		int b = A.y*B.x+B.y*C.x+C.y*A.x;
		return a-b;
	}
	static void input() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int N = stoi(br.readLine());
		ArrayList<Pos> edge = new ArrayList<>();
		for(int i =0;i<N;i++) {
			st = new StringTokenizer(br.readLine());
			edge.add(new Pos(stoi(st.nextToken()),stoi(st.nextToken())));
		}
		Collections.sort(edge,(o1,o2)->o1.y-o2.y);
		
	}
	static void sortEdge() {
		
	}
	static int stoi(String s) {
		return Integer.parseInt(s);
	}
	public static void main(String[] args) throws IOException {
		input();
	}
}