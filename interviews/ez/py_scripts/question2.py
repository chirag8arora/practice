# coding=utf-8
def main():
    sentence = raw_input('type any sentence: ')
    missing = []
    counter = [0] * 26
    for i in sentence:
        charCode = ord(i)
        if charCode >= 97 and charCode <= 122:
            counter[charCode - 97] += 1
        elif charCode >= 65 and charCode <= 90:
            counter[charCode - 65] += 1

    for k, v in enumerate(counter):
        if v == 0:
            missing.append(chr(k + 97))
    return "".join(missing)

if __name__ == '__main__':
    while True:
        missing = main()
        print missing if missing else "This sentence contains every letter"
