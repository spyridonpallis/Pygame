class Animal:
    def __init__(self, name, species, age, location, owner, notes):
        self.name = name
        self.species = species
        self.age = age
        self.location = location
        self.owner = owner
        self.notes = notes

class AnimalManager:
    def __init__(self):
        self.animals = []
        
    def add_animal(self, animal):
        self.animals.append(animal)
        
    def update_animal(self, name, new_animal):
        for i, animal in enumerate(self.animals):
            if animal.name == name:
                self.animals[i] = new_animal
                break
                
    def delete_animal(self, name):
        for i, animal in enumerate(self.animals):
            if animal.name == name:
                del self.animals[i]
                break

# Example usage

animal_manager = AnimalManager()

# Add animals
animal_manager.add_animal(Animal("Buddy", "dog", 5, "USA", "John Doe", "Loyal pet"))
animal_manager.add_animal(Animal("Sasha", "cat", 3, "Canada", "Jane Doe", "Playful cat"))
animal_manager.add_animal(Animal("Max", "horse", 7, "Mexico", "Jim Smith", "Fast runner"))

# Update an animal
animal_manager.update_animal("Sasha", Animal("Sasha", "cat", 4, "Canada", "Jane Doe", "Adventurous cat"))

# Delete an animal
animal_manager.delete_animal("Max")

# Print the animals in the Terminal
for animal in animal_manager.animals:
    print("Name:", animal.name)
    print("Species:", animal.species)
    print("Age:", animal.age)
    print("Location:", animal.location)
    print("Owner:", animal.owner)
    print("Notes:", animal.notes)
    print()
