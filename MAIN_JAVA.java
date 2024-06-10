// Abstract Base Class
abstract class Animal {
    // Abstract method (must be implemented by subclasses)
    abstract void makeSound();
    
    // Concrete method
    void eat() {
        System.out.println("Eating...");
    }
}

// Interface 1
interface Pet {
    void play();
}

// Interface 2
interface ServiceAnimal {
    void serve();
}

// Concrete Class inheriting from Animal and implementing Pet and ServiceAnimal interfaces
class Dog extends Animal implements Pet, ServiceAnimal {
    private String name;

    // Constructor
    public Dog(String name) {
        this.name = name;
    }

    // Implementing the abstract method from Animal
    @Override
    void makeSound() {
        System.out.println(name + " says: Bark");
    }

    // Implementing the play method from Pet interface
    @Override
    public void play() {
        System.out.println(name + " is playing with the ball");
    }

    // Implementing the serve method from ServiceAnimal interface
    @Override
    public void serve() {
        System.out.println(name + " is serving as a guide dog");
    }

    // Overriding the eat method from Animal
    @Override
    void eat() {
        // Using super to call the parent class's eat method
        super.eat();
        System.out.println(name + " is eating dog food");
    }
}

// Main class to demonstrate the functionality
public class Main {
    public static void main(String[] args) {
        // Creating an instance of Dog
        Dog myDog = new Dog("Buddy");

        // Calling methods
        myDog.makeSound();  // Buddy says: Bark
        myDog.play();       // Buddy is playing with the ball
        myDog.serve();      // Buddy is serving as a guide dog
        myDog.eat();        // Eating... \n Buddy is eating dog food
    }
}
