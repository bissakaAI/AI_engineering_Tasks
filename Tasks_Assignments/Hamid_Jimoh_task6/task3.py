#simulating a football match ticket system
#create a set of 1-50 numbers 
seat_numbers = set(range(1,51))
print(seat_numbers)
for x in range (1,51):
    selected_seat=int(input("please enter the seat number you want to book from 1-50: "))
    if selected_seat not in seat_numbers:
        print("this seat is not available")
    else:
        seat_numbers.remove(selected_seat)
        x= x+1
        print(seat_numbers)

