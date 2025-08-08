"""
SHIPPING CALCULATOR 

Rules:
1. Base Cost by Weight:
o For orders weighing 0 to 5 kg (inclusive): P50.00
o For orders weighing 5.01 to 10 kg (inclusive): P100.00
o For orders weighing over 10 kg: P150.00
2. Destination Surcharge:
o If the destination is 'International': Add an additional P7.50 to the base cost.
o If the destination is 'Domestic': No additional surcharge.
3. Priority Shipment Fee:
o If the shipment is marked as 'Priority': Add an additional 20% of the total cost
(base cost + destination surcharge).

Input:
The program will prompt the user for the following inputs:
o weight (float): The weight of the order in kilograms. The user should enter a numeric
value.
o destination (string): Either 'Domestic' or 'International'. The input will be case-insensitive.
o is_priority (string): 'Yes'; or 'No'; to indicate if it's a priority shipment. The input will be
case-insensitive.
The program should continue to ask for new inputs until the user types 'exit'; when prompted to
continue.

Output:
o For each set of inputs, the program will display the total_shipping_cost (float), rounded
to two decimal places.
o It should also provide clear prompts and handle invalid inputs gracefully (e.g., non-
numeric weight, invalid destination, invalid priority choice).


NOTE: 
THIS PROGRAM DOES NOT USES FUNCTION AS OF THE MOMENT SINCE FUNCTIONS ARE NOT DISCUSSED YET.
THIS IS A BASIC IMPLEMENTATION OF THE ABOVE PROBLEM.
"""



#Charges
PRIORITY_SURCHARGE = 0.2
DESTINATION_SURCHARGE = 7.50
cargo_weight_cost = 0
subtotal = 0
total_cost = 0
subtotal_added_fee = 0

valid_input = False


while True:
    
    print("\nWelcome to the Shipping Calculator!")
    
    cargo_weight = input("Enter weight of the cargo: ")
    
    #Cargo Weight
    if cargo_weight.lower() == "exit":
        break
    elif cargo_weight.isnumeric() or "." in cargo_weight.lower():
        cargo_weight = float(cargo_weight)
        valid_input = True
    else:
        print("Invalid Input")


    if valid_input:
        
        #Destination
        destination = input("Choose destination:\
                        \n•Domestic"\
                       "\n•International\n= ").lower()
        
        if destination == "exit":
            break
        elif destination == "domestic" or destination == "international":
            valid_input = True
        else: 
            print("Invalid input")
            valid_input = False
        
        #Priority Shipping
        if valid_input:
            priority_shipping = input("Mark as Priority?:\
                        \n•Yes"\
                       "\n•No\n= ").lower()
        
            if priority_shipping.lower() == "exit":
                break
            if priority_shipping == "no" or priority_shipping == "yes":
                valid_input = True
            else: 
                print("Invalid input")
                valid_input = False
            
   
    if valid_input: 
        #Cargo weight calculation
        if cargo_weight > 10.00:
            cargo_weight_cost = 150.00
        elif cargo_weight <= 10 and cargo_weight >= 5.01:
            cargo_weight_cost = 100.00
        else:
            cargo_weight_cost = 50.00

            
        #Destination calculation    
        if destination == "international":
            subtotal = cargo_weight_cost + DESTINATION_SURCHARGE
        else:
            subtotal = cargo_weight_cost
                    
        #Priority Shipping
        if priority_shipping == "yes":
            subtotal_added_fee = subtotal * PRIORITY_SURCHARGE
            total_cost = subtotal_added_fee + subtotal
        else:
            total_cost = subtotal
        
        
        #Print Summary
        print("")
        print("="*30)
        print("{:^30s}".format("DETAILS"))
        print("="*30)
        print("Entered Weight: {:.2f}".format(cargo_weight))
        print("Destination: {}".format(destination))
        print("Priority Shipping: {}".format(priority_shipping))
        
        print("-"*30)
        print("{:^30s}".format("COMPUTATION"))
        print("-"*30)
        print("Base Cost: {:.2f}".format(cargo_weight_cost))
        print("Destination Surcharge: {:.2f}".format(DESTINATION_SURCHARGE if destination == "international" else 0))
        print("Priority Surcharge: {:.2f}".format(subtotal_added_fee))
        print("Total Shipping Cost: {:.2f}".format(total_cost))
        print("="*30)
        print("")
        
        new_transaction = input("Do you want to make another transaction? [Yes/No]: ").lower()
        
        if new_transaction == "no":
            break
        else:
            valid_input = False
            cargo_weight_cost = 0
            subtotal = 0
            total_cost = 0
            print("\n")
            continue
    
            
            
print("\nThank you for using the Shipping Calculator!")    
        
    