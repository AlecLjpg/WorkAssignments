
class M2Q1 {
	public static void main(String[] args){
		Student newStudent = new Student(1,"John","Smith",1235435453, "History", 124.2);
		newStudent.displayDetails();
        Student newStudent1 = new Student(2,"James","Smith",1235435453, "History", 130.2);
		newStudent1.displayDetails();
        Student newStudent2 = new Student(3,"Bob","Smith",1235435453, "History", 200.2);
		newStudent2.displayDetails();
        Student newStudent3 = new Student(4,"Alex","Smith",1235435453, "History", 50.2);
		newStudent3.displayDetails();
        Student newStudent4 = new Student(5,"Rick","Smith",1235435453, "History", 124.2);
		newStudent4.displayDetails();
		newStudent.studentFees();
	}
}
class Student {
	int studentId;
	String studentF;
	String studentL;
	String studentFull;
	int contactNo;
	String course;
	double fees;
	static double totalFees;
	public Student(int sId, String sF, String sL, int coNo, String sC, double fee) {
		studentId = sId;
		studentFull = (sF + " " +sL);
		contactNo = coNo;
		course = sC;
		fees = fee;
	}
	public void displayDetails() {
		System.out.println("Student name: " + studentFull );
        System.out.println("Student ID: " + studentId); 
        System.out.println("Contact #: " + contactNo );
        System.out.println("Course: " + course);
        totalFees = totalFees + fees;
	}
	public void studentFees(){
		System.out.println("Total fees for all student: $" + totalFees);
	}
}
