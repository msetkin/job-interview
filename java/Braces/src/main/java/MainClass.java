import org.junit.Assert;

public class MainClass {

  /**
    * checks if the input string brace-wise balanced. "Balanced" means, that the number and the
    * order of opening and closing brackets are symmetrical. See test-cases for more details.
    *
    * @param  someString  input string, can contain opening or closing braces: parentheses, square and curly brackets
    * @return  true is the input string is "balanced" and false otherwise
    */
  public static boolean isStringBraceBalanced(String someString) {
      /* your solution goes here */
      return true;
  }

  public static void main(String[] args) {
    Assert.assertTrue(isStringBraceBalanced("({[]})"));
    Assert.assertFalse(isStringBraceBalanced("({[}])"));
    Assert.assertFalse(isStringBraceBalanced("({[}]))))"));
    Assert.assertTrue(isStringBraceBalanced(""));
    Assert.assertFalse(isStringBraceBalanced("}{][)("));
    Assert.assertFalse(isStringBraceBalanced("}{][)]("));
    Assert.assertFalse(isStringBraceBalanced("(((({{{{{"));
    Assert.assertFalse(isStringBraceBalanced("]]])}}})}}}}"));
    Assert.assertTrue(isStringBraceBalanced("(()){}"));
  }
}
