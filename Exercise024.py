from itertools import cycle
def spiral_matrix(level):

    matrix=[[None] * level for lvl in range(level)]

    #start
    x,y = 0,0
    moves=cycle(((0,1),(1,0),(0,-1),(-1,0)))
    dx,dy=next(moves)

    for i in range(level**2):
        matrix[x][y]=i+1
        xdx = x + dx
        ydy = y + dy
        if not 0 <= xdx < level or not 0 <=ydy < level or matrix[xdx][ydy] is not None:
            dx,dy=next(moves)

        x+=dx
        y+=dy
    return matrix