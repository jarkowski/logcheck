# ToDo:  Script graps logs, moves, unzips and cat them
# ToDo:  Run report on login automatically


def search(filename, grepsting, datestart, dateend, leftsplit, rightsplit):
    with open(filename) as f:
        for line in f:
            if grepsting in line:
                datecode = line[datestart:dateend]
                split1 = line.split(leftsplit)
                split2 = split1[1]
                split3 = split2.split(rightsplit)
                split4 = split3[0]
                print(f"{datecode} UTC - user on session: {split4}")


if __name__ == "__main__":
    search("log.log", "Electing", 7, 23, "ChatMember[", "@conference.meeting")
