import java.util.*;
class Calculate{
	public static void main(String args[]){
		Scanner x=new Scanner(System.in);
		int i=1;
		do{
		System.out.println("Enter integer number 1");
		int n1=x.nextInt();
		System.out.println("Enter integer number 2");
		int n2=x.nextInt();
		System.out.println("Enter your choice 1. Addition 2. Subtraction 3.Multiplication 4.Divison");
		int c=x.nextInt();
		switch(c)
		{
			case 1: System.out.println(n1+n2);
				break;

			case 2: System.out.println(n1-n2);
				break;

			case 3: System.out.println(n1*n2);
				break;

			case 4: System.out.println(n1/n2);
				break;

			default: System.out.println("Invalid choice");
				break;
		}
		System.out.print("Enter 1 to do another calculation ");
		i=x.nextInt();
		}while(i==1);

	}
}
