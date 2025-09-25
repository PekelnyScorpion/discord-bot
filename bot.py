import discord
from discord.ext import commands
import os
import asyncio

<<<<<<< HEAD
intents = discord.Intents.all()
=======
intents = discord.Intents.all()  # Aktivuj všechny eventy pro test
>>>>>>> ec02a147fc4342307ea1d7dd3e2d99816384f47e
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
<<<<<<< HEAD
    print(f"✅ Bot je přihlášen jako {bot.user}")
=======
    print(f"✅ Přihlášen jako {bot.user}")
>>>>>>> ec02a147fc4342307ea1d7dd3e2d99816384f47e

@bot.event
async def on_voice_state_update(member, before, after):
    if after.channel and not before.channel:
        if not member.bot:
            voice_channel = after.channel
            print(f"🔔 {member.display_name} se připojil do kanálu: {voice_channel.name}")
            try:
                vc = await voice_channel.connect()
<<<<<<< HEAD
                print("✅ Bot se připojil do voice kanálu")
            except Exception as e:
                print(f"❌ Chyba při připojení: {e}")
=======
                print("✅ Připojeno do voice kanálu")
            except Exception as e:
                print(f"❌ Chyba při připojení do voice: {e}")
>>>>>>> ec02a147fc4342307ea1d7dd3e2d99816384f47e
                return

            jmeno = member.display_name.capitalize()

            hlasky = {
                "Lejtto": "hlasky/Lejtto.mp3",
                "Lovable": "hlasky/Lovable.mp3"
            }

            cesta = hlasky.get(jmeno, "hlasky/servus.mp3")

            print(f"🎧 Soubor k přehrání: {cesta}")
<<<<<<< HEAD
            print(f"📂 Existuje: {os.path.exists(cesta)}")

            if os.path.exists(cesta):
=======
            print(f"📂 Soubor existuje: {os.path.exists(cesta)}")

            if os.path.exists(cesta):
                print("✅ Soubor existuje, zkouším přehrát...")
>>>>>>> ec02a147fc4342307ea1d7dd3e2d99816384f47e
                try:
                    audio_source = discord.FFmpegPCMAudio(cesta, executable="ffmpeg")
                    vc.play(audio_source)
                    print("✅ Přehrávání spuštěno")
<<<<<<< HEAD
                    await asyncio.sleep(5)
=======

                    await asyncio.sleep(5)
                    print("✅ Odpojuji se po 5 sekundách")
>>>>>>> ec02a147fc4342307ea1d7dd3e2d99816384f47e
                except Exception as e:
                    print(f"❌ Chyba při přehrávání: {e}")
            else:
                print("❌ Soubor neexistuje")

            await vc.disconnect()
<<<<<<< HEAD
            print("🔌 Bot se odpojil z voice kanálu")

@bot.command()
async def test(ctx):
    await ctx.send("✅ Bot reaguje na příkazy")
=======
            print("🔌 Odpojeno z voice kanálu")
>>>>>>> ec02a147fc4342307ea1d7dd3e2d99816384f47e

bot.run(os.getenv("DISCORD_TOKEN"))
