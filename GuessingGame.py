from modules import func 
print("Guessing Game\n--------------")
print("Choose a difficulty:")
print("1 - Easy - 1 - 5")
print("2 - Medium - 1 - 8")
print("3 - Hard - 1 - 12")
print("4 - Custom - 1 - ??")
type = int(input("Difficulty: "))
func.startGame(type)