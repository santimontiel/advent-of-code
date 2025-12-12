"""Solution for Advent of Code 2020 Day 04."""
from dataclasses import dataclass, asdict
from typing import Optional


@dataclass
class Passport:
    byr: Optional[str] = None
    iyr: Optional[str] = None
    eyr: Optional[str] = None
    hgt: Optional[str] = None
    hcl: Optional[str] = None
    ecl: Optional[str] = None
    pid: Optional[str] = None
    cid: Optional[str] = None

    def from_raw_record(record: str) -> "Passport":
        """Return a Passport object from a raw string record.
        """
        passport = Passport()
        fields = record.split(" ")
        for field in fields:
            k, v = field.split(":")
            passport.__setattr__(k, v)
        return passport
    
    def is_valid_part1(self) -> bool:
        """Check if the passport is valid for part 1.
        """
        if sum(v is not None for v in asdict(self).values()) == 8:
            return True
        if sum(v is not None for v in asdict(self).values()) == 7 and self.cid is None:
            return True
        return False
    
    def is_valid_part2(self) -> bool:
        """Check if the passport is valid for part 2.
        """
        byr = self.byr
        if byr is None or len(byr) != 4 or not 1920 <= int(byr) <= 2002:
            return False
        
        iyr = self.iyr
        if iyr is None or len(iyr) != 4 or not 2010 <= int(iyr) <= 2020:
            return False
        
        eyr = self.eyr
        if eyr is None or len(eyr) != 4 or not 2020 <= int(eyr) <= 2030:
            return False
        
        hgt = self.hgt
        if hgt is None:
            return False
        unit = hgt[-2:]
        if unit not in ["in", "cm"]:
            return False
        if unit == "cm" and not (150 <= int(hgt[:-2]) <= 193):
            return False
        if unit == "in" and not (59 <= int(hgt[:-2]) <= 76):
            return False
        
        hcl = self.hcl
        if hcl is None:
            return False
        if hcl[0] != "#" or len(hcl) != 7:
            return False
        try:
            int(hcl[1:], 16)
        except ValueError:
            return False
        
        ecl = self.ecl
        if ecl is None:
            return False
        if ecl not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            return False
        
        pid = self.pid
        if pid is None or len(pid) != 9:
            return False
        try:
            int(pid)
        except ValueError:
            return False

        return True


def parse_input(input_data: list[str]) -> list[Passport]:
    """Parse input data into a list of Passport objects.
    """
    passports: list[Passport] = []
    curr_passport = ""
    for line in input_data:
        if line == "":
            passports.append(Passport.from_raw_record(curr_passport))
            curr_passport = ""
        else:
            if len(curr_passport) != 0:
                curr_passport += " "
            curr_passport += line
    passports.append(Passport.from_raw_record(curr_passport))
    return passports


def part1(input_data: list[str]) -> int:
    passports: list[Passport] = parse_input(input_data)
    return sum(passport.is_valid_part1() for passport in passports)


def part2(input_data: list[str]) -> int:
    passports: list[Passport] = parse_input(input_data)
    return sum(passport.is_valid_part2() for passport in passports)