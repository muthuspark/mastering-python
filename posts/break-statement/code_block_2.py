count = 0
while count < 10:
    count += 1
    if count == 5:
        print("Reached 5, breaking the loop!")
        break  # Exits the loop when count reaches 5
    print(f"Count: {count}")

print("Loop finished.")