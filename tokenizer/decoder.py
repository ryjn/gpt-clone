from encoder import compress_tokens

def decode(merges):
    vocab = {idx: bytes([idx]) for idx in range(256)}
    for (p0, p1), idx in merges.items():
        vocab[idx] = vocab[p0] + vocab[p1]

    print(vocab)
    return(vocab)


if __name__ == "__main__":
    tokens, merges = compress_tokens(257)
    vocab = decode(merges)



