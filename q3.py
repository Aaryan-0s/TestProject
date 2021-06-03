
K = int(input("write the no of apples: "))
N = int(input("write the no of students: "))

eachgets = (K//N)
remaining = (K%N)
print(f"no of apples each student gets: {eachgets}")
print(f"no of apples remaining in the basket: {remaining}")