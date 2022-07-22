# jabber = open('jabberwocky.txt', 'r')
#
# for line in jabber:
#     print(line.rstrip())
#     # print(len(line))
#
# jabber.close()

# using with is preferred because it will automatically close the file.
# with open('jabberwocky.txt', 'r') as jabber:
#     # for line in jabber:
#     #     print(line.rstrip())
#     lines = jabber.readlines()
#
# print(lines)
# print(lines[-1:])
# for line in reversed(lines):
#     print(line, end='')

# with open('jabberwocky.txt', 'r') as jabber:
#     text = jabber.read()
#
# print(text)

with open('jabberwocky.txt', 'r') as jabber:
    while True:
        line = jabber.readline().rstrip()
        print(line)
        if 'jubjub' in line.casefold():
            break

print('*' * 80)
with open('jabberwocky.txt', 'r') as jabber:
    for line in jabber:
        print(line.rstrip())
        if 'jubjub' in line.casefold():
            break