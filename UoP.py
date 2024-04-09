# Define the function to read the dictionary from a file and invert it
def invert_dictionary(input_file, output_file):
    try:
        # Open the input file in read mode
        with open(input_file, 'r') as file:
            # Read the content of the file
            content = file.read()
            # Evaluate the content as a dictionary
            original_dict = eval(content)
            
            # Create an empty dictionary to store the inverted dictionary
            inverted_dict = {}
            
            # Iterate through the items in the original dictionary
            for key, value in original_dict.items():
                # Split the value by comma if it contains multiple values
                values = [v.strip() for v in value.split(',')]
                # Iterate through each value
                for v in values:
                    # Check if the value exists in the inverted dictionary
                    if v in inverted_dict:
                        # If the value exists, append the key to the list of keys for that value
                        inverted_dict[v].append(key)
                    else:
                        # If the value does not exist, create a new entry with the value as key and the key as the first item in the list
                        inverted_dict[v] = [key]
            
            # Open the output file in write mode
            with open(output_file, 'w') as output:
                # Write the inverted dictionary to the output file
                output.write("{\n")
                for key, values in inverted_dict.items():
                    output.write(f'  {key}: {", ".join(values)}\n')
                output.write("}\n")
            print("Inverted dictionary has been written to", output_file)
    except FileNotFoundError:
        print("File not found or does not exist.")
    except Exception as e:
        print("An error occurred:", e)

# Input and output file paths
input_file = r"C:\Users\PC\Desktop\remi\sample.txt"
output_file = "inverted_dict.txt"

# Call the function to invert the dictionary
invert_dictionary(input_file, output_file)
