#simulating a football match ticket system
#create a set of 1-50 numbers 
seat_numbers = set(range(1,51))
print(seat_numbers)
booked= []

for x in range (1,51):
    selected_seat=int(input("please enter the seat number you want to book from 1-50: "))
    if selected_seat in booked:
        print("❌❌❌❌❌❌❌❌❌❌❌".center(100))
        print("This seat has already been reserved by someone else")
    else:
        seat_numbers.remove(selected_seat)
        booked.append(selected_seat)
        print(f"Booking confirmed ✅✅✅✅✅\n seat {selected_seat} has been reserved for you")
else:
    print("all seats are booked")
print("no seat no")  


# print(seat_numbers)
#use the try and except thing for task 10