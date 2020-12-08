f = open("input", "r")
maxID = 0
rows = []
columns = []
for line in f.readlines():
    row = 0
    column = 0
    start = 127
    first = 0
    last = start
    # for i in line.split():
        # i is current line
    print("current line", line[:-1], "splitting", line[:7], line[-4:-1], end=' | ')
    for c in line[:7]:
        print(c, end='')
        if (c == 'F'):
            last = (last - first) // 2 + first
        elif (c == 'B'):
            # print("bs first", first, "last", last)
            first = ((last + 1) - first) // 2 + first
            # print("new first", first)
        # print("first:", first, "last:", last)
    print()
    row = first
    # print("row", row)
    # print("trying to add row", row)
    
    first = 0
    last = 7
    for c in line[-4:-1]:
        if (c == 'L'):
            last = (last - first) // 2 + first
        elif (c == 'R'):
            first = ((last + 1) - first) // 2 + first
        # print("first:", first, "last:", last)
    column = last
    # print("column", column)
    # print("trying to add column", column)
    # print("appending ",row,column)
    # if row not in rows:
    rows.append(row)
    # if column not in columns:
    columns.append(column)
    # print("row:", row)
    # print("column:", column)
    # print("line", line[:-1], "seatID:", row * 8 + column, "row", row, "column", column)
    if (row * 8 + column) > maxID:
        maxID = row * 8 + column
# rows.sort()
# columns.sort()
print("rows:", rows, len(rows))
print("columns:", columns, len(columns))
print("max:", maxID)
count = 0
known = [None] * len(rows)
cols = [None] * len(rows)
for i in rows:
    j = columns[count]
    print("row", i, "column", j)
    if i not in known:
        known.append(i)
        if cols[int(i)] == None:
            cols[int(i)] = []
        cols[int(i)].append(j)
    count += 1
print("known",known)
print("cols",cols)
# prev = 0
# count = 0
# for i in rows:
#     if prev == 0:
#         prev = i
#     # print("prev", prev)
#     # print("current", i)
#     if prev != i:
#         if count != 8:
#             print("stopped at", count, "prev", prev, "i", i)
#         prev = i
#         count = 0
#     count += 1
# for i in range(1,128):
#     for j in range(1,8):
#         print(i, j)
# The best algorithm: Brute Force
# 66 * 8 + 6 INCORRECT
# 65 * 8 + 6 = 526 INCORRECT
# 65 * 8 + 7 = 527 INCORRECT
# 65 * 8 + 5 = 525 INCORRECT
# 65 * 8 + 4 = 524 CORRECT
# 65 * 8 + 3 = 523 INCORRECT
# 65 * 8 + 2 = 522 ?
# 65 * 8 + 1 = 521 ?
# 65 * 8 + 0 = 520 ?