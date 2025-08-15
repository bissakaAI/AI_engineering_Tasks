#Nigeria School fees breakdown
School_name = input("what is the name of your school: ")
Tuition = float(input("How much is your tuition fee: "))
Hostel_fee = float(input("How much is charges as hostel fee: "))
Feeding_fee = float(input("how much is the feeding fee: "))

Total_fee = Tuition + Hostel_fee + Feeding_fee

print(f"\tSCHOOL FEES RECEIPT for {School_name}\nTuition fee\t {Tuition:,}\nHostel fee\t {Hostel_fee:,}\nFeeding fee\t {Feeding_fee:,}\nTotal\t\t {Total_fee:,}")

