#simulating a football match ticket system
#create a set of 1-50 numbers 
seat_numbers = set(range(1,51))
print(seat_numbers)
booked= []

while True:    
    try:
        selected_seat=int(input("please enter the seat number you want to book from 1-50: "))
        for x in range(50):
            if selected_seat in booked:
                    print("❌❌❌❌❌❌❌❌❌❌❌".center(100))
                    print("This seat has already been reserved by someone else")
            elif selected_seat not in booked:
                    seat_numbers.remove(selected_seat)
                    booked.append(selected_seat)
                    print(f"Booking confirmed ✅✅✅✅✅\n seat {selected_seat} has been reserved for you")
                    
            elif seat_numbers == set():
                print("all seats are booked")
                print("no seat no")
                break
            print(seat_numbers)
    except TypeError as e:
            print("Error: ",e)
    except ValueError:
            print("invalid input")
    except Exception as e:
            print("Error:",e)
    
    #use the try and except thing for task 10