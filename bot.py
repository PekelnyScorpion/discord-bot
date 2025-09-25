import discord
from discord.ext import commands
import os
import asyncio

intents = discord.Intents.all()  # Aktivuj všechny eventy pro test
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Přihlášen jako {bot.user}")

@bot.event
async def on_voice_state_update(member, before, after):
    if after.channel and not before.channel:
        if not member.bot:
            voice_channel = after.channel
            print(f"🔔 {member.display_name} se připojil do kanálu: {voice_channel.name}")
            try:
                vc = await voice_channel.connect()
                print("✅ Připojeno do voice kanálu")
            except Exception as e:
                print(f"❌ Chyba při připojení do voice: {e}")
                return

            jmeno = member.display_name.capitalize()

            hlasky = {
                "Lejtto": "hlasky/Lejtto.mp3",
                "Lovable": "hlasky/Lovable.mp3"
            }

            cesta = hlasky.get(jmeno, "hlasky/servus.mp3")

            print(f"🎧 Soubor k přehrání: {cesta}")
            print(f"📂 Soubor existuje: {os.path.exists(cesta)}")

            if os.path.exists(cesta):
                print("✅ Soubor existuje, zkouším přehrát...")
                try:
                    audio_source = discord.FFmpegPCMAudio(cesta, executable="ffmpeg")
                    vc.play(audio_source)
                    print("✅ Přehrávání spuštěno")

                    await asyncio.sleep(5)
                    print("✅ Odpojuji se po 5 sekundách")
                except Exception as e:
                    print(f"❌ Chyba při přehrávání: {e}")
            else:
                print("❌ Soubor neexistuje")

            await vc.disconnect()
            print("🔌 Odpojeno z voice kanálu")

bot.run(os.getenv("DISCORD_TOKEN"))
