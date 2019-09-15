import java.util.Scanner;

class Animal{
    String type;
    String color;
    String shout;
    String food;
    public Animal(){}
   
    public Animal(String ty, String col, String foo){
        this.type = ty;
        this.color = col;
        this.food = foo;
    }
    public String getType(){
        return type;
    }
    public void setType(String type){
        this.type = type;
    }
    public String getFood(){
        return food;
    }
    public void setFood(String food){
        this.food = food;
    }
    public String getColor(){
        return color;
    }
    public void setColor(String color){
        this.color = color;
    }
    public String getShout(){
        return shout;
    }
    public static void main(String[] args) {
        Animal[] anArray = new Animal[10];
        Dog dog = new Dog("dog","brown","kibble");
        Horse horse = new Horse("horse","white","apples");
        Cat cat = new Cat("cat","black","mice");
        anArray[0] = dog;
        anArray[1] = horse;
        anArray[2] = cat;
        for(Animal ob : anArray){
            System.out.println("The " + ob.getColor() + " " + ob.getType() + " eats " + ob.getFood() + " and goes " + ob.getShout() + "!");
    
        } 

    }
}

class Dog extends Animal{
    private String shout;
    
    public Dog(String type, String color, String food){
        super(type, color, food);
        this.shout = "woof";
    }
    public Dog(String type, String color, String food, String shout){
        super(type, color, food);
        this.shout = shout;
    }
    public String getShout(){
        return shout;
    }
}

class Horse extends Animal{
    private String shout;
    public Horse(String type, String color, String food){
        super(type,color,food);
        this.shout = "neigh";
    }
    public Horse(String type, String color, String food, String shout){
        super(type,color,food);
        this.shout = shout;
    }
    public String getShout(){
        return shout;
    }
}

class Cat extends Animal{
    private String shout;
    public Cat(String type, String color, String food){
        super(type,color,food);
        this.shout = "meow";
    }
    public Cat(String type, String color, String food, String shout){
        super(type, color, shout);
        this.shout = shout;
    }
    public String getShout(){
        return shout;
    }
}