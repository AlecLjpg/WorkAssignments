class M1Q8 {
	public static void main(String[] args){
		Book newBook = new Book (12345678, "BookTest","fAuthor","lAuthor", 30.00);
		newBook.discountedPrice();
		newBook.displayDetails();
	}
}

class Book {
	int bookIsbn;
	String bookTitle;
	String authorFirst;
	String authorLast;
	String authorFull;
	double bookPrice;

	public Book(int isbn, String title, String first, String last, double price){
		bookIsbn = isbn;
		bookTitle = title;
		authorFull = (last + ", "+first);
		bookPrice = price;
	}
	public double discountedPrice() {
		return (bookPrice * 0.9);
	}
	public void displayDetails() {
		System.out.println("ISBN: " + bookIsbn);
		System.out.println("Title: "+bookTitle);
		System.out.println("Author: " + authorFull);
		System.out.println("Price (after 10% discount): " + discountedPrice());
	}
} 
