import tokenize


def remove_white_space(ifile):
    try:
        file1 = open(ifile, "r")
        for line in file1:
            line = line.strip()
            line = line.replace(" ", "")
            if line:
                print(line)
        updated_file = file1
        file1.close()
        return updated_file
    except FileNotFoundError:
        print("File was not found")


def tokenize_code():
