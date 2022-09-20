#this gives diamonds to new posts every 15 seconds.
import deso
from datetime import datetime
import time
import os

desoPosts = deso.Posts()

SEED_HEX = os.getenv("SEED_HEX")
PUBLIC_KEY = ""
desoSocial = deso.Social(nodeURL="https://bitclout.com/api/v0/", publicKey=PUBLIC_KEY, seedHex=SEED_HEX)  #

timer1 = 0
while (True):
    try:
        if time.time() - timer1 > 15:
            timer1 = time.time()

            posts = desoPosts.getPostsStateless(getPostsForGlobalWhitelist=False, fetchSubcommnets=True,
                                                readerPublicKey=PUBLIC_KEY,
                                                numToFetch=10).json()
            for post in posts["PostsFound"]:

                last_post_hash = post["PostHashHex"]
                if (post["IsHidden"] == False and len(post["Body"]) > 0):
                    nanos = post["TimestampNanos"]
                    secs = nanos / 1e9
                    dt = datetime.fromtimestamp(secs)

                    now = datetime.now()
                    duration = now - dt
                    if duration.total_seconds() <= 15:
                        print(post["Body"])
                        status = desoSocial.diamond(post["PostHashHex"], post["PosterPublicKeyBase58Check"],
                                                    diamondLevel=1).json()
                        if "Transaction" in status:
                            print("==>Done")
                        else:
                            print("==>Error")
                        time.sleep(5)
    except Exception as e:
        print(e)
