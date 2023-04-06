import youtube_dl

with open("urls.txt") as file_in:
    lines = []
    for line in file_in:
        lines.append(line)
        print(line)
