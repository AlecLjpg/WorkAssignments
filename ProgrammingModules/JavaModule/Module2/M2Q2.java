import java.util.Scanner;

class Document{
    String text;
    
    public void setText(String text) {
        this.text = text;
    }
    public String toString(){
        return text;
    }

    public static void main(String[] args) {
        Email newEmail = new Email();
        Document doc = new Document();
        Scanner uInput = new Scanner(System.in);
        System.out.println("Enter the email recipient: ");
        newEmail.setRecipient(uInput.nextLine());
        System.out.println("Enter the email sender: ");
        newEmail.setSender(uInput.nextLine());
        System.out.println("Enter the email title: ");
        newEmail.setTitle(uInput.nextLine());
        System.out.println("Enter the body of the email: ");
        doc.setText(uInput.nextLine());
        uInput.close();
        System.out.println("Sender: " + newEmail.getSender() + "\nRecipient: " + newEmail.getRecipient() + "\nSubject: " + newEmail.getTitle() + "\nBody:" + doc.toString());
    }

}

class Email extends Document{
    String sender;
    String recipient;
    String title;
    
    public String getRecipient() {
        return recipient;
    }
    public void setRecipient(String recipient) {
        this.recipient = recipient;
    }


    public String getSender() {
        return sender;
    }
    public void setSender(String sender) {
        this.sender = sender;
    }

    
    public String getTitle() {
        return title;
    }
    public void setTitle(String title) {
        this.title = title;
    }



}