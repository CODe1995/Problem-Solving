package boj1747;

import java.util.Scanner;

public class Main {
	static int n;
	static int max = 1000001;
	static int[] arr = new int[max];//0:¼Ò¼ö
	static int answer = 0;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		arr[0]=1;arr[1]=1;
		n = sc.nextInt();
		for(int i = 2;i<max;i++) {
			if(arr[i]==1)continue;
			for(int j = 2*i;j<max;j+=i)
				arr[j]=1;
		}
		for(int i = n;i<max;i++) {
			if(arr[i]==0) {
				String tmp = Integer.toString(i);
				StringBuffer sb = new StringBuffer();
				sb.append(tmp);
				if(sb.reverse().substring(0, tmp.length()/2).equals(tmp.substring(0,tmp.length()/2))) {
					answer = i;
					break;
				}
			}
		}
		if(answer==0)answer=1003001;		
		System.out.println(answer);
		sc.close();
	}
}
