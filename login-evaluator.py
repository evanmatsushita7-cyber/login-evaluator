import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--threshold', type=int, help='The desired threshold, crossing it triggers a warning')
parser.add_argument('--file', type=open, help = ('Selects which file the user would like opened and analyzed'))
parser.add_argument('--timestamp', help = ('Alternatively displays ip and timestamp pairs, checking and warning for odd times'))
args = parser.parse_args()
ip_precursor_word = ("from")
username_precursor_word = ("for")

ip_counts = {}
ip_usernames = {}
ip_timestamp = {}
username_count = 0
text = args.file.read()
args.file.close()
def timestamp_call():
    print (ip_timestamp)

    
for line in text.splitlines():
        if "Failed password" in line:
            parts = line.split(ip_precursor_word, 1)
            result = parts[1].strip()
            uparts1 = line.split(username_precursor_word, 1)[1]
            uparts2 = uparts1.split(ip_precursor_word, 1)[0]
            usernames = uparts2.strip()
            splitline = line.split()
            timestamp = splitline[2]       
            if result in ip_timestamp:
                ip_timestamp[result].add(timestamp)
            else:
                ip_timestamp[result] ={timestamp}
            if result in ip_usernames:
                 ip_usernames[result].add(usernames)
            else:
                 ip_usernames[result] = {usernames}
            if result in ip_counts:
                ip_counts[result] = ip_counts[result] + 1
            else:
                ip_counts[result] = 1
        else:
            continue
for ip, count in ip_counts.items():
    print (ip, count)
for ip, username in ip_usernames.items():
    print (ip, username)
for ip, count in ip_counts.items():
    if count >  args.threshold:
        print (f"Excessive Login Attempts: Possible brute force from ip {ip}")
for ip, username in ip_usernames.items():
     if len(username) > args.threshold:
          print (f"Many usernames entered: Possible credential stuffing from {ip} ")