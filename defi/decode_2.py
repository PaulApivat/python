def varbinary_substring(data, start_index, byte_length=32):
    """
    Mimics the varbinary_substring function in DuneSQL that extracts a specific number of bytes
    from a hexadecimal string starting at a given index.

    Parameters:
    - data: Hexadecimal data string.
    - start_index: The starting index (1-based).
    - byte_length: Number of bytes to extract.

    Returns:
    - A substring of the hexadecimal data of length `byte_length * 2` characters,
      representing `byte_length` bytes.
    """
    # Remove the '0x' prefix if present
    if data.startswith("0x"):
        data = data[2:]

    # Calculate the character index for substring extraction
    # Subtract 1 because Python uses 0-based indexing
    char_index = (start_index - 1) * 2

    # Calculate the number of characters to extract (2 characters per byte)
    num_chars = byte_length * 2

    # Extract the substring representing the specified number of bytes
    extracted_hex = data[char_index : char_index + num_chars]

    # Calculate the remaining part of the data
    remaining_hex = data[char_index + num_chars :]

    # Calculate the next start index
    next_start_index = start_index + byte_length

    # explicit printing
    print("hex data to be decoded :", data, "\n")
    print("0x +", "\n")
    print("extracted hex :", extracted_hex, "\n")
    print("length of first substring :", len(extracted_hex), "\n")
    print("remaining hex: ", remaining_hex, "\n")
    print("next start index: ", next_start_index, "\n")

    # Return the result with '0x' prefix to signify hexadecimal
    return "0x" + extracted_hex


def left_trim(hex_data):
    """
    Removes all leading zero bytes from a hexadecimal string but ensures correct formatting.

    Parameters:
    - hex_data: Hexadecimal data string, prefixed with '0x'.

    Returns:
    - A hexadecimal string with leading zero bytes properly trimmed, keeping '0x' prefix.
    """
    # Remove the '0x' prefix if present
    if hex_data.startswith("0x"):
        hex_data = hex_data[2:]

    # Remove leading zeros but leave at least one zero if all characters are zeros
    trimmed_hex = hex_data.lstrip("0")
    if not trimmed_hex:  # Check if the string is empty after stripping
        trimmed_hex = "0"  # Ensure at least one zero remains if all were zeros
    elif (
        len(trimmed_hex) % 2 != 0
    ):  # Ensure hex string length is even to represent complete bytes
        trimmed_hex = "0" + trimmed_hex

    # Return the result with '0x' prefix
    return "0x" + trimmed_hex


def varbinary_to_uint256(hex_data):
    """
    Converts a hexadecimal string to a uint256 integer.

    Parameters:
    - hex_data: Trimmed hexadecimal data string prefixed with '0x'.

    Returns:
    - The decoded integer value of the hexadecimal string.
    """
    # Ensure the input is a string and remove the '0x' prefix if present
    if hex_data.startswith("0x"):
        hex_data = hex_data[2:]

    # Convert the hexadecimal string to a decimal integer
    uint256_value = int(hex_data, 16)

    return uint256_value


# Example usage
data = "0x00000000000000000000000082af49447d8a07e3bd95bd0d56f35241523fbab10000000000000000000000000000000000000000000000000000012531b3697b000000000000000000000000000000000000000000000000006a94d7d073e4f6"
first_substring = varbinary_substring(data, 1, 32)
print("first substring :", first_substring, "\n")
second_substring = varbinary_substring(data, 33, 32)
print("second substring :", second_substring, "\n")
third_substring = varbinary_substring(data, 65, 32)
print("third substring: ", third_substring, "\n")

# Test the function with given examples
test_data1 = "0x00000000000000000000000082af49447d8a07e3bd95bd0d56f35241523fbab1"
test_data2 = "0x0000000000000000000000000000000000000000000000000000012531b3697b"
test_data3 = "0x000000000000000000000000000000000000000000000000006a94d7d073e4f6"

trimmed1 = left_trim(first_substring)
trimmed2 = left_trim(second_substring)
trimmed3 = left_trim(third_substring)

print("trimmed 1:", trimmed1, "\n")
print("trimmed 2:", trimmed2, "\n")
print("trimmed 3:", trimmed3, "\n")


# Test the function with the specified examples
test_data1 = "0x012531b3697b"
test_data2 = "0x6a94d7d073e4f6"

# Decode the hexadecimal to integer
decoded_value1 = varbinary_to_uint256(trimmed2)
decoded_value2 = varbinary_to_uint256(trimmed3)

print("decoded value1 :", decoded_value1, "\n")
print("decoded value2 :", decoded_value2, "\n")
