package boj1002;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj1002 {	
	public static void main(String[] args) throws IOException{
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(bf.readLine());
		int T= Integer.parseInt(st.nextToken());
		for(int t = 0;t<T;t++) {
			double x1,y1,r1,x2,y2,r2,d;
			st = new StringTokenizer(bf.readLine());
			x1 = Double.parseDouble(st.nextToken());
			y1 = Double.parseDouble(st.nextToken());
			r1 = Double.parseDouble(st.nextToken());
			x2 = Double.parseDouble(st.nextToken());
			y2 = Double.parseDouble(st.nextToken());
			r2 = Double.parseDouble(st.nextToken());
			double x = x2-x1;
			double y = y2-y1;			
			d =  Math.sqrt(x*x+y*y);
			if(d==0 && r1==r2)//원이 완전히 겹치는 경우(거리0,반지름동일)
				System.out.println(-1);
			else if(d==Math.abs(r1-r2) || r1+r2==d)//원이  내접하는 경우, 외접하는 경우				
				System.out.println(1);
			else if(Math.abs(r1-r2)<d && d<r1+r2)
				System.out.println(2);
			else
				System.out.println(0);
		}
	}
}
