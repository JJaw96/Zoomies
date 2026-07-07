import discord

from constants.trophy_emojis import trophy_emojis


def the_hunt_winners():
    embed = discord.Embed(title="The Hunt Winners", colour=0xFE86E4)

    embed.add_field(
        name="<:huberte:1514809555152932864> Chapter I (Hueycoatl)",
        value="N/A\n",
        inline=False,
    )
    embed.add_field(
        name="<:ancient_hilt:1514809924515790889> Chapter II (Nex)",
        value="<:1stplace:1514784685295927435> We Can Spoon, Voteyes2pvp\n",
        inline=False,
    )
    embed.add_field(
        name="<:warrior_helm:1514809925090545674> Chapter III (Barbarian Assault)",
        value="<:1stplace:1514784685295927435> w1zzy, SithLordMeow, dnd5, ZaryteKnight, Pattaya\n",
        inline=False,
    )
    embed.add_field(
        name="<:ghrazi_rapier:1514810083278852126> Chapter IV (Theatre of Blood)",
        value="N/A\n",
        inline=False,
    )

    embed.set_thumbnail(url="https://i.imgur.com/8GI8n4g.png")

    return embed


def highest_kcs(data, category_name):
    embed = discord.Embed(title=category_name, colour=0xFE86E4)

    for key in data:
        # convert to comma format 1234 = 1,234
        player_normie = data[key]["normie"]["name"]
        player_iron = data[key]["iron"]["name"]
        metric_normie = data[key]["normie"]["kills"]
        metric_iron = data[key]["iron"]["kills"]
        terminology = data[key]["normie"]["terminology"]

        embed.add_field(
            name=f"{get_clean_name(key)} {data[key]['emote']}",
            value=f"> {player_normie} - {metric_normie:,} {terminology}\n> <:ironman:1516279477657800724> {player_iron} - {metric_iron:,} {terminology}",
            inline=False,
        )

    embed.add_field(
        name="",
        value="Last updated: " + discord.utils.format_dt(discord.utils.utcnow()),
    )

    return embed


def pb_category(activity_payloads, category_name):
    embed = discord.Embed(title=category_name, description="", colour=0xFE86E4)

    for activity in activity_payloads:
        embed.add_field(
            name=f"{activity['name']} {activity['emoji']}", value="", inline=False
        )
    return embed
    # [
    #     {
    #         "name": "Duke Sucellus",
    #         "emoji": "<:Baron:1518781036081709106>",
    #         "placements_to_show": 1,
    #         "placements": [{"submissions": []}],
    #         "is_time_based": True,
    #     },
    #     {
    #         "name": "Duke Sucellus (Awakened)",
    #         "emoji": "<:Baron:1518781036081709106>",
    #         "placements_to_show": 1,
    #         "placements": [{"submissions": []}],
    #         "is_time_based": True,
    #     },
    #     {
    #         "name": "Vardorvis",
    #         "emoji": "<:Butch:1518781033104015605>",
    #         "placements_to_show": 1,
    #         "placements": [{"submissions": []}],
    #         "is_time_based": True,
    #     },
    #     {
    #         "name": "Vardorvis (Awakened)",
    #         "emoji": "<:Butch:1518781033104015605>",
    #         "placements_to_show": 1,
    #         "placements": [{"submissions": []}],
    #         "is_time_based": True,
    #     },
    #     {
    #         "name": "The Whisperer",
    #         "emoji": "<:Wisp:1518781031887405248>",
    #         "placements_to_show": 1,
    #         "placements": [{"submissions": []}],
    #         "is_time_based": True,
    #     },
    #     {
    #         "name": "The Whisperer (Awakened)",
    #         "emoji": "<:Wisp:1518781031887405248>",
    #         "placements_to_show": 1,
    #         "placements": [{"submissions": []}],
    #         "is_time_based": True,
    #     },
    #     {
    #         "name": "Leviathan",
    #         "emoji": "<:Lilviathan:1518781035163287813>",
    #         "placements_to_show": 1,
    #         "placements": [
    #             {"submissions": [{"username": "The", "metric": 53, "imgur_url": ""}]}
    #         ],
    #         "is_time_based": True,
    #     },
    #     {
    #         "name": "Leviathan (Awakened)",
    #         "emoji": "<:Lilviathan:1518781035163287813>",
    #         "placements_to_show": 1,
    #         "placements": [
    #             {
    #                 "submissions": [
    #                     {
    #                         "username": "1:01",
    #                         "metric": 35,
    #                         "imgur_url": "https://i.imgur.com/8p3cdcx.png",
    #                     }
    #                 ]
    #             }
    #         ],
    #         "is_time_based": True,
    #     },
    # ]


def changelog(
    players: str,
    activity: str,
    metric: str,
    imgur_url: str,
    leaderboard_url: str,
    is_time_based: bool,
    new_placement: int | None,
):
    embed = discord.Embed(
        title="New PB Achieved!",
        colour=0xFE86E4,
        timestamp=discord.utils.utcnow(),
    )

    embed.add_field(
        name="Submitter(s)",
        value=players,
    )

    embed.add_field(
        name="Activity",
        value=activity,
    )

    # TODO - Time or integer
    embed.add_field(
        name="PB",
        value=convert_game_ticks_to_time(metric) if is_time_based else metric,
    )

    embed.add_field(
        name="Ranking",
        value="<:1stplace:1514784685295927435> 1st place!"
        if new_placement == 1
        else "<:2ndplace:1514784692996669490> 2nd place"
        if new_placement == 2
        else "<:3rdplace:1514784698692276426> 3rd place",
    )

    embed.add_field(
        name="Leaderboard Link",
        value=leaderboard_url,
    )

    if imgur_url:
        embed.set_image(url=imgur_url)

    return embed


def get_clean_name(boss_name) -> str:
    clean_name = str(boss_name.name)
    # Add a space between each uppercase letter
    for i in range(len(clean_name) - 1, 0, -1):
        if clean_name[i].isupper() and clean_name[i - 1].islower():
            clean_name = clean_name[:i] + " " + clean_name[i:]

    return clean_name


def convert_game_ticks_to_time(ticks: int) -> str:
    total_ms = ticks * 600
    minutes, rem_ms = divmod(total_ms, 60_000)
    seconds, ms = divmod(rem_ms, 1_000)
    centiseconds = ms // 10

    return f"{minutes}:{seconds:02}.{centiseconds:02}"
