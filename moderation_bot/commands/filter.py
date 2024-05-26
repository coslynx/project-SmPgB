#import necessary packages
from utils.config import FILTER_WORDS

#filter function to check for offensive language and spam
async def filter_message(message):
    content = message.content.lower()

    #check for offensive language
    for word in FILTER_WORDS:
        if word in content:
            await message.delete()
            await message.channel.send(f"{message.author.mention}, please refrain from using offensive language.")
            break

    #check for spam
    spam_count = 0
    async for past_message in message.channel.history(limit=10):
        if past_message.author == message.author and past_message.content == message.content:
            spam_count += 1
            if spam_count >= 3:
                await message.author.ban(reason="Spamming")
                await message.channel.send(f"{message.author.mention} has been banned for spamming.")
                break

#end of filter.py file