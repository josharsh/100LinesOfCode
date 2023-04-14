public class Password{
    public static void main(String[] args) {
        String alpha[] = {"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"};
        int number[] = {0,1,2,3,4,5,6,7,8,9};
        int randomAlpha = 0;
        int randomNum = 0;
        String PasswordString = "";
        String PasswordNum = "";

        do{
            randomAlpha=(int)(Math.random()*alpha.length);
            PasswordString+=alpha[randomAlpha];
            randomNum=(int)(Math.random()*number.length);
            PasswordNum+=String.valueOf(number[randomNum]);
        }while(PasswordString.length()!=4);

        String finalPassword = PasswordString.substring(0,1).toUpperCase()+PasswordString.substring(1)+"@"+PasswordNum;
         System.out.println("Your password is "+finalPassword);
    }
}