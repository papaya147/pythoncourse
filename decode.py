from morse import MorseMessage

morse_message = MorseMessage("... . -.-. .-. . - / -- . ... ... .- --. .")

print(f"Morse message:{morse_message.message}")
print(f"Morse decoded:{morse_message.decode()}")