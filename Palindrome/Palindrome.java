import java.util.Scanner;
public class Palindromo{
	// testenado o merge
	public static void checkPalindromo(int num){
		int novonumero = 0;
		int temp = num;
		int unidade = 0;
		for(int i=0; i<5; ++i){
			unidade = temp % 10;
			temp /=10;
			novonumero*=10;
			novonumero += unidade;
		}
		if(novonumero == num) System.out.println("São palindromos");
	}

	public static void main(String[] args){
		Scanner input = new Scanner(System.in);
		int num = 1;
		
		while(num != 0){
		System.out.println("Caso queira parar, digite 0");
		System.out.println("Informe o número: ");
		num = input.nextInt();

		if(num > 9999) checkPalindromo(num);
		else System.out.println("Número não aceito");
		}
	}
}
