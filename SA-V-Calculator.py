#Surface Area and Volume calculator

#Surface area and volume calculator for most solids. Functions are grouped as this eg. C would stand for cube, and SA would stand for Surface Area, so the grouping name would be CSA.

#Surface Area Functions

#CSA
def CSA(x):
    return 6 * (x * x)

#RPSA
def RPSA(x, y, z):
    return ((x * y) + (x * z) + (y * z)) * 2

#SSA
def SSA(x):
    return 4 * ((x * x) * 3.14159)

#COSA (with slant)
def COSA1(x, y):
    return (3.14159 * (x * y)) + ((x * x) * 3.14159)

#COSA (whitout slant but with height)
def COSA2(x, y):

    import math

    return (3.14159 * x) * (x + (math.sqrt((x * x) + (y * y))))

#SPSA (with slant)
def SPSA1(x, y):
    return (x * x) + ((x * y) * 2)

#SPSA (without slant)
def SPSA2(x, y):

    import math

    return (x * x) + (2 * x) * (math.sqrt(((x * x) / 4) + (y * y)))

#CYSA
def CYSA(x, y):
    return (2 * 3.14159 * x * y) + (2 * ((x * x) * 3.14159))

#Volume Functions

#CV
def CV(x):
    return x * x * x

#RPV
def RPV(x, y, z):
    return x * y * z

#SV
def SV(x):
    return (x * x * x) * 3.14159 * (4 / 3)

#COV
def COV(x, y):
    return (3.14159 * (x * x)) * (y / 3)

#SPV
def SPV(x, y):
    return (x * x) * (y / 3)

#CYV
def CYV(x, y):
    return (3.14159 * (x * x)) * y

#User inputs

#Select Surface Area or volume

print("Would you like to calculate Surface Area or Volume?")
print("1. Surface Area")
print("2. Volume")

while True:
    choice = input("Enter your choice (1/2): ")

    if choice in ('1', '2'):

        #Selecting solids for surface area

        if choice == '1':
            print("Select the solid you want")
            print("1. Cube")
            print("2. Rectangular Prism")
            print("3. Sphere")
            print("4. Cone (with slant)")
            print("5. Cone (without slant)")
            print("6. Square Pyramid (with slant)")
            print("7. Square Pyramid (without slant)")
            print("8. Cylinder")

            while True:
                choice = input("Enter your choice (1/2/3/4/5/6/7/8): ")

                #outputs for surface area

                if choice == '1':
                    csl = float(input("Enter the cube's side length: "))
                    print("Surface area of your cube is", CSA(csl))

                elif choice == '2':
                    rpl = float(input("Enter your rectangular prism's length: "))
                    rpw = float(input("Enter your rectangular prism's width: "))
                    rph = float(input("Enter your rectangular prism's height: "))
                    print("Surface area of your recangular prism is", RPSA(rpl, rpw, rph))

                elif choice == '3':
                    sr = float(input("Enter your sphere's radius: "))
                    print("Surface area of your sphere is", SSA(sr))

                elif choice == '4':
                    cor = float(input("Enter your cone's radius: "))
                    cos = float(input("Enter your cone's slant: "))
                    print("Surface area of your cone is", COSA1(cor, cos))

                elif choice == '5':
                    cor = float(input("Enter your cone's radius: "))
                    coh = float(input("Enter your cone's height: "))
                    print("Surface area of your cone is", COSA2(cor, coh))

                elif choice == '6':
                    spbl = float(input("Enter your square pyramid's base length: "))
                    sps = float(input("Enter your square pyramid's slant: "))
                    print("Surface area of your square pyramid is", SPSA1(spbl, sps))

                elif choice == '7':
                    spbl = float(input("Enter your square pyramid's base length: "))
                    sph = float(input("Enter your square pyramid's height: "))
                    print("Surface area of your square pyramid is", SPSA2(spbl, sph))

                elif choice == '8':
                    cyr = float(input("Enter your cylinder's radius: "))
                    cyh = float(input("Enter your cylinder's height: "))
                    print("Surface area of your cylinder is", CYSA(cyr, cyh))
                break

        #Selecting solids for volume

        elif choice == '2':
            print("Select the solid you want")
            print("1. Cube")
            print("2. Rectangular Prism")
            print("3. Sphere")
            print("4. Cone")
            print("5. Square pyramid")
            print("6. Cylinder")

            while True:
                choice = input("Enter your choice (1/2/3/4/5/6): ")

            #outputs for volume

                if choice == '1':
                    csl = float(input("Enter the cube's side length: "))
                    print("Volume of your cube is", CV(csl))

                elif choice == '2':
                    rpl = float(input("Enter your rectangular prism's length: "))
                    rpw = float(input("Enter your rectangular prism's width: "))
                    rph = float(input("Enter your rectangular prism's height: "))
                    print("Volume of your recangular prism is", RPV(rpl, rpw, rph))

                elif choice == '3':
                    sr = float(input("Enter your sphere's radius: "))
                    print("Volume of your sphere is", SV(sr))

                elif choice == '4':
                    cor = float(input("Enter your cone's radius: "))
                    coh = float(input("Enter your cone's height: "))
                    print("Volume of your cone is", COV(cor, coh))

                elif choice == '5':
                    spbl = float(input("Enter your square pyramid's base length: "))
                    sph = float(input("Enter your square pyramid's height: "))
                    print("Volume of your square pyramid is", SPV(spbl, sph))

                elif choice == '6':
                    cyr = float(input("Enter your cylinder's radius: "))
                    cyh = float(input("Enter your cylinder's height: "))
                    print("Volume of your cylinder is", CYV(cyr, cyh))
                break
