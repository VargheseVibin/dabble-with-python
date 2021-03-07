facebook_posts = [
    {"Likes": 21, "Comments": 2, "Shares": 10},
    {"Likes": 10, "Shares": 10},
    {"Comments": 2, "Shares": 10},
    {"Likes": 21, "Comments": 2, "Shares": 10},
    {"Comments": 2, "Shares": 10},
    {"Likes": 21, "Comments": 2, "Shares": 10},
]

total_likes = 0


for post in facebook_posts:
    try:
        total_likes += post["Likes"]
    except KeyError:
        total_likes = total_likes + 0
        print("Post doesn't have a Like")

print(f"Total Facebook Likes: {total_likes}")
