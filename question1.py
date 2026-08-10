# Parking Fee Calculator

hours = int(input("Enter the hours of parking:"))

if hours <= 2:
    parking_charge = 30 * hours
elif hours <= 5:
    parking_charge = 50 * hours
else:
    parking_charge = 20 * hours

if parking_charge > 150:
    service_charge = 20
else:
    service_charge = 0

final_amount = parking_charge + service_charge

print("Parking Charge: ₹ ",parking_charge)
print("Service Charge: ₹ ",service_charge)
print("Final Amount: ₹ ",final_amount)
        