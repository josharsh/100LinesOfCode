import java.util.Scanner;
class question14
{
    public static void main(String[] arg)
    {
        Scanner sa=new Scanner(System.in);
        System.out.println("Queston 14 : Program to print user menu and take input of two numbers and perform operation according to the user choice using switch case. ");
        System.out.println("Answer:");
        System.out.println("Enter two numbers:");
        int a = sa.nextInt();
        int b = sa.nextInt();
        System.out.println("Press 1 for addition");
        System.out.println("Press 2 for substraction");
        System.out.println("Press 3 for multiplication");
        System.out.println("Press 4 for division");
        System.out.println("\n\n Enter your choice");
        int choice = sa.nextInt();
        switch(choice)
        {
            case 1:
                   System.out.println("addition = "+(a+b));
                   break;
            case 2:
                   System.out.println("substraction = "+(a-b)); 
                   break;
            case 3:
                   System.out.println("multiplication = "+(a*b)); 
                   break;
            case 4:
                   System.out.println("divison = "+(a/b)); 
                   break;
            default:
                   System.out.println("Invalid Input"); 
                   break; 
         }
       }
}
    