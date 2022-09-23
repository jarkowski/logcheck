# ToDo:  Script graps logs, moves, unzips and cat them
# ToDo:  Run report on login automatically
from subprocess import call


def prepare_logs(logfile_source_path):
    call(f"rm -f /root/logcheck/result.csv", shell=True)
    call(f"rm -f /root/logcheck/*.gz", shell=True)
    call(f"rm -f /root/logcheck/jicofo.log*", shell=True)
    call(f"rm -f /root/logcheck/log.log", shell=True)
    call(f"cp {logfile_source_path}/jicofo.log* /root/logcheck", shell=True)
    call(f"gzip -d /root/logcheck/*.gz", shell=True)
    call(f"cat /root/logcheck/jicofo.log* > log.log", shell=True)


def parse_log(filename, grepsting, datestart, dateend, leftsplit, rightsplit):
    with open(filename) as f:
        print(f"=================================================")
        for line in f:
            if grepsting in line:
                datecode = line[datestart:dateend]
                datecode_onlydate = line[datestart : dateend - 6]
                split1 = line.split(leftsplit)
                split2 = split1[1]
                split3 = split2.split(rightsplit)
                session_name = split3[0]
                print(f"{datecode} UTC - user on session: {session_name}")

                with open("result.csv", "a+") as result_file:
                    result_file.seek(0)
                    data = result_file.read(10)
                    if len(data) > 0:
                        result_file.write("\n")
                    result_file.write(f"{datecode_onlydate};{datecode};{session_name}")
        print(f"=================================================")


if __name__ == "__main__":
    prepare_logs("/var/log/jitsi")
    parse_log("log.log", "Electing", 7, 23, "ChatMember[", "@conference.meeting")
