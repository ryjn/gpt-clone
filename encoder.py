def get_text():
    """
    Get sample text from user
    """
    text = input("Enter some text: ")
    
    return text


def utf8_encoder(s: str):
    """
    Given a string, encode using UTF-8 standard

    Params:
        s: string

    Returns:
        enc_s: list - encoded bytes of s
    """
    tokens = s.encode("utf-8")  # raw bytes
    tokens = list(map(int, tokens))

    return tokens


def byte_pairing(bytes: list):
    """
    Given a list of integers (representing bytes), get count of every pair
    """
    counts = {}
    for pair in zip(bytes, bytes[1:]):
        counts[pair] = counts.get(pair, 0) + 1

    return counts


def max_pair(counts: dict):
    """
    Given dictionary of counts of pairs, return pair with highest count

    Params:
        counts: dict - dictionary with byte pairs and their counts

    Returns:
        top_pair: tuple - highest count pair
    """
    top_pair = max(counts, key=counts.get)

    return top_pair


def new_tokens(tokens, top_pair, new_token):
    """
    Given a list of integers (representing bytes), replace consecutive occurences of top_pair with new token (new_token)

    Params:
        tokens: list - list of integers (representing bytes)
        top_pair: tuple - top_pair of bytes with highest count
        new_token: int - new token

    Returns:
        
    """
    new_ids = []
    i = 0
    while i < len(tokens):
        if i < len(tokens) - 1 and tokens[i] == top_pair[0] and tokens[i + 1] == top_pair[1]:
            new_ids.append(new_token)
            i += 2
        else:
            new_ids.append(tokens[i])
            i += 1

    return new_ids


def compress_tokens(vocab_size):
    """
    """
    text = get_text()
    tokens = utf8_encoder(text)
    
    num_merges = vocab_size - 256   # 256 bytes, anything over are new tokens
    merges = {}
    for i in range(num_merges):
        counts = byte_pairing(tokens)
        top_pair = max_pair(counts)
        upd_tokens = new_tokens(tokens, top_pair, 256 + i)
        tokens = upd_tokens

    return tokens


if __name__ == "__main__":
#    # Get text
#    text = get_text()
#    print(text)
#
#    # UTF-8 Encoding
#    tokens = utf8_encoder(text)
#    print(tokens)
#    
#    # Byte Pairing
#    counts = byte_pairing(tokens)
#    print(counts)
#    
#    # Highest count pair
#    top_pair = max_pair(counts)
#    print(top_pair)
#
    # Replace pair with new token
    final_tokens = compress_tokens(276)
    print(f"final length: {len(final_tokens)}")
