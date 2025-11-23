import random

player_name = "Vivan"
score = 0
lives = 3

print("Welcome,", player_name)
print("Score:", score, "| Lives:", lives)
print("---------------------------------\n")


snacks = ["biscuits", "chips", "chocolate"]
snacks.append("juice")  

print("Available snacks:", snacks)

def move_direction(direction):
    if direction == "up":
        return "You walked north."
    elif direction == "down":
        return "You walked south."
    elif direction == "left":
        return "You walked west."
    elif direction == "right":
        return "You walked east."
    else:
        return "Invalid direction."

print("\nDirection Example:", move_direction("up"))

class Player:
    def __init__(self, name):
        self.name = name
        self.x = 0   
        self.y = 0

    def move(self, direction):
        if direction == "up":
            self.y += 1
        elif direction == "down":
            self.y -= 1
        elif direction == "left":
            self.x -= 1
        elif direction == "right":
            self.x += 1
        else:
            print("Invalid move command.")

        print(f"{self.name} moved {direction}. Current position: ({self.x}, {self.y})")



player = Player(player_name)

player.move("up")
player.move("right")
player.move("right")

food_x = random.randint(0, 5)
food_y = random.randint(0, 5)

print("\n🍎 Food spawned at:", (food_x, food_y))


print("\nEating snacks...")

while len(snacks) > 0:
    current_snack = snacks.pop(0)
    print("You ate:", current_snack)

print("No snacks left!\n")



print("Counting from 1 to 5:")
for number in range(1, 6):
    print(number)

print("\nProgram finished successfully!")
