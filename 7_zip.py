import re
import zipfile


def crawl(nothing_rep, nothing, f, zip_file):
    comments = []
    while True:
        try:
            file_source = zip_file.read(f % nothing)
            nothing = re.search(nothing_rep, file_source).group(1)
            print (nothing)
        except:
            # print(zip_file.read(f % nothing))
            break
        comments.append(zip_file.getinfo(f % nothing).comment)

    print("".join(comments))

if __name__ == '__main__':
    zip_file = zipfile.ZipFile("Data/channel.zip")
    f = "%s.txt"
    nothing = "90052"
    nothing_rep = "Next nothing is (\d+)"
    crawl(nothing_rep, nothing, f, zip_file)
