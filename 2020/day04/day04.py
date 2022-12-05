import re

with open('input') as f:
    passports_str = f.read()

passports = passports_str.split('\n\n')

n_valid_passports_pt1 = 0
n_valid_passports_pt2 = 0

for passport in passports:
    passport_valid = True
    for field in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]:
        passport_valid = passport_valid and (passport.rfind(field) > -1)
    
    if passport_valid:
        n_valid_passports_pt1 = n_valid_passports_pt1 + 1

        # Part 2: check values
        fields = passport.split()
        passport_valid_pt2 = True
        for field in fields:
            field_id = field[:3]
            field_value = field[4:]

            if field_id == "byr":
                v = int(field_value)
                if not 1920 <= v <= 2002 :
                    passport_valid_pt2 = False

            elif field_id == "iyr":
                v = int(field_value)
                if not 2010 <= v <= 2020 :
                    passport_valid_pt2 = False

            elif field_id == "eyr":
                v = int(field_value)
                if not 2020 <= v <= 2030 :
                    passport_valid_pt2 = False

            elif field_id == "hgt":
                if field_value.rfind("cm") > -1:
                    v = int(field_value[:-2])
                    if not 150 <= v <= 193 :
                        passport_valid_pt2 = False

                elif field_value.rfind("in") > -1:
                    v = int(field_value[:-2])
                    if not 59 <= v <= 76 :
                        passport_valid_pt2 = False

                else:
                    passport_valid_pt2 = False

            elif field_id == "hcl":
                if field_value[0] == "#":
                    if len(re.findall("[0-9a-f]+", field_value)[0]) != 6:
                        passport_valid_pt2 = False
    
                else:
                    passport_valid_pt2 = False

            elif field_id == "ecl":
                if field_value not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                    passport_valid_pt2 = False

            elif field_id == "pid":
                if len(field_value) != 9 or len(re.findall("[0-9]+", field_value)[0]) != 9:
                    passport_valid_pt2 = False

        if passport_valid_pt2:
            n_valid_passports_pt2 = n_valid_passports_pt2 + 1

print("Part 1: {} valid passports".format(n_valid_passports_pt1))
print("Part 2: {} valid passports".format(n_valid_passports_pt2))
