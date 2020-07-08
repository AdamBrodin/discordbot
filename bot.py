import discord

# Global Variables
botToken = "NzIxODc1MzkyMTg4NjQ1NDc4.Xudiqg.MUA4ng2QjBA60KbjBTiJucl-nmE"
client = discord.Client()


class AutoResponse:
    def __init__(self, keyMessage, respondMessage, mustEqualTo, capsSensitive):
        self.keyMessage = keyMessage
        self.respondMessage = respondMessage
        self.mustEqualTo = mustEqualTo
        self.capsSensitive = capsSensitive


autoResponses = []
autoResponses.append(AutoResponse("gn", "God natt bope :)", False, False))
autoResponses.append(AutoResponse("gorilla", "Oo-Aa!", False, False))
autoResponses.append(AutoResponse("15 min", "Femton minuter, en kvart", False, False))
autoResponses.append(
    AutoResponse("hungrig", "Kristens Pizzeria, vad vill du beställa?", False, False)
)
autoResponses.append(AutoResponse("Vem var det som kasta", "Ingen!", False, False))


def runClient():
    client.run(botToken)


@client.event
async def on_message(message):
    # Analyses the received message and checks whether corresponds to a matching key message
    for i in range(len(autoResponses)):
        if autoResponses[i].mustEqualTo:
            if autoResponses[i].keyMessage == message.content:
                await message.channel.send(autoResponses[i].respondMessage)
        elif not autoResponses[i].mustEqualTo:
            if autoResponses[i].capsSensitive:
                if autoResponses[i].keyMessage in message.content:
                    await message.channel.send(autoResponses[i].respondMessage)
            elif (
                not autoResponses[i].capsSensitive
                and autoResponses[i].keyMessage.lower() in message.content.lower()
            ):
                await message.channel.send(autoResponses[i].respondMessage)


runClient()
