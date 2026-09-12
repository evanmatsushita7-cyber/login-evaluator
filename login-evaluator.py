import argparse
def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--threshold', type=int, help='The desired threshold, crossing it triggers a warning')
    parser.add_argument('--file', help=('Selects which file the user would like opened and analyzed'))
    parser.add_argument('--timestamp', help=('Alternatively displays ip and timestamp pairs, checking and warning for odd times'))
    return parser.parse_args()

args = parse_arguments()

ip_precursor_word = ("from")
username_precursor_word = ("for")

ip_counts = {}
ip_usernames = {}
ip_timestamp = {}

def readfiles():
    try:
        with open(args.file) as f:
            text = f.read()
        return text
    except FileNotFoundError:
        print ("Could not find that file")
        exit()

def processlines(text):
    for line in text.splitlines():
        if "for" in line and "from" in line:
            parts = line.split(ip_precursor_word, 1)
            result = parts[1].strip()
            uparts1 = line.split(username_precursor_word, 1)[1]
            uparts2 = uparts1.split(ip_precursor_word, 1)[0]
            usernames = uparts2.strip()
            splitline = line.split()
            timestamp = splitline[2]
            timestamp_hour = timestamp[:2]       
            if result in ip_timestamp:
                ip_timestamp[result].add(timestamp_hour)
            else:
                ip_timestamp[result] ={timestamp_hour}
            if "Failed password" in line:
                if result in ip_usernames:
                    ip_usernames[result].add(usernames)
                else:
                    ip_usernames[result] = {usernames}
                if result in ip_counts:
                    ip_counts[result] = ip_counts[result] + 1
                else:
                    ip_counts[result] = 1
    return ip_counts, ip_usernames, ip_timestamp        

def display_ip_counts_and_names(ip_counts, ip_usernames):
    for ip, count in ip_counts.items():
       if count >  args.threshold:
        print (f"Excessive Login Attempts: Possible brute force from ip {ip}")
    for ip, username in ip_usernames.items():
        if len(username) > args.threshold:
            print (f"Many usernames entered: Possible credential stuffing from {ip} ")
def print_odd_hour_timestamps(ip_timestamp):
    if  args.timestamp:
        for ip, times in ip_timestamp.items():
            for time in times:
                if int(time) < 5:
                    print (f"Odd hour detected from {ip}")
def main():
    text = readfiles()
    ip_counts, ip_usernames, ip_timestamp = processlines(text)
    display_ip_counts_and_names(ip_counts, ip_usernames)
    print_odd_hour_timestamps(ip_timestamp)
main()