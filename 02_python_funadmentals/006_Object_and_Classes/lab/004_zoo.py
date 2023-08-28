class Zoo:
    __animals = 0


    def __init__(self, n):
        self.zoo_name = n
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animals(self, species, name):
        self.name = name
        if species == 'mammal':
            self.mammals.append(self.name)
        elif species == 'fish':
            self.fishes.append(self.name)
        elif species == 'bird':
            self.birds.append(self.name)
        Zoo.__animals += 1

    def get_info(self, species):
        result = ''
        if species == 'mammal':
            result += f"Mammals in {self.zoo_name}: {', '.join(self.mammals)}\n"
        elif species == 'fish':
            result += f"Fishes in {self.zoo_name}: {', '.join(self.fishes)}\n"
        elif species == 'bird':
            result += f"Birds in {self.zoo_name}: {', '.join(self.birds)}\n"
        result += f"Total animals: {Zoo.__animals}"
        return result



zoo_n = input()
zoo = Zoo(zoo_n)
num = int(input())
for i in range(num):
    line = input().split()
    species = line[0]
    name = line[1]
    zoo.add_animals(species, name)

print(zoo.get_info(input()))

