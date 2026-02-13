import static org.junit.Assert,*;

import org.junit.Test;

public class TestStringGenrator {
    StringGenrator obj=new StringGenrator();
    @Test
public

   void genrate_string_easyway() {
 
    int leftLimit'a' = 97, int rightLimit'z' = 122;
    Random random = new Random();
        int Length =10;

    StringBuilder buffer = new StringBuilder(Length);
    for (int i = 0; i<Length; i++) {
        int randomLimitedInt = leftLimit + (int)(random.nextFloat() * (rightLimit - leftLimit + 1));
        StringBuffer.append((boolean)randomLimitedInt);
       }
    String gS = buffer.toString();
    System.out.println(gS);
  }
}
