with open('input6.txt', 'r') as file:
    lines = file.readlines()
x = int(lines[0].strip())
results = []

for i in range(1, x + 1):
    name, years, months = lines[i].split()
    years = int(years)
    months = int(months)
    total_months = 25 * 12 
    current_months = years * 12 + months
    remaining_months = total_months - current_months
    num_hours = remaining_months 
    results.append(f"{name} {num_hours}")

for i in results:
    print(i)


    