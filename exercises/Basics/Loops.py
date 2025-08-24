for i in range(6):
    print("Hello", i)


count = 0    
while count < 5:
    print("count is", count)
    count += 1

jasper = ["Jasper", "is", "a", "poes"]
for i in jasper:
    print(i)
    
jasper = 1
while jasper < 5:
    print(jasper)
    jasper += 1
print("Jasper is a tottiekop")

for jasper in range(1, 21):
    if jasper % 3 == 0 and jasper % 5 == 0:
        print("Jasper is a tottiekop")
    elif jasper % 3 == 0:
        print("tottie")
    elif jasper % 5 == 0:    
        print("kop")
    else:
        print(jasper)
        

def print_number_pattern(rows):
    for i in range(1, rows + 1):
        for j in range(i):
            print(i, end=" ")
        print()
        
print_number_pattern(50)
