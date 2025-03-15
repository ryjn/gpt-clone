# GPT Tokenizer
At the heart of ChatGPT, and practically all LLMs, is the tokenizer. This crucial component processes text and breaks them down into a format that is suitable for the models to understand.

It is also responsible for many of the LLMs' 'weirdness.' Output can vary depending on whether a token is for an entire word or a single character, or whether to include spaces or not. Additionally, different tokenization processes can result in excessive bloat of a model if they are too granular.

A simple solution could be to use Unicode to convert each character into an integer. However, due to the sheer volume of the number of characters. Additionally, the Unicode standard is updated routinely, and so may not provide a consistent method.

To address this, an option is encoding, such as UTF-8.

Use UTF-8 encoding but compress bytes (long text would be too stretched out) byte-pairing coding algorithm
Find most common pairing, map to a new token, compress text. Repeat until a pair only repeats once. Append new tokens, increasing vocabulary length
