from encoder import compress_tokens


def decode(tokens: list):
    """
    Given a list of tokens as a list of integers, decode and return string
    """
    vocab = {idx: bytes([idx]) for idx in range(256)}
    for (p0, p1), idx in tokens.items():
        vocab[idx] = vocab[p0] + vocab[p1]

    return vocab


if __name__ == "__main__":
    tokens = compress_tokens(276)
    print(tokens)
    vocab = decode(tokens)
    print(vocab)
