import logging
import discord
from discord.ext import commands

from database import init_db, SessionLocal
from models import Activity, Submission


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=discord.Intents.all())

        init_db()

        self.SessionLocal = SessionLocal
        self.Activity = Activity
        self.Submission = Submission

        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    async def setup_hook(self) -> None:
        cogs = [
            "cogs.pb_submission",
            "cogs.pb_approval",
            "cogs.static_embeds",
            "cogs.highest_killcounts",
            "cogs.display_pbs",
        ]
        for cog in cogs:
            try:
                await self.load_extension(cog)
                self.logger.info(f"{cog} loaded successfully.")
            except Exception as e:
                self.logger.error(f"Failed to load {cog}: {e}")

    async def on_ready(self):
        await self.tree.sync()
        self.logger.info(f"{self.user} has connected to Discord!")
