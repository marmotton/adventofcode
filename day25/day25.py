public_keys = [1526110, 20175123]

loop_sizes = [0, 0]

def step(val, subject):
    new_val = (val * subject) % 20201227
    return new_val

# Find loop size for [0]
val = 1
while val != public_keys[0]:
    loop_sizes[0] += 1
    val = step(val=val, subject=7)

# Compute encryption key using loop size of [0] and public key of [1]
encryption_key = 1
for _ in range(loop_sizes[0]):
    encryption_key = step(val=encryption_key, subject=public_keys[1])

print("Encryption key is {}".format(encryption_key))
