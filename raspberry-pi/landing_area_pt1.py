# Paul Schakel
# Landing Area Part 1

def get_input(): # Takes user input of 3 sets of coordinates
    print("Enter 3 sets of coordinates: ")
    coordinates = []
    try: # Makes sure that the user is entering the correct syntax
        for i in range(3):
            inp = input(f"Enter coordinate set {i} in x,y format: ")
            coordinate = inp.split(',') # Splits the input string into its 2 numbers
            print(coordinate)
            x = float(coordinate[0])
            y = float(coordinate[1])
            coordinates.append([x, y])
        return coordinates
    except:
        print("These points are not a valid triangle. Please try again, and make sure you are using the x,y syntax!\n\n")
        return get_input()

def calculate(coordinates): # Calculates the area or a triangle from the coordinates of its vertices
    print(coordinates)
    area = 1/2*abs(coordinates[0][0] * (coordinates[1][1] - coordinates[2][1]) + coordinates[1][0] * (coordinates[2][1] - coordinates[0][1]) + coordinates[2][0] * (coordinates[0][1] - coordinates[1][1]))
    return area

while True:
    coordinates = get_input()
    area = calculate(coordinates)
    print(f"The area of the triangle with vertices ({coordinates[0][0]}, {coordinates[0][1]}), ({coordinates[1][0]}, {coordinates[1][1]}), ({coordinates[2][0]}, {coordinates[2][1]}) is {area} square km.\n\n")