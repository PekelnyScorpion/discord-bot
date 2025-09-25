import discord
from discord.ext import commands
import os
import asyncio

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot je přihlášen jako {bot.user}")

@bot.event
async def on_voice_state_update(member, before, after):
    if after.channel and not before.channel:
        if not member.bot:
            voice_channel = after.channel
            print(f"🔔 {member.display_name} se připojil do kanálu: {voice_channel.name}")
            try:
                vc = await voice_channel.connect()
                print("✅ Bot se připojil do voice kanálu")
            except Exception as e:
                print(f"❌ Chyba při připojení: {e}")
                return

            jmeno = member.display_name.capitalize()

            hlasky = {
                "Lejtto": "Lejtto.mp3",
                "Lovable": "Lovable.mp3"
            }

            cesta = hlasky.get(jmeno, "servus.mp3")

            print(f"🎧 Soubor k přehrání: {cesta}")
            print(f"📂 Absolutní cesta: {os.path.abspath(cesta)}")
            print(f"📂 Existuje: {os.path.exists(cesta)}")

            if os.path.exists(cesta):
                try:
                    audio_source = discord.FFmpegPCMAudio(cesta, executable="ffmpeg")
                    vc.play(audio_source)
                    print("✅ Přehrávání spuštěno")
                    await asyncio.sleep(5)
                except Exception as e:
                    print(f"❌ Chyba při přehrávání: {e}")
            else:
                print("❌ Soubor neexistuje")

            await vc.disconnect()
            print("🔌 Bot se odpojil z voice kanálu")

@bot.command()
async def test(ctx):
    await ctx.send("✅ Bot reaguje na příkazy")

bot.run(os.getenv("DISCORD_TOKEN"))
