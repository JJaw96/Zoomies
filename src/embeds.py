import discord

from constants.trophy_emojis import trophy_emojis


def the_hunt_winners():
    embed = discord.Embed(title="The Hunt Winners", colour=0xFE86E4)

    embed.add_field(
        name="<:Hubert:1524823059436146719> Chapter I (Hueycoatl)",
        value="N/A\n",
        inline=False,
    )
    embed.add_field(
        name="<:hilt:1524823060308561960> Chapter II (Nex)",
        value=f"{trophy_emojis[0]} We Can Spoon, Voteyes2pvp\n",
        inline=False,
    )
    embed.add_field(
        name="<:whelm:1524823069401550958> Chapter III (Barbarian Assault)",
        value=f"{trophy_emojis[1]} w1zzy, SithLordMeow, dnd5, ZaryteKnight, Pattaya\n",
        inline=False,
    )
    embed.add_field(
        name="<:rapier:1524823074866724915> Chapter IV (Theatre of Blood)",
        value=f"{trophy_emojis[2]} N/A\n",
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
            value=f"> {player_normie} - {metric_normie:,} {terminology}\n> <:iron:1524823076003643492> {player_iron} - {metric_iron:,} {terminology}",
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
        placements_string = ""

        for i, placement in enumerate(activity["placements"]):
            if len(placement["submissions"]) == 0:
                placements_string += f"> {trophy_emojis[i + 1]} • N/A\n"
                continue
            for submission in placement["submissions"]:
                placements_string += f"> {trophy_emojis[i + 1]} • {submission['username']} • {convert_game_ticks_to_time(submission['metric']) if activity['is_time_based'] else submission['metric']} • [Proof]({submission['imgur_url']})\n"

        embed.add_field(
            name=f"{activity['name']} {activity['emoji']}",
            value=placements_string,
            inline=False,
        )
    return embed


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
        value=f"{trophy_emojis[0]} 1st place!"
        if new_placement == 1
        else f"{trophy_emojis[1]} 2nd place"
        if new_placement == 2
        else f"{trophy_emojis[2]} 3rd place",
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
