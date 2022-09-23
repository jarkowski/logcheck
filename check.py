# ToDo:  Script graps logs, moves, unzips and cat them
# ToDo:  Run report on login automatically


def search(filename, text):
    with open(filename) as f:
        for line in f:
            if text in line:
                print(line[7:17])
                split1 = line.split("ChatMember[")
                split2 = split1[1]
                split3 = split2.split("@conference.meeting")
                split4 = split3[0]
                print(split4)


if __name__ == "__main__":
    search("log.log", "Electing")
