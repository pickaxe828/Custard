import discohook
import json

from deta import Deta

with open("creds.json", "r") as f:
    creds = json.load(f)

app = discohook.Client(
    application_id = creds["APPLICATION_ID"],
    token = creds["APPLICATION_TOKEN"],
    public_key = creds["APPLICATION_PUBLIC_KEY"]
)

deta = Deta(creds["DETA_ACCESS_KEY"])
base = deta.Base("sessions")

@app.on_event("startup")
async def ready():
    print("Bot is ready!")

@app.command(
    id="1076419367526465567",
    name="help", 
    description="Basic help command for the bot"
)
async def help_command(interaction: discohook.Interaction):
    await interaction.response(
        "Hello, World!",
        embed=discohook.Embed(title="Help", description="This is a help command. Definitely helpful."),
        ephemeral=True,
    )


@app.command(
    id="1077661226378727506",
    name="whoami", 
    description="Command to tell you... who you are."
)
async def whoami(interaction: discohook.Interaction):
    await interaction.response(
        embed=discohook.Embed(title="This is you:", 
                              description=f"This is you here: {interaction.author.id}. Definitely helpful."),
        ephemeral=True,
    )


@app.command(
    id="1077661226378727507",
    name="verify", 
    description="Verify your account here!"
)
async def verify(interaction: discohook.Interaction):
    # await base.put(interaction)
    await interaction.response(
        embed=discohook.Embed(title="Verify yourself:", 
                              description="This is a help command",
                              url="https://google.com"
                              ),
        ephemeral=True,
    )