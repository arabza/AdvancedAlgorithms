# Aracelli Melissa Boza Zabarburú - A01662934
# 17/09/24

# Calculate the Z array that gives the length of matching substrings
def getZarr(string):
    n = len(string)
    z = [0] * n  # Z array of length n
    l, r, k = 0, 0, 0  
    for i in range(1, n):
        if i > r:
            l, r = i, i
            while r < n and string[r - l] == string[r]:
                r += 1
            z[i] = r - l  # Length of the substring
            r -= 1
        else:
            k = i - l
            if z[k] < r - i + 1:
                z[i] = z[k]
            else:
                l = i
                while r < n and string[r - l] == string[r]:
                    r += 1
                z[i] = r - l
                r -= 1
    return z

# Removing commas and spaces
def load_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
        # Creating a continuous string
        clean_data = data.replace(',', '').replace(' ', '').strip()
        return clean_data

# Function that calculates Z values and returns array
def calculate_z_from_file(file_path):
    text = load_file(file_path)  
    z_values = getZarr(text)  
    return z_values

if __name__ == "__main__":
    file_paths = ['Z_function-Test01.txt', 'Z_function-Test02.txt', 'Z_function-Test03.txt']

    # Looping through each file path and calculating Z values
    for file_path in file_paths:
        z_array = calculate_z_from_file(file_path)
        print(f"The z-function array for {file_path} is:", z_array)
