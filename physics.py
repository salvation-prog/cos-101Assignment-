print("WELCOME TO COS 101")
print("BHU|24|04|10|0008")
print("salvation simon")
def a():
    velocity= float(input("input velocity:"))
    time= float(input("input time:"))
    displacement=str(velocity*time)
    print(displacement)

def b():
    workdone= float(input("input workdone:"))
    time= float(input("input time:"))
    energy=str(workdone/time)
    print(energy)


def c():
    mass= float(input("input mass:"))
    volume = float(input("input volume:"))
    pressure = str(mass / volume)
    print(pressure)


def d():
    mass = float(input("mass:"))
    g= float(input(10))
    height= float(input("input height"))
    energy = str(mass*g*height)
    print(energy)


def e():
    a = float(input("input a:"))
    b = float(input("input b:"))
    division = a/b
    print(division)

def main():
    user_choice = input("choose from a - e:")

    if user_choice == "a":
        a()
    elif user_choice == "b":
        b()
    elif user_choice == "c":
        c()
    elif user_choice == "d":
        d()
    elif user_choice == "e":
        e()

if __name__ == '__main__':
      main()