import codecs


def decode_solidity_abi(hex_data, types):
    # Remove the '0x' prefix if it exists
    if hex_data.startswith("0x"):
        hex_data = hex_data[2:]

    # Remove leading zeros for clarity
    stripped_hex = hex_data.lstrip("0")

    # Initialize output dictionary
    decoded_values = {}

    # Each Uint256 will consume 64 characters from the hex string (32 bytes per Uint256)
    offset = 0
    for i, type_name in enumerate(types):
        if type_name == "Uint256":
            # Extract 64 characters (32 bytes) for each Uint256
            byte_length = 64
            value_hex = stripped_hex[offset : offset + byte_length].lstrip("0")
            # Ensure leading zero if the value is non-zero
            if value_hex == "":
                value_hex = "0"
            else:
                value_hex = "0x" + value_hex
            decoded_values[i] = {"_hex": value_hex}
            offset += byte_length

    return decoded_values


# Test the function
hex_data = "0x00000000000000000000000000000000000000000000005150ae84a8cdf0000000000000000000000000000000000000000000000000000002f94bb8c870db6d"
types = ["Uint256", "Uint256"]
decoded_output = decode_solidity_abi(hex_data, types)
print(decoded_output)
