Jason bot is a simple telegram bot in python that uses the python-telegram library. It  provides links to various socials such as Linkedin, github, email
Link to see how it works https://youtube.com/shorts/3THS7URXsSY?feature=share

I setup the bot using Telegrams API bot token.
Used python-telegram bot v20 with async 
I ran into a compatability issue between apscheduler (schedules tasks)  and tzlocal (time zone) and fixed it by downgrading tzlocal version
I then kept the bot in polling mode so it continues to listen to messages
.
