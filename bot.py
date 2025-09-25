import discord
from discord.ext import commands
import os
import asyncio

intents = discord.Intents.default()
intents.voice_states = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Přihlášen jako {bot.user}")

@bot.event
async def on_voice_state_update(member, before, after):
    if after.channel and not before.channel:
        if not member.bot:
            voice_channel = after.channel
            vc = await voice_channel.connect()

            # Získat jméno uživatele s velkým prvním písmenem
            jmeno = member.display_name.capitalize()

            # Mapování jmen na specifické hlášky
            hlasky = {
                "Lejtto": "hlasky/Lejtto.mp3",
                "Lovable": "hlasky/Lovable.mp3"
            }

            # Vyber správnou hlášku
            if jmeno in hlasky and os.path.exists(hlasky[jmeno]):
                cesta = hlasky[jmeno]
            else:
                cesta = "hlasky/servus.mp3"

            # Přehrát zvuk
            if os.path.exists(cesta):
                audio_source = discord.FFmpegPCMAudio(cesta)
                vc.play(audio_source)

                while vc.is_playing():
                    await asyncio.sleep(1)

            await vc.disconnect()

# Přihlášení bota pomocí tokenu z Renderu
bot.run(os.getenv("DISCORD_TOKEN"))
