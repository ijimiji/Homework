from string import ascii_lowercase


class Cipher:
    def __init__(self, keyword):
        alphabet = list(ascii_lowercase)
        for char in reversed(keyword):
            alphabet.remove(char)
            alphabet.insert(0, char)
        self.encoder = {key: char for (char, key) in zip(alphabet, ascii_lowercase)}
        uppercase_translator = {}
        for key, val in self.encoder.items():
            uppercase_translator[key.upper()] = val.upper()
        self.encoder.update(uppercase_translator)
        self.decoder = {val: key for key, val in self.encoder.items()}

    def encode(self, word: str):
        encoded_word = str()
        for char in word:
            if char in self.encoder:
                encoded_word += self.encoder[char]
            else:
                encoded_word += char

        return encoded_word

    def decode(self, word: str):
        decoded_word = str()
        for char in word:
            if char in self.encoder:
                decoded_word += self.decoder[char]
            else:
                decoded_word += char
        return decoded_word
