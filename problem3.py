with open('input3.txt', 'r') as file:
  for line in file:
      x = int(line.strip())
      if x == -1:
          break
      if x == 1:
          print(f"You, {x} minute ago.")
      elif x == 0 or x > 1:
          print(f"You, {x} minutes ago.")


