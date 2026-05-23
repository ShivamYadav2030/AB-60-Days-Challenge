from collections import deque
def flood_fill(image, sr, sc, color):
    rows = len(image)
    cols = len(image[0])
    original = image[sr][sc]
    if original == color:
        return image
    queue = deque()
    queue.append((sr, sc))
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    while queue:
        r, c = queue.popleft()
        if image[r][c] == original:
            image[r][c] = color
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if image[nr][nc] == original:
                        queue.append((nr, nc))
    return image

image = [
    [1,1,1],
    [1,1,0],
    [1,0,1]
]

sr = 1
sc = 1
color = 2

result = flood_fill(image, sr, sc, color)

print("Flood Filled Image:")
for row in result:
    print(row)