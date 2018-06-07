import facebook
import requests


def graphAPI(token):
    token = token
    fb = facebook.GraphAPI(access_token=token)
    posts = fb.get_connections(id='me', connection_name='posts')
    posts = posts['data']
    fans =[]
    for row in posts:
        if 'message' in row:
            date = row['created_time']
            message = row['message']

            if 'likes' in row:
                likes = row['likes']['data']
                for row in likes:
                    name = row['name']
                    fans.append(name)

    print(fans)
    print(max(fans))

graphAPI("EAACEdEose0cBANgmOfm5tZCwZBZBhvGVteZCE1752UvS0P0VEFZCCkXpfVZC64HEr9Ka6JMwylW2cxZBKyXF9SBSZAJevIZCl94KPN5nwPBr2RSTqtHYbSDbXsZAo8RGH2ZA4kSbZAt1pMJyoJcdMyfsKAKeMUCxSdVF1OuvDgF1XRgJVY9dLuVmmL25cWbJ3z10b6ii4g49adJZCPwZDZD")
