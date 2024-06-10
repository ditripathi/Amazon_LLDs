from abc import ABC, abstractmethod

# Abstract Base Class (Abstract Class)
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
    
    def eat(self):
        print("Eating...")

# Abstract Base Class (Interface)
class Pet(ABC):
    @abstractmethod
    def play(self):
        pass

# Concrete Class implementing multiple interfaces using multiple inheritance
class Dog(Animal, Pet):
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        print("Bark")

    def play(self):
        print("Playing with the ball")

    def eat(self):
        # Use super() to call the method from the Animal class
        super().eat()
        print(f"{self.name} is eating.")

# Another Abstract Base Class (Interface)
class ServiceAnimal(ABC):
    @abstractmethod
    def serve(self):
        pass

# Concrete Class extending Dog and implementing ServiceAnimal
class ServiceDog(Dog, ServiceAnimal):
    def __init__(self, name, service):
        # Use super() to call the constructor of the parent class
        super().__init__(name)
        self.service = service
    
    def serve(self):
        print(f"{self.name} is serving by {self.service}")

    def make_sound(self):
        # Use super() to call the method from the Dog class
        super().make_sound()
        print(f"{self.name} makes a loud bark when on duty")

# Example Usage
if __name__ == "__main__":
    dog = Dog("Buddy")
    dog.make_sound()  # Output: Bark
    dog.play()        # Output: Playing with the ball
    dog.eat()         # Output: Eating... \n Buddy is eating.

    service_dog = ServiceDog("Max", "guiding the blind")
    service_dog.make_sound()  # Output: Bark \n Max makes a loud bark when on duty
    service_dog.play()        # Output: Playing with the ball
    service_dog.eat()         # Output: Eating... \n Max is eating.
    service_dog.serve()       # Output: Max is serving by guiding the blind

