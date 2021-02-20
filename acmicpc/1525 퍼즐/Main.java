package boj1525;
import java.util.*;
import java.io.*;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;

	public static void main(String[] args) throws IOException {
		String field = "";
		for(int i=0;i<3;i++) {
			st = new StringTokenizer(br.readLine());
			for(int j =0;j<3;j++) {
				char input = st.nextToken().charAt(0);
				field+=input;
			}
		}
		Deque<String> dq = new ArrayDeque<>();
		dq.add(field);
		HashMap<String, Integer> visited = new HashMap<>();
		visited.put(field, 0);
		
		int direction[][] = new int[][]{{0,1},{1,0},{-1,0},{0,-1}};
		while(!dq.isEmpty()) {
			String current_puzzle = dq.pollFirst();
			int pos0 = current_puzzle.indexOf('0');
			int x = pos0%3;
			int y =pos0/3;
			for(int[] pos:direction) {
				int nx = x+pos[0],ny = y+pos[1];
				if(0>nx || 0>ny || ny>=3 || nx>=3)continue;//범위체크				
				//원래좌표 -> 새로운좌표 변경
				char target = current_puzzle.charAt(nx+ny*3);
				StringBuilder ssb = new StringBuilder(current_puzzle);//swap
//				print(ssb.toString());
				ssb.setCharAt(pos0, target);
				ssb.setCharAt(nx+ny*3, '0');
//				print(ssb.toString());
				if(visited.get(ssb.toString())==null) {//visited체크, 이미 있다면?
					visited.put(ssb.toString(),visited.get(current_puzzle)+1);//이동거리+1
					dq.add(ssb.toString());
				}
			}
		}
		if(visited.get("123456780")!=null) {
			System.out.println(visited.get("123456780"));
		}
		else {
			System.out.println(-1);
		}
	}
	public static void print(String s) {
		System.out.println("========");
		for(int j=0;j<3;j++) {
			for(int i =0;i<3;i++) {
				System.out.print(s.charAt(i+j*3));
			}
			System.out.println();
		}
	}
	public static int contains(char[] arr) {
        int num = Integer.parseInt(new String(arr));
        return num;//숫자로반환 
    }
}