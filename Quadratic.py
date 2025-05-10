while True:  # Start a loop
    
        A = float(input("A: "))
        B = float(input("B: "))
        C = float(input("C: "))

        # Correcting the formula
        D = (B**2) - (4 * A * C)  # Standard quadratic discriminant formula
        if D > 0:
            print("No real solutions exist.")
        else:
            x1 = (-B + (D ** 0.5)) / (2 * A)
            x2 = (-B - (D ** 0.5)) / (2 * A)

            Test = input(f"Are these numbers right? {A}, {B}, {C} (yes/no): ").strip().lower()

            if Test == "yes":
                print(f"The solutions are: {x1} and {x2}")
                break  # Exit the loop if input is correct
            else:
                print("Let's try again.")
   
