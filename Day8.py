input = """..........M..........j.............y.....O........
...B...............q......m........lGO............
....................q......2.l.GQ...O.............
.....X.......................................4....
.....................q............................
....M......P...............xl.K.............2.....
....F.........L.......C.K..............m..........
..........FM......P....jy......m..........o...r...
..X.......P.....RL..............G..x..........4...
............L..........NC.....q...................
.....C.X...............K....y..........4..........
........S...R.............j.x.....V...4...........
.....................R..x.....V..i......m.........
...........................R.V......N.......X.....
.....F.........M......N......E....................
................v................T.......F......O.
.............................N...V.......Q........
...v.....................C.....i..................
......c.....W..n.w........................E.......
3...................c.....................Q..6....
...........h......................j...............
.......n.0......h.................E..............2
.v.............7.......120.....c..................
......n.0............w...........D.t.........E...r
....8..3......0.w.hP....z...D..T...............r..
.................f........T........G......eQ......
......f.n.....7..p................................
.....Y..7.......f......I......D......K............
............Uf....T..W.....D..r...i...............
......I...............................Z...........
....5....B.......b..............s..............Z..
..........d...W..Uwh.............c..........i.....
..I.3..Y......................e...................
.....p.b..........k......7........................
p...........k....I..b..........s..................
.....k.......o...........W........................
.A..Y..........U.................a........6.......
..A...Y.p...................................6.....
B......k..........................Z............u..
...3.....................s..............a.........
......A.........................g.....a...........
.......A....8...b.U......H....sS..................
.........................S1.............t.........
.....................9z..e.....5..1.g.u...........
.......................z....d....g....H.J....o.6..
........B................d.....u....9.J.H.........
.8........S.................u9.............J.....H
.....................Z5.............t1...........a
.....................e..v...................o..t..
.....8...............L.....z.............J........""".splitlines()

coords = []

for row in input:
    coords.append([x for x in row])

print(f"The dimensions of the map are {len(coords)} deep by {len(coords[0])} wide")

antinode_flags = [["N" for _ in range(len(coords[0]))] for _ in range(len(coords))]


def node_check(i, j, symbol):
    symb_positions = [(i, j)
                      for i, row in enumerate(coords)
                      for j, element in enumerate(row)
                      if element == symbol]
    for pos in symb_positions:
        if pos != (i, j):
            if 0 <= (pos[0] + pos[0] - i) < len(coords) and 0 <= (pos[1] + pos[1] - j) < len(coords[0]):
                antinode_flags[pos[0] + pos[0] - i][pos[1] + pos[1] - j] = "Y"
    return



for i in range(len(coords)):
    for j in range(len(coords[0])):
        if coords[i][j] != ".":
            node_check(i, j, coords[i][j])

node_count = 0

for row in antinode_flags:
    for element in row:
        if element == "Y":
            node_count += 1

print(f"The number of nodes in Part 1 is {node_count}")

# Part 2

antinode_flags = [["N" for _ in range(len(coords[0]))] for _ in range(len(coords))]


def node_check2(i, j, symbol):
    symb_positions = [(i, j)
                      for i, row in enumerate(coords)
                      for j, element in enumerate(row)
                      if element == symbol]
    for pos in symb_positions:
        if pos != (i, j):
            vert_vector = pos[0] - i
            horiz_vector = pos[1] - j
            reduced_vert_vector = vert_vector
            reduced_horiz_vector = horiz_vector
            for num in range(1, max(vert_vector, horiz_vector) + 1):
                if (vert_vector / num).is_integer() and (horiz_vector / num).is_integer():
                    reduced_vert_vector = vert_vector / num
                    reduced_horiz_vector = horiz_vector / num
            node_pos_i = i
            node_pos_j = j
            while 0 <= node_pos_i < len(coords) and 0 <= node_pos_j < len(coords[0]):
                antinode_flags[int(node_pos_i)][int(node_pos_j)] = "Y"
                node_pos_i += reduced_vert_vector
                node_pos_j += reduced_horiz_vector
    return


for i in range(len(coords)):
    for j in range(len(coords[0])):
        if coords[i][j] != ".":
            node_check2(i, j, coords[i][j])

node_count = 0

for row in antinode_flags:
    for element in row:
        if element == "Y":
            node_count += 1

print(f"The number of nodes in Part 2 is {node_count}")