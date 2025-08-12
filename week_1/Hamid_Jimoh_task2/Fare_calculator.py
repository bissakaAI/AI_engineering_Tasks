# task8
# transport fare calculator
# use a code that asks for the km to be travelled (float) 
# and a code that asks for the fare per km (float)
# code that multiplies km by fare per km

travel_distance = float(input("how many km's is the journey: "))
fare_pkm = float(input("what is the fare charged per km: "))

Transp_fare = travel_distance * fare_pkm

print(f"the transport fare for the journey is {Transp_fare:.2f}")
