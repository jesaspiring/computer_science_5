#Charges
PRIORITY_SURCHARGE = 0.2
DESTINATION_SURCHARGE = 7.50
cargo_weight_cost = 0
subtotal = 0
total_cost = 0

new_transaction = ""
priority_shipping = ""
destination = ""
cargo_weight = ""
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
            total_cost = (subtotal * PRIORITY_SURCHARGE) + subtotal
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
        print("{:^30s}".format("SUMMARY"))
        print("-"*30)
        print("Base Cost: {:.2f}".format(cargo_weight_cost))
        print("Destination Surcharge: {:.2f}".format(DESTINATION_SURCHARGE if destination == "international" else 0))
        print("Priority Surcharge: {:.2f}".format(PRIORITY_SURCHARGE*subtotal if priority_shipping == "yes" else 0))
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
    
            
            
print("Thank you for using the Shipping Calculator!")    
        
    