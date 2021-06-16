# Begin loop asking for weight input
while True:
  try:
    # Collect input in KG
    kg_input = input("Enter weight in KG:")
    
    # Convert to float
    kg_input = float(kg_input);
    
    # Convert to LB, 1kg = 2.205LB
    lb_output = kg_input*2.205
    
    # Lets output the value in LB
    print("Weight converted to lb: ",lb_output)
    
  except ValueError:
    # Error, wasn't a valid numberic value
    print("Provide an integer value...")
    continue
