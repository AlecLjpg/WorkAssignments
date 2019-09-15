import java.util.Scanner;
	class M1Q2 {
		public static void main(String args[]) {
			Scanner userInput = new Scanner(System.in);
			System.out.println("Enter a number of minutes for conversion: ");
			double minutes = userInput.nextDouble();
			double days = (minutes/1440);
			double years = (minutes/525600);
			System.out.println(minutes + " minutes is equivalent to " + days + " days and " + 
            years + " years");
            userInput.close();
		}
	}
