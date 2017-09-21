import os, time, praw, config

os.system("clear")
time.sleep(1)


def bot_login(): # Function that logs into Reddit using the parameters used in the config file
    print "Logging in..."
    r = praw.Reddit(username = config.username,
        password = config.password,
        client_id = config.client_id,
        client_secret = config.client_secret,
        user_agent = "tontomurphybot reply on /r/test -  PRAW test v.01")
    print "Logged in!"

    return r # returns an "instance" of being logged in


def run_bot(r): # Function that runs the bot



    for comment in r.subreddit('test').comments(limit=10):
        if "nuka" in comment.body:
            print comment.body, "\n\n", "  -", comment.id
#            comments_replied_to.append(comment.id) # This appends the comment ID to the comment we created
            time.sleep(1)

#            comment.reply("This is a bot reply with a pic [Here](https://imgur.com/gallery/GAG0DCW)")

# This is where the functions get called - it's essentially the starting point of the program
r = bot_login()
# for x in range(0, 1):

run_bot(r)
