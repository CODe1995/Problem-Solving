package boj2941;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
	public static void main(String[] args) throws IOException {
//		StringTokenizer st = new StringTokenizer(bf.readLine());
		String input = bf.readLine();
		String alpha[] = {"c=","c-","dz=","d-","lj","nj","s=","z="};
		int answer =0 ;
		int index = 0;
		while(index<input.length()) {
			boolean flag = false;
			if(input.length()<=1) {answer=1;break;}
			for (String x:alpha)
				if(input.length()>=index+x.length()&&input.substring(index,index+x.length()).equals(x)) {
					index+=x.length();
					answer++;
					flag = true;
					break;
				}
			if(!flag) {
				index+=1;
				answer++;
			}
		}
		System.out.println(answer);
	}
}
