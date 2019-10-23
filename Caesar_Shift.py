def caesar_cipher(text, shift):
  characters = [char for char in text]
  return ''.join(list(map(lambda character: 
    ' ' if ord(character) == 32 else chr((ord(character) + shift - 97) % 26 + 97),
    characters)))
