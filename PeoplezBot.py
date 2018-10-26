#RevaliBot ver 1.2
#Created by Peoplez101 (Ryan E.)
#Last Update 25/10/18 (DD/MM/YY)

import discord
import datetime
import random
from discord.ext import commands

import calculator_core as cc

bot = commands.Bot(command_prefix='$', description="Peoplez101's Discord Chat Bot")

def to_upper(arguement):
    return arguement.upper()

def to_lower(arguement):
    return arguement.lower()

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)

    #Changes the game title associated with the bot
    await bot.change_presence(game=discord.Game(name='type $help for help!'))

#Hello
@bot.command()
async def hello():
    """Say Hello"""
    await bot.say("Well that's just asinine!")


#Echo
@bot.command()
async def echo(*, args):
    """Returns the input the user inputted"""
    words = args.split()
    join = ''.join(words)
    await bot.say(join)

#Text to Uppercase
@bot.command()
async def upper(*, content = to_upper):
    """Returns the users input in all uppercase"""
    await bot.say(content)

#Text to Lowercase
@bot.command()
async def lower(*, content: to_lower):
    """Returns the users input in all lowercase"""
    await bot.say(content)


class copyPasta:

    @bot.command()
    async def navySeal():
        """Navy Seal Copypasta"""
        await bot.say("What the fuck did you just fucking say about me, you little bitch? I’ll have you know I graduated top of my class in the Navy Seals, and I’ve been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills.")
        await bot.say("I am trained in gorilla warfare and I’m the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words.")
        await bot.say("You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You’re fucking dead, kid.")
        await bot.say("I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that’s just with my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit.")
        await bot.say("If only you could have known what unholy retribution your little ‘clever’ comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldn’t, you didn’t, and now you’re paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. You’re fucking dead, kiddo.")

    @bot.command()
    async def oceanMan():
        """Ocean Man Copypasta"""
        await bot.say("OCEAN MAN 🌊 😍 Take me by the hand ✋ lead me to the land that you understand 🙌 🌊 OCEAN MAN 🌊 😍 The voyage 🚲 to the corner of the 🌎 globe is a real trip 👌 🌊 OCEAN MAN 🌊 😍 The crust of a tan man 👳 imbibed by the sand 👍 Soaking up the 💦 thirst of the land 💯")

    @bot.command()
    async def rickAndMorty():
        """Rick and Morty Copypasta"""
        await bot.say("To be fair, you have to have a very high IQ to understand Rick and Morty. The humor is extremely subtle, and without a solid grasp of theoretical physics most of the jokes will go over a typical viewer's head. There's also Rick's nihilistic outlook, which is deftly woven into his characterisation - his personal philosophy draws heavily from Narodnaya Volya literature, for instance. The fans understand this stuff; they have the intellectual capacity to truly appreciate the depths of these jokes, to realize that they're not just funny- they say something deep about LIFE. As a consequence people who dislike Rick and Morty truly ARE idiots- of course they wouldn't appreciate, for instance, the humour in Rick's existencial catchphrase ‘Wubba Lubba Dub Dub,’ which itself is a cryptic reference to Turgenev's Russian epic Fathers and Sons I'm smirking right now just imagining one of those addlepated simpletons scratching their heads in confusion as Dan Harmon's genius unfolds itself on their television screens. What fools... how I pity them. 😂 And yes by the way, I DO have a Rick and Morty tattoo. And no, you cannot see it. It's for the ladies' eyes only- And even they have to demonstrate that they're within 5 IQ points of my own (preferably lower) beforehand.")

#Alternate
@bot.command()
async def alternate(*, args):
    """Changes text into alternating upper/lower case"""
    counter = 1  #Chooses whether uppercase or lowercase
    letters = []
    arg = to_lower(args)
    words = arg.split()
    wordsLength = len(words)
    counter2 = 0

    for i in range(0,wordsLength):
        word = list(words[i])
        wordLength = len(word)
        
        for j in range(0, wordLength):
            if counter == 0:
                letters.append(word[j])
                counter2 += 1
                counter = 1
            else:
                upper = to_upper(word[j])
                letters.append(upper)
                counter2 += 1
                counter = 0
                
        letters.append(' ')
    join = ''.join(letters)
    await bot.say(join)   

# ReverseAlternate
@bot.command()
async def revalternate(*, args):
    """Changes the text into alternating upper/lower case"""
    counter = 1  #Chooses whether uppercase or lowercase
    letters = []
    arg = to_upper(args)
    words = arg.split()
    wordsLength = len(words)
    counter2 = 0

    for i in range(0,wordsLength):
        word = list(words[i])
        wordLength = len(word)
        
        for j in range(0, wordLength):
            if counter == 0:
                letters.append(word[j])
                counter2 += 1
                counter = 1
            else:
                lower = to_lower(word[j])
                letters.append(lower)
                counter2 += 1
                counter = 0
                
        letters.append(' ')
    join = ''.join(letters)
    print(join)
    await bot.say(join) 

    #Change Game
@bot.command()
async def changeGame(*, args):
    """Changes the game being played by the bot"""
    await bot.change_presence(game=discord.Game(name = args))

#owo
@bot.command()
async def owo(*, args):
    """uwu this changes text into weal good stuff. Twust me. """
    letters = []
    words = args.split()
    wordsLength = len(words)
    counter = 0

    for i in range(0,wordsLength):
        word = list(words[i])
        wordLength = len(word)

        for j in range(0,wordLength):
            if word[j] == "l":
                letters.append("w")
                counter += 1
            elif word[j] == "L":
                letters.append("W")
                counter += 1
            elif word[j] == "r":
                letters.append("w")
                counter += 1
            elif word[j] == "R":
                letters.append("W")
                counter += 1
            else:
                letters.append(word[j])
                counter += 1

        letters.append(' ')

    letters.append('owo')
    join = ''.join(letters)
    hold = join
    await bot.say(join)

@bot.command()
async def calc(*, args):
        """Simple Calculator. 
        Supported operations:
        Addition (+)
        Subtraction (-)
        Multiplication (* ×)
        Division (/ ÷)
        Exponentiation (^)
        Square Root (sqrt √)
        
        Parenthesis (), as well as BEDMAS is supported. 
        Use "digits=<n>" to round the answer to n number of digits.
        """
        terms = args.split()
        
        digits = -1
        parsed_digits = True
        for i in terms:
            if "digits=" in i:
                try:
                    digits = int(i.replace("digits=",""))
                    args = args.replace(i,"")
                except ValueError:
                    await bot.say("Invalid number of rounding digits.")
                    parsed_digits = False
        
        if(parsed_digits):
            try:
                eq = cc.parse_equation(args)
                res = cc.eval_equation(eq, digits)
                await bot.say(str(res))
            except ValueError as v:
                msg = str(v)
                
                if(msg == cc.invalid_token()):
                    await bot.say("Invalid token in expression. Maybe double check your equation?")
                elif(msg == cc.unbalanced_parenthesis()):
                    await bot.say("Unbalenced parenthesis found. Maybe double check your equation?")
                else:
                    await bot.say("Square root of a negative number found. That's not possible.")
            except ZeroDivisionError:
                await bot.say("You can't divide by zero!")

@bot.command()
async def arcana():
    """Random Arcana Given"""
    Arcana = ["Fool", "Jester", "Magician", "Priestess", "Empress", "Emperor", "Hierophant", "Lovers", "Chariot", "Justice", "Hermit", "Fortune", "Strength", "Hanged", "Death", "Temperance", "Devil" "Tower", "Star", "Moon", "Sun", "Judgement", "World"]
    integerRand = random.randint(1, 20)
    arcanaNum = integerRand - 1
    await bot.say(Arcana[arcanaNum])


@bot.command()
async def today():
    """Returns today's date"""
    today = datetime.datetime.now()
    day = str(today.day)
    month = str(today.month)
    year = str(today.year)
    date = year + "-" + month + "-" + day
    await bot.say("Today Is: " + date)

@bot.command()
async def close():
    print ('logging out')
    await bot.close()


bot.run('MzIyNTUwNjAyMTcxMTU0NDMz.DSidFg.ifKsPdbn-PoZAcuDkiDxvDkpTvE')

