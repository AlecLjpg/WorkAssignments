class EmployeeMain {
    public static void main(String[] args) {
        String employeeName = args[0];
        String dept = args[1];
        String designation = args[2];
        double basicSalary =  Double.parseDouble(args[3]);

        if(dept == "Mgr"){
            Manager x1 = new Manager(employeeName, dept, designation, basicSalary);
            x1.employeeDetails();
        }
        else{
            Clerk x1 = new Clerk(employeeName, dept, designation, basicSalary);
            x1.employeeDetails();
        }
    
        }

    }
}

class Employee {

    public Employee(String emName, String dep, String desig, double bSalary){
        employeeName = emName;
        dept = dep;
        designation = desig;
        basicSalary = bSalary;
    }

    public void employeeDetails(){
        print("Name: " + this.employeeName);
        print("Dept: " + this.dept);
        print("Designation: " + this.designation);
        print("Salary:" + this.basicSalary);
    }
}

class Manager extends Employee{
    
    public Manager(String emName, String dep, String desig, double bSalary) {
        super(emName, dep, desig, bSalary);
    }

    double calculateSalary(double basicSalary) {
        return (basicSalary*10);
    }
}

class Clerk extends Employee{

    public Clerk(String emName, String dep, String desig, double bSalary) {
        super(emName, dep, desig, bSalary);

    }

    double calculateSalary(double basicSalary) {
        return (basicSalary*3);
    }
}