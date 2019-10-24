import java.security.SecureRandom;
import java.util.Scanner;
class PasswordGenerator {
    private static SecureRandom random = new SecureRandom();
    private static final String ALPHA_CAPS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    private static final String ALPHA = "abcdefghijklmnopqrstuvwxyz";
    private static final String NUMERIC = "0123456789";
    private static final String SPECIAL_CHARS = "!@#$%^&*_=+-/";
    static String password = "";
    public static String generatePassword(int len, String dic) {
	String result = "";
	for (int i = 0; i < len; i++) {
	    int index = random.nextInt(dic.length());
	    result += dic.charAt(index);
	}
	return result;
    }

    public static void main(String[] args) {
	System.out.println("Password Generator Examples");
	Scanner lenth = new Scanner(System.in);
	System.out.println("Enter Length: ");
	int len = lenth.nextInt();
	System.out.println("Password is: ");
	password = generatePassword(len, ALPHA_CAPS + ALPHA + SPECIAL_CHARS + NUMERIC);
	System.out.println(password);
	System.out.println();
    }
}
