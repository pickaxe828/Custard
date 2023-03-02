import discohook
import secrets
import json

from deta import Deta

BASE_URL = "https://custard-1-u4890829.deta.app/"

with open("creds.json", "r") as f:
    creds = json.load(f)

app = discohook.Client(
    application_id = creds["APPLICATION_ID"],
    token = creds["APPLICATION_TOKEN"],
    public_key = creds["APPLICATION_PUBLIC_KEY"]
)

deta = Deta(creds["DETA_ACCESS_KEY"])
sessions_store = deta.Base("sessions")

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
    id="1077661226378727507",
    name="verify", 
    description="Verify your account here!"
)
async def verify(interaction: discohook.Interaction):
    session_id = secrets.token_urlsafe(16)
    obj = {
        "user_id": interaction.author.id,
        "guild_id": interaction.guild_id,
        "action": "add",
        "role_id": 0
    }
    sessions_store.put(key = session_id, data = obj)

    view = discohook.View()
    view.add_button_row(
        discohook.Button(
            label = "Press me to Verify! ✅", 
            url = BASE_URL + "verify/" + session_id,
            style = discohook.ButtonStyle.link
        )
    )
    embed = discohook.Embed(
        title = "Joining this server requires verification.", 
        description = "Click the button below to verify yourself."       
    )

    await interaction.response(
        embed=embed,
        view=view,
        ephemeral=True
    )

@app.on_error
async def error_handler(error: Exception, data: dict):
    print(error)
    print(data)
    raise Exception