#Неправельна версія проекту(не )

def up_down_first():
    global b, df, a, visited, route
    if a + 1 <= len(df) - 1 and (df[a + 1][b] == 1 or df[a + 1][b] == 2) and not visited[a + 1][b]:
        a += 1
        visited[a][b] = True
        route.append("down")
    elif a - 1 >= 0 and (df[a - 1][b] == 1 or df[a - 1][b] == 2) and not visited[a - 1][b]:
        a -= 1
        visited[a][b] = True
        route.append("up")
    elif b + 1 <= len(df[0]) - 1 and (df[a][b + 1] == 1 or df[a][b + 1] == 2) and not visited[a][b + 1]:
        b += 1
        visited[a][b] = True
        route.append("right")
    elif b - 1 >= 0 and (df[a][b - 1] == 1 or df[a][b - 1] == 2) and not visited[a][b - 1]:
        b -= 1
        visited[a][b] = True
        route.append("left")
    else:
        not_rout_found()


def right_left_first():
    global b, df, a, visited, route
    if b + 1 <= len(df[0]) - 1 and (df[a][b + 1] == 1 or df[a][b + 1] == 2) and not visited[a][b + 1]:
        b += 1
        visited[a][b] = True
        route.append("right")
    elif b - 1 >= 0 and (df[a][b - 1] == 1 or df[a][b - 1] == 2) and not visited[a][b - 1]:
        b -= 1
        visited[a][b] = True
        route.append("left")
    elif a + 1 <= len(df) - 1 and (df[a + 1][b] == 1 or df[a + 1][b] == 2) and not visited[a + 1][b]:
        a += 1
        visited[a][b] = True
        route.append("down")
    elif a - 1 >= 0 and (df[a - 1][b] == 1 or df[a - 1][b] == 2) and not visited[a - 1][b]:
        a -= 1
        visited[a][b] = True
        route.append("up")
    else:
        not_rout_found()


def right_first():
    global b, df, a, visited, route
    if b + 1 <= len(df[0]) - 1 and (df[a][b + 1] == 1 or df[a][b + 1] == 2) and not visited[a][b + 1]:
        b += 1
        visited[a][b] = True
        route.append("right")
    elif a + 1 <= len(df) - 1 and (df[a + 1][b] == 1 or df[a + 1][b] == 2) and not visited[a + 1][b]:
        a += 1
        visited[a][b] = True
        route.append("down")
    elif a - 1 >= 0 and (df[a - 1][b] == 1 or df[a - 1][b] == 2) and not visited[a - 1][b]:
        a -= 1
        visited[a][b] = True
        route.append("up")
    elif b - 1 >= 0 and (df[a][b - 1] == 1 or df[a][b - 1] == 2) and not visited[a][b - 1]:
        b -= 1
        visited[a][b] = True
        route.append("left")
    else:
        not_rout_found()


def left_first():
    global b, df, a, visited, route

    if b - 1 >= 0 and (df[a][b - 1] == 1 or df[a][b - 1] == 2) and not visited[a][b - 1]:
        b -= 1
        visited[a][b] = True
        route.append("left")
    elif a + 1 <= len(df) - 1 and (df[a + 1][b] == 1 or df[a + 1][b] == 2) and not visited[a + 1][b]:
        a += 1
        visited[a][b] = True
        route.append("down")
    elif a - 1 >= 0 and (df[a - 1][b] == 1 or df[a - 1][b] == 2) and not visited[a - 1][b]:
        a -= 1
        visited[a][b] = True
        route.append("up")
    elif b + 1 <= len(df[0]) - 1 and (df[a][b + 1] == 1 or df[a][b + 1] == 2) and not visited[a][b + 1]:
        b += 1
        visited[a][b] = True
        route.append("right")
    else:
        not_rout_found()


def left_up_first():
    global b, df, a, visited, route
    if a - 1 >= 0 and (df[a - 1][b] == 1 or df[a - 1][b] == 2) and not visited[a - 1][b]:
        a -= 1
        visited[a][b] = True
        route.append("up")
    elif b - 1 >= 0 and (df[a][b - 1] == 1 or df[a][b - 1] == 2) and not visited[a][b - 1]:
        b -= 1
        visited[a][b] = True
        route.append("left")
    elif b + 1 <= len(df[0]) - 1 and (df[a][b + 1] == 1 or df[a][b + 1] == 2) and not visited[a][b + 1]:
        b += 1
        visited[a][b] = True
        route.append("right")
    elif a + 1 <= len(df) - 1 and (df[a + 1][b] == 1 or df[a + 1][b] == 2) and not visited[a + 1][b]:
        a += 1
        visited[a][b] = True
        route.append("down")
    else:
        not_rout_found()


def down_first():
    global b, df, a, visited, route
    if a + 1 <= len(df) - 1 and (df[a + 1][b] == 1 or df[a + 1][b] == 2) and not visited[a + 1][b]:
        a += 1
        visited[a][b] = True
        route.append("down")
    elif b + 1 <= len(df[0]) - 1 and (df[a][b + 1] == 1 or df[a][b + 1] == 2) and not visited[a][b + 1]:
        b += 1
        visited[a][b] = True
        route.append("right")
    elif b - 1 >= 0 and (df[a][b - 1] == 1 or df[a][b - 1] == 2) and not visited[a][b - 1]:
        b -= 1
        visited[a][b] = True
        route.append("left")
    elif a - 1 >= 0 and (df[a - 1][b] == 1 or df[a - 1][b] == 2) and not visited[a - 1][b]:
        a -= 1
        visited[a][b] = True
        route.append("up")
    else:
        not_rout_found()


def up_first():
    global b, df, a, visited, route
    if a - 1 >= 0 and (df[a - 1][b] == 1 or df[a - 1][b] == 2) and not visited[a - 1][b]:
        a -= 1
        visited[a][b] = True
        route.append("up")

    elif b + 1 <= len(df[0]) - 1 and (df[a][b + 1] == 1 or df[a][b + 1] == 2) and not visited[a][b + 1]:
        b += 1
        visited[a][b] = True
        route.append("right")
    elif b - 1 >= 0 and (df[a][b - 1] == 1 or df[a][b - 1] == 2) and not visited[a][b - 1]:
        b -= 1
        visited[a][b] = True
        route.append("left")
    elif a + 1 <= len(df) - 1 and (df[a + 1][b] == 1 or df[a + 1][b] == 2) and not visited[a + 1][b]:
        a += 1
        visited[a][b] = True
        route.append("down")
    else:
        not_rout_found()


def down_left_first():
    global b, df, a, visited, route
    if a + 1 <= len(df) - 1 and (df[a + 1][b] == 1 or df[a + 1][b] == 2) and not visited[a + 1][b]:
        a += 1
        visited[a][b] = True
        route.append("down")
    elif b - 1 >= 0 and (df[a][b - 1] == 1 or df[a][b - 1] == 2) and not visited[a][b - 1]:
        b -= 1
        visited[a][b] = True
        route.append("left")
    elif b + 1 <= len(df[0]) - 1 and (df[a][b + 1] == 1 or df[a][b + 1] == 2) and not visited[a][b + 1]:
        b += 1
        visited[a][b] = True
        route.append("right")
    elif a - 1 >= 0 and (df[a - 1][b] == 1 or df[a - 1][b] == 2) and not visited[a - 1][b]:
        a -= 1
        visited[a][b] = True
        route.append("up")
    else:
        not_rout_found()


def down_right_first():
    global b, df, a, visited, route
    if a + 1 <= len(df) - 1 and (df[a + 1][b] == 1 or df[a + 1][b] == 2) and not visited[a + 1][b]:
        a += 1
        visited[a][b] = True
        route.append("down")
    elif b + 1 <= len(df[0]) - 1 and (df[a][b + 1] == 1 or df[a][b + 1] == 2) and not visited[a][b + 1]:
        b += 1
        visited[a][b] = True
        route.append("right")
    elif b - 1 >= 0 and (df[a][b - 1] == 1 or df[a][b - 1] == 2) and not visited[a][b - 1]:
        b -= 1
        visited[a][b] = True
        route.append("left")
    elif a - 1 >= 0 and (df[a - 1][b] == 1 or df[a - 1][b] == 2) and not visited[a - 1][b]:
        a -= 1
        visited[a][b] = True
        route.append("up")
    else:
        not_rout_found()

def up_right_first():
    global b, df, a, visited, route
    if a - 1 >= 0 and (df[a - 1][b] == 1 or df[a - 1][b] == 2) and not visited[a - 1][b]:
        a -= 1
        visited[a][b] = True
        route.append("up")
    elif b + 1 <= len(df[0]) - 1 and (df[a][b + 1] == 1 or df[a][b + 1] == 2) and not visited[a][b + 1]:
        b += 1
        visited[a][b] = True
        route.append("right")
    elif b - 1 >= 0 and (df[a][b - 1] == 1 or df[a][b - 1] == 2) and not visited[a][b - 1]:
        b -= 1
        visited[a][b] = True
        route.append("left")
    elif a + 1 <= len(df) - 1 and (df[a + 1][b] == 1 or df[a + 1][b] == 2) and not visited[a + 1][b]:
        a += 1
        visited[a][b] = True
        route.append("down")
    else:
        not_rout_found()


df = [
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 0],
    [1, 0, 1, 0, 2, 1],
    [1, 0, 1, 0, 1, 1],
    [1, 1, 1, 1, 1, 1]
]

def not_rout_found():
    print("No route found")
    exit()

def find_position(df, target):
    global b, a, visited, route
    for row in range(len(df)):
        for col in range(len(df[row])):
            if df[row][col] == target:
                return (row, col)
    return None


def find_route(df):
    global b, a, visited, route
    position = find_position(df, 2)
    if position:
        col = position[0]
        row = position[1]
    else:
        print("Not found exit")
    visited = [[False for i in range(len(df))] for i in range(len(df))]
    a, b = 0, 0
    route = []
    algoritm = []
    visited[0][0] = True
    while a != col or b != row:
        algoritm.append(f"{a,b}")
        if row == b:  # Якщо ми на одному рядку з виходом
            up_down_first()
        elif col == a:  # Якщо ми на одному стовпчику з виходом
            right_left_first()
        elif b < row:  # Вихід справа
                right_first()
        elif b > row:  # Вихід зліва
                left_first()
        elif a < col:  # Вихід знизу
                down_first()
        elif a > col:  # Вихід зверху
            up_first()
        elif a > col and b > row:  # Вихід знизу справа
            down_right_first()
        elif a > col and b < row:  # Вихід зверху справа
                up_right_first()
        elif a < col and b > row:  # Вихід знизу зліва
                    down_left_first()
        else:  # Вихід зверху зліва
                left_up_first()

    print("ALGORITM:")
    print(" => ".join(route))
    print("\n")
    print(" => ".join(algoritm))
    print("\n")


    for r in range(len(df)):
        for c in range(len(df[r])):
            if r == col and c == row:
                df[r][c] = 6
            elif visited[r][c] and visited[r][c] != (b,a):
                df[r][c] = '8'

    print("matrx path \"8\" = passed part:")
    for row in df:
        print([int(x) for x in row])

find_route(df)


