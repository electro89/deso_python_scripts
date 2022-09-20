import deso
import time

USERNAME=""
SEED_HEX = ''
PUBLIC_KEY = ""
desoSocial = deso.Social(nodeURL="https://bitclout.com/api/v0/", publicKey=PUBLIC_KEY, seedHex=SEED_HEX)  #
# print(desoSocial.submitPost("This is a test post from python")) #returns a response object. add .json() in end to see complete response
desoPosts = deso.Posts()

posts = desoPosts.getPostsForPublicKey(username=USERNAME, numToFetch=20).json()
print(posts["Posts"][0])
lastHash = posts["Posts"][len(posts["Posts"]) - 1]["PostHashHex"]
while True:
    posts = desoPosts.getPostsForPublicKey(username=USERNAME, numToFetch=50, lastPostHashHex=lastHash).json()
    for post in posts["Posts"]:
        try:
            print(post)
            postHashHex = post["PostHashHex"]
            lastHash = postHashHex
            print(postHashHex)
            if len(post["Body"]) > 0:
                if post["RepostedPostEntryResponse"] is None:
                    print("post")
                    if not post["IsHidden"]:
                        time.sleep(15)
                else:
                    print("Reclout")
                    if not post["IsHidden"]:
                     
                        time.sleep(15)
            else:
                print("repost")
                print(post["RepostedPostEntryResponse"]["PostHashHex"])
                if not post["IsHidden"]:
                    print(desoSocial.submitPost(body='', repostedPostHash=post["RepostedPostEntryResponse"]["PostHashHex"],
                                                postHashHexToModify=postHashHex, isHidden=True).json())
                    time.sleep(15)

        except Exception as e:
            print(e)

