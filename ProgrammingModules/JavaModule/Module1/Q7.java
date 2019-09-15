import java.util.Scanner;

class M1Q7 {
	public static void main(String[] args) {
		Scanner inputScanner = new Scanner(System.in);
		System.out.println("Enter a number to find the factorial: ");
		int input = inputScanner.nextInt();
		int num = input;
		int res = factorial(num);
        System.out.println("The factorial is: " + res);
        inputScanner.close();
	}
	public static int factorial(int x) {
		if(x==0)
			return 1;
		else return (x*factorial(x-1));
	}
}
