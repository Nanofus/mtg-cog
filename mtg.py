""" MTG Card Fetcher cog for the Red Discord bot """
""" Copyright (c) 2017 Ville Talonpoika """

import discord
from discord.ext import commands

from mtgsdk import Card
from mtgsdk import Set

class MTG:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def mtg(self, ctx, word1="", word2="", word3="", word4="", word5="", word6=""):

        if word1 == "" or word1 == "help":
            await self.bot.say("Syntax: `!mtg cardname` or `!mtg [set] cardname`")
            return

        cardset = ""
        if word1[0] == "[" and word1[len(word1) - 1] == "]":
            cardset = word1[1:-1]
            cardname = (word2 + " " + word3 + " " + word4 + " " + word5 + " " + word6).rstrip()
        else:
            cardname = (word1 + " " + word2 + " " + word3 + " " + word4 + " " + word5 + " " + word6).rstrip()

        cards = []
        mcmLink = ""
        if cardset != "":
            cards = Card.where(set=cardset).where(name=cardname).all()
            if len(cards) == 0:
                await self.bot.say("Card not found.")
                return
            mcmLink = "https://www.magiccardmarket.eu/Products/Singles/" + cards[0].set_name.replace(" ", "+") +  "/"
        else:
            cards = Card.where(name=cardname).all()
            if len(cards) == 0:
                await self.bot.say("Card not found.")
                return
            mcmLink = "https://www.magiccardmarket.eu/Cards/"

        message = (cards[0].name + " " + cards[0].image_url + "\nGatherer: http://gatherer.wizards.com/Pages/Card/Details.aspx?name=" + cards[0].name.replace(" ", "%20") + "\nMCM: " + mcmLink + cards[0].name.replace(" ", "+"))

        await self.bot.say(message)

def setup(bot):
    bot.add_cog(MTG(bot))
