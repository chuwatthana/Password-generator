import random 
character=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","X","T","U","V","W","X","Y","Z",]
numbers=['1','2','3','4','5','6','7','8','9',]
symbols=['!','#','$','%','@','*','+']


nr_character=int(input("How many letter would you like in your password"))
nr_symbols=int(input("How many symbols would you like in your password"))
nr_number=int(input("How many number would you like in your password"))

password=[]
for char in range(1,nr_character+1):
   password+=random.choice(character)

for char in range(1,nr_symbols+1):
   password+=random.choice(symbols)

for char in range(1,nr_number+1):
   password+=random.choice(numbers)

random.shuffle(password)

final_password=""

for char in password:
   final_password+=char

print(f"your password would be :",final_password)
