#timezone library for scheduling tasks
import pytz

#import update class from library, represents new message/command 
from telegram import Update

from telegram.ext import (

    #main bot application class
    ApplicationBuilder,

    #listens for commands
    CommandHandler,

    #context for callback functions
    ContextTypes,
    
)
#scheduler library
from apscheduler.schedulers.asyncio import AsyncIOScheduler

# Handlers
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I am Jason's  bot. Type /help to see what I can do.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Links to everything:\n"
        "/linkedin - Visit my LinkedIn\n"
        "/github - Visit my GitHub\n"
        "/gmail - My email address"
    )
# reply functions for commands
async def linkedin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("https://www.linkedin.com/in/jason-gaynor-1899b62a0/")

async def github(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("https://github.com/JasonG22")

async def gmail(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("jasong220605@gmail.com")

# Main
def main():
    # Create scheduler with explicit pytz timezone
    scheduler = AsyncIOScheduler(timezone=pytz.UTC)

    #creates app and passes bot token
    app = (
        ApplicationBuilder()
        .token("removed for privacy")
        
        .build()
    )

    #handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("linkedin", linkedin))
    app.add_handler(CommandHandler("github", github))
    app.add_handler(CommandHandler("gmail", gmail))

    #start polling updates from tele
    app.run_polling()

# program Entry
if __name__ == '__main__':
    main()
