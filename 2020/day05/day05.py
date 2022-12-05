# row: F=0, B=1
# seat: L=0, R=1
# seat ID = 8*row + seat

with open("input") as f:
    seat_strs = f.readlines()

highest_seat_id = 0
all_seat_ids = []

for seat_str in seat_strs:
    seat_id_str = seat_str.strip().replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1")
    
    seat_id = int(seat_id_str, base=2)

    all_seat_ids.append(seat_id)
    
    if seat_id > highest_seat_id :
        highest_seat_id = seat_id

print("Part 1: highest seat ID is {}".format(highest_seat_id))

# Part2: find my seat
all_seat_ids.sort()

for idx, elem in enumerate(all_seat_ids):
    if all_seat_ids[idx+1] > elem + 1:
        print("Part 2: my seat ID is {}".format(elem + 1))
        break
