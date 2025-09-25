import discord
from discord.ext import commands
import asyncio

# ✅ Správné nastavení intentů
intents = discord.Intents.default()
intents.message_content = True
intents.presences = True
intents.members = True
intents.voice_states = True
intents.guilds = True

# ✅ Vytvoření bota s intentama
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Přihlášen jako {bot.user}")

@bot.event
async def on_voice_state_update(member, before, after):
    if after.channel and not before.channel:
        if not member.bot:
            voice_channel = after.channel
            vc = await voice_channel.connect()
            audio_source = discord.FFmpegPCMAudio(r"E:\servus.mp3")
            vc.play(audio_source)

            while vc.is_playing():
                await asyncio.sleep(1)

            await vc.disconnect()

# ✅ Token bota
bot.run(os.getenv("DISCORD_TOKEN"))
