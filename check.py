def search(filename, text):
    with open(filename) as f:
        for line in f:
            if text in line:
                print(line)


if __name__ == "__main__":
    search("jicofo.log", "Electing")
