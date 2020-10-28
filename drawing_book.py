total_pages = int(input())
required_page = int(input())
front = (required_page)//2
back = (total_pages)//2-(required_page)//2
print(min(front,back))
