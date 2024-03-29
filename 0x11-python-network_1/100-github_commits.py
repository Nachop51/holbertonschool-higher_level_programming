#!/usr/bin/python3
"""  Python script that takes 2 arguments in order to solve this challenge
    - The first argument will be the repository name
    - The second argument will be the owner name
    - You must use the packages requests and sys
    - You are not allowed to import packages other than requests and sys
    - You don't need to check arguments passed to the script (number or type)
 """

if __name__ == '__main__':
    import sys
    import requests

    repo = sys.argv[1]
    owner = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)
    response = requests.get(url)
    if response.status_code < 400:
        result = response.json()
        for res in result[:10]:
            sha = res.get('sha')
            author = res.get("commit").get("author").get("name")
            print("{}: {}".format(sha, author))
