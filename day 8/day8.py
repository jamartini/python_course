import day8_art
print(day8_art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
  
def caesar(text, shift, direction):
  text = [*text]
  if shift > len(alphabet):
    shift %= len(alphabet)
  if direction == "encode":
    for i in range(len(text)):
      if alphabet.count(text[i]):
        text[i] = alphabet[alphabet.index(text[i]) + shift]
      else:
        text[i] = text[i]  
    text = ''.join(text)
    print(f"The encoded text is {text}")
  elif direction == "decode":
    for i in range(len(text)):
      if alphabet.count(text[i]):
        text[i] = alphabet[alphabet.index(text[i]) - shift]
      else:
        text[i] = text[i]
    text = ''.join(text)
    print(f"The decoded text is {text}")
  start_again = input("Do you want to start again? \n")
  if start_again == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)

caesar(text, shift, direction)