def flames_game(name1, name2):
   
    name1 = name1.replace(" ", "").lower()
    name2 = name2.replace(" ", "").lower()

    # Remove common characters
    for char in name1:
        if char in name2:
            name1 = name1.replace(char, '', 1)
            name2 = name2.replace(char, '', 1)

    # Calculate the remaining characters
    count = len(name1) + len(name2)

    # Define the FLAMES result categories
    flames = ['F', 'L', 'A', 'M', 'E', 'S']
    
    # Determine the result based on the count
    while len(flames) > 1:
        split_index = (count % len(flames)) - 1
        if split_index >= 0:
            flames = flames[split_index + 1:] + flames[:split_index]
        else:
            flames = flames[:len(flames) - 1]

    # Define the relationship based on the final letter
    relationship = {
        'F': "Friends",
        'L': "Lovers",
        'A': "Affectionate",
        'M': "Marriage",
        'E': "Enemies",
        'S': "Siblings"
    }

    return relationship[flames[0]]

# Example usage
name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")

result = flames_game(name1, name2)
print(f"The relationship between {name1} and {name2} is: {result}")