public class Password{
    public static void main(String[] args) {
        String[] alpha = {"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"};
        int[] number = {0,1,2,3,4,5,6,7,8,9};
        int randomAlpha = 0;
        int randomNum = 0;
        String passwordString = "";
        String passwordNum = "";

        do{
            randomAlpha=(int)(Math.random()*alpha.length);
            passwordString+=alpha[randomAlpha];
            randomNum=(int)(Math.random()*number.length);
            passwordNum+=String.valueOf(number[randomNum]);
        }while(passwordString.length()!=4);

        String finalPassword = passwordString.substring(0,1).toUpperCase()+passwordString.substring(1)+"@"+passwordNum;
         System.out.println("Your password is "+finalPassword);
    }
}