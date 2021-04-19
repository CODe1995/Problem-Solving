package boj1708;
import java.util.*;
import java.io.*;

public class Main_boj_1708_볼록껍질 {
	static StringBuilder sb = new StringBuilder();
	static int N;
	static Pos arr[];
	static class Pos implements Comparable<Pos>{
		long x,y,p,q;
		public Pos(long x, long y) {
			this.x = x;
			this.y = y;
			p=1;q=0;
		}
		@Override
		public int compareTo(Pos o) {
			long a = this.p*o.q;
			long b = this.q*o.p;
			if(a!=b) {
				if(a==b)return 0;
				else if(a<b)return 1;
				return -1;
			}			
			if(this.y==o.y) {
				if(this.x<o.x) {
					return 1;
				}
				return -1;
			}else if(this.y<o.y)
				return 1;
			return -1;
		}
	}
	static long ccw(Pos A, Pos B, Pos C) {
	    return A.x * B.y + B.x * C.y + C.x * A.y - B.x * A.y - C.x * B.y - A.x * C.y;
	}
	static void input() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		N = Integer.parseInt(br.readLine());
		arr = new Pos[N];
		for(int i =0;i<N;i++) {
			st = new StringTokenizer(br.readLine());
			arr[i] = new Pos(Integer.parseInt(st.nextToken()),Integer.parseInt(st.nextToken()));
		}
		Arrays.sort(arr);//y좌표 기준으로 정렬
		for(int i=1;i<N;i++) {//기준점으로부터 위치계산
			arr[i].p = arr[i].x-arr[0].x;
			arr[i].q = arr[i].y-arr[0].y;
		}
		Arrays.sort(arr, 1, arr.length);//기준점 제외하고 반시계로 정렬
		
		Stack<Integer> stack = new Stack<>();
		stack.add(0);//first
		stack.add(1);//second
		int next= 2;
		while(next<N) {
			while(stack.size()>=2) {
				int first,second;
				second = stack.pop();
				first = stack.peek();
				//좌회전인지 확인 아니라면 while 반복
				if(ccw(arr[first],arr[second],arr[next])>0) {
					stack.add(second);
					break;
				}
			}
			stack.add(next++);
		}
		System.out.println(stack.size());
	}

	public static void main(String[] args) throws IOException {
		input();
	}
}