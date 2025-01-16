with open('input14.txt', 'r') as file:
    input_line = file.readline().strip()
    checksum_line = file.readline().strip()

calculated_checksum = sum(map(float, input_line.split()))

print(input_line)

if '=' in checksum_line:
    expected_checksum = float(checksum_line.split('=')[1])
else:
    expected_checksum = 0.0

if calculated_checksum == expected_checksum: 
    print("CHECKED")
else:
    print(f"BADCHECK:{calculated_checksum}")
    print(f"Calculated Checksum: {calculated_checksum}")

