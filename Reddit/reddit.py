import os, time, praw, config

#import sys
#sys.path.insert (0, '~/Desktop')
#import bob
os.system("clear")
time.sleep(1)


def bot_login(): # Function that logs into Reddit using the parameters used in the config file
    print ("Logging in...")
    r = praw.Reddit(username = config.username,
        password = config.password,
        client_id = config.client_id,
        client_secret = config.client_secret,
        user_agent = "osx:prawtest:v0.2 (by /u/tontomurphybot)")
        #user_agent = "tontomurphybot reply on /r/test -  PRAW test v.01"
    print ("Logged in!")

    return r # returns an "instance" of being logged in


def choose_sub(): # Function that chooses the Subreddit to run the program on
    print ("\n")
    entry = raw_input ("Enter the name of the Subreddit you want to check, or 'q' to quit > ")
    if entry =="q":
        exit(0)
    else:
        sub = entry

    return sub

def bot_title(r): # Function that prints title/url/Author of submissions in subreddit
    for submission in r.subreddit(sub).hot(limit=10):
        print (submission.title)
        print (submission.url)
        print (submission.author)
        print ("\n")


def bot_me(r): # Function that prints the top level commments in a submission
    for submission in r.subreddit(sub).hot(limit = 200):
        if submission.author == "tontomurphy":# or submission.author == "tontomurphybot":
            submission.comments.replace_more(limit=0)
            for comment in submission.comments.list():
                print(comment.body)




#r = bot_login()
#sub = choose_sub()
#c = choose_run(sub)




def choose_run(r, sub):
    while True:
        run = raw_input("Enter either 'title', 'me', 'c' to change sub or 'q' to quit > ")
        if run == "q":
            exit(0)
 
        if run == "c":
            choose_sub()

        if run == "title":
            bot_title(r)
    
        if run == "me":
            bot_me(r)
  
        if run != "title" and run != "me":
            print ("You need to enter either title or dude")

#r = bot_login()


r = bot_login()
sub = choose_sub()
print sub
choose_run(r, sub)
