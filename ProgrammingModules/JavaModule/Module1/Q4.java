import java.util.Scanner;
import java.util.Arrays;
class M1Q4 {
	public static void main(String args[]) {
		Scanner uInput = new Scanner(System.in);
		System.out.println("Input a four digit number: ");
		String input = uInput.nextLine();
		char[] charArr = input.toCharArray();
		int[] intArr = new int[4];
		int sum = 0;
		for(int i = 0; i < intArr.length; i ++) {
			sum = sum + Character.getNumericValue(charArr[i]);
		}
        System.out.println("The sum of all digits is : " + sum);
        uInput.close();
	}
}		
