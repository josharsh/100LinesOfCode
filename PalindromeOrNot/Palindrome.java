
class Palindrome {

  public static void main(String[] args) {

    String inputString = "ThisIsFun";
    //String inputString = "radar";

    boolean isPalindrome = true;

    //if its empty string or single letter then consider it as palindrone.
    if(inputString.length >1) {
      //Iterate through chars from start and end and check if char matches
      for (int i = 0; i < inputString.length() / 2; i++) {
        if (inputString.charAt(i) != inputString.charAt(inputString.length() - 1 - i)) {
          isPalindrome = false;
          break;
        }
      }
    }

    //Print the result
    if(isPalindrome) {
      System.out.println(inputString+" is Palindrome.");
    } else {
      System.out.println(inputString+" is not Palindrome.");
    }
  }

}