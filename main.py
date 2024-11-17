num_files = int(input("10 "))


for i in range(1, num_files + 1):
    filename = f"file_{i}.txt"
    with open(filename, 'w') as f:
        f.write(f"{i}")
    print(f"{filename}")