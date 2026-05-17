def find_content_children(greed, cookies):
    greed.sort()
    cookies.sort()
    child = 0
    cookie = 0
    while child < len(greed) and cookie < len(cookies):
        if cookies[cookie] >= greed[child]:
            child += 1
        cookie += 1
    return child


greed = list(map(int, input("Enter greed factors: ").split()))
cookies = list(map(int, input("Enter cookie sizes: ").split()))

result = find_content_children(greed, cookies)

print("Maximum Content Children:", result)