"""those you can to find way in labirint"""


df = [
    [1, 0, 1, 0, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 0, 0, 1],
    [1, 1, 1, 0, 0, 0, 1, 2],
    [0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 0, 1, 1]
]




#find_position - шукаємо двойку в матриці та записуємо її координати
def find_position_t(df, target):
    for row in range(len(df)):
        for col in range(len(df[row])):
            if df[row][col] == target:
                return (row, col)
    return None




def find_route_b(df, a, b, col, row, visited, route):
    #if a == col and b == row: !!!Якщо дісталися виходу!!!
    if a == col and b == row:
        route.append((a, b))
        return True

    visited[a][b] = True
    route.append((a, b))

    # Можливі напрямки ходів
    ways = [(1, 0, "down"), (0, 1, "right"), (-1, 0, "up"), (0, -1, "left")]

    # Пробуємо рухатись в кожен напрямок
    for way in ways:
        next_a, next_b = a + way[0], b + way[1]

        if is_move(df, visited, next_a, next_b):
            if find_route_b(df, next_a, next_b, col, row, visited, route):
                return True

    # це якщо ми зайшли в тупий кут
    route.pop()

def find_route(df):
    position = find_position_t(df, 2)
    if position:
        col = position[0]
        row = position[1]
    else:
        print("Not found exit")
        return

    visited = [[False for r in range(len(df[0]))] for c in range(len(df))]
    route = []

    if find_route_b(df, 0, 0, col, row, visited, route):
        print("Route found:")
        print(" => ".join([f"({x},{y})" for x, y in route]))
        # Тутв в наспозначається 8 - шлях який був пройдений and 6 - вихід з лабіринту
        for x, y in route:
            df[x][y] = 8
        df[col][row] = 6
        print("\nMatrix path '8' = passed part, '6' = exit:")
        for row in df:
            print(row)
    else:
        print("No route found")

def is_move(df, visited, a, b):
    #перевірка чи є можливий хід не виходячи за межі матриці
    if 0 <= a < len(df) and 0 <= b < len(df[0]) and df[a][b] != 0 and not visited[a][b]:
        return True
    else:
        return False

def not_rout_found():
    print("No route found")
    exit()

find_route(df)
