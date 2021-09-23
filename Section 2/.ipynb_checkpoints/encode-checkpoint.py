from morse import EnglishMessage

message = EnglishMessage("SOS We have hit an iceberg and need help quickly")

print(f"Incoming message: {message.message}")
print(f"   Morse encoded: {message.encode()}")