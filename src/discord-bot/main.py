import discohook
import json

# Read creds.json and parse the json
with open("creds.json", "r") as f:
    creds = json.load(f)

app = discohook.Client(
    application_id = creds["APPLICATION_ID"],
    token = creds["APPLICATION_TOKEN"],
    public_key = creds["APPLICATION_PUBLIC_KEY"]
)

@app.on_event("startup")
async def ready():
    print("Bot is ready!")

@app.command(
    id="1076419367526465567",
    name="help", 
    description="basic help command for the bot"
)
async def help_command(interaction: discohook.Interaction):
    await interaction.response(
        "Hello, World!",
        embed=discohook.Embed(title="Help", description="This is a help command"),
        ephemeral=True,
    )