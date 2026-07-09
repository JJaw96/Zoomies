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
        value=f"{trophy_emojis[1]} We Can Spoon, Voteyes2pvp\n",
        inline=False,
    )
    embed.add_field(
        name="<:whelm:1524823069401550958> Chapter III (Barbarian Assault)",
        value=f"{trophy_emojis[1]} w1zzy, SithLordMeow, dnd5, ZaryteKnight, Pattaya\n",
        inline=False,
    )
    embed.add_field(
        name="<:rapier:1524823074866724915> Chapter IV (Theatre of Blood)",
        value="N/A\n",
        inline=False,
    )

    embed.set_thumbnail(url="https://i.imgur.com/8GI8n4g.png")

    return embed


def bingo_winners_embeds():
    embeds = []

    # ----- First Bingo (2022) -----
    firstbingo_embed = discord.Embed(title="Unnamed Bingo (2022)")
    firstbingo_embed.add_field(
        name="Winners",
        value=f"{trophy_emojis[1]} kitty neko, Lil xarp, deadlymoth, Sanguinestis",
        inline=False,
    )
    firstbingo_embed.set_footer(text="August 24th, 2022")

    # ----- Candyland (2023) -----
    candyland_embed = discord.Embed(title="Candyland (2023)")
    candyland_embed.add_field(
        name="Winners",
        value=f"{trophy_emojis[1]} Impressed, KlRBY, Helen Feller, Baked, A Cat Dad, Iron Coosa",
        inline=False,
    )
    candyland_embed.add_field(
        name="",
        value="https://discord.com/channels/847313025919746129/847313574040305704/1097535747902423150\n",
    )

    candyland_embed.set_thumbnail(
        url="https://oldschool.runescape.wiki/images/thumb/Purple_sweets_detail.png/120px-Purple_sweets_detail.png?41120"
    )

    candyland_embed.set_footer(text="April 17th, 2023")

    candyland_embed.set_image(url="https://i.imgur.com/M5apOQv.png")

    snakes_embed = discord.Embed(title="Snakes & Ladders (2023)")

    snakes_embed.add_field(
        name="Winners",
        value=f"{trophy_emojis[1]} Lamhirh, Dopamemes, Adaboy23, Scarlet cat, Zueskin, Rotting,",
        inline=False,
    )

    snakes_embed.add_field(
        name="",
        value="https://discord.com/channels/847313025919746129/847313574040305704/1131088765675380847\n",
    )

    snakes_embed.set_thumbnail(
        url="https://oldschool.runescape.wiki/images/Ladders.png?b5be8&20150310211136"
    )

    snakes_embed.set_footer(text="July 19th, 2023")
    snakes_embed.set_image(url="https://i.imgur.com/gBbTq0j.png")

    # ----- Battle of the Gods (2023) -----
    battle_gods = discord.Embed(title="Battle of the Gods (2023)")

    battle_gods.add_field(
        name="",
        value=f"{trophy_emojis[1]} Lilies, Steals, Bird, justduff, jalals mane, Fat Cat, Silly Cowboy, Domimic, Virgin Rabbi, Shypu, Musei, LunasHowl, XtraIcy",
        inline=False,
    )

    battle_gods.add_field(
        name="",
        value="https://discord.com/channels/847313025919746129/847313574040305704/1148004422153158666\n",
    )

    battle_gods.set_thumbnail(
        url="https://oldschool.runescape.wiki/images/thumb/Zamorak%27s_statue_%28Slepe%29.png/122px-Zamorak%27s_statue_%28Slepe%29.png?7e7ee"
    )

    battle_gods.set_footer(text="September 3rd, 2023")
    battle_gods.set_image(url="https://i.imgur.com/kAMUnC9.png")

    # ----- Black cat bingo (2023) -----
    blackcatbingo = discord.Embed(title="Black Cat Halloween Bingo (2023)")

    blackcatbingo.add_field(
        name="",
        value=f"{trophy_emojis[1]} kitty neko, Lil Yeeter, Miggy Spoon, Iron Yesu, nora cat, unrot, Scarlet cat",
        inline=False,
    )

    blackcatbingo.set_thumbnail(
        url="https://oldschool.runescape.wiki/images/thumb/Cat_%28black%29.png/180px-Cat_%28black%29.png?1dfde"
    )

    blackcatbingo.add_field(
        name="",
        value="https://discord.com/channels/847313025919746129/847313574040305704/1165755681664667789\n",
    )

    blackcatbingo.set_footer(text="October 22nd, 2023")

    blackcatbingo.set_image(
        url="blob:https://imgur.com/85aae058-e4e9-47d8-9be0-586d2f83b31c"
    )

    # ----- Darts bingo -----
    darts = discord.Embed(title="Darts 2024")

    darts.add_field(
        name="",
        value=f"{trophy_emojis[1]} Norden, Rat King, Viables, Gerg, Lt Kasper, Bob Kat, Bornfury95, Wrldsbestsmp, unrot, nora cat",
        inline=False,
    )

    darts.set_footer(text="February 11th, 2024")

    darts.add_field(
        name="",
        value="https://discord.com/channels/847313025919746129/847313574040305704/1206795998077132810\n",
    )

    darts.set_thumbnail(
        url="https://oldschool.runescape.wiki/images/thumb/Target_%28Ranging_Guild%29.png/150px-Target_%28Ranging_Guild%29.png?89891"
    )

    summerland = discord.Embed(title="Summerland 2024")

    summerland.add_field(
        name="",
        value=f"{trophy_emojis[1]} Rad Hard, Luckyzhoulji, Natoh, Centac, rad soft, Eboj111, Zezimas pimp, Pup in a Cup, Auzty, Inri, L indsey",
        inline=False,
    )

    summerland.set_footer(text="June 1st, 2024")

    summerland.add_field(
        name="",
        value="https://discord.com/channels/847313025919746129/847313574040305704/1253131324483567698\n",
    )

    summerland.set_image(url="https://i.imgur.com/RT1AlJj.png")

    trickortreat = discord.Embed(title="Trick or Treat 2024")

    trickortreat.add_field(
        name="",
        value=f"{trophy_emojis[1]} Natoh, Centac, Teddy Bauer, zezimas pimp, Pawrie, Smartpants77, Thorn, Enza Denino, Iron Yesu, FE CEO, 3nv07",
        inline=False,
    )

    trickortreat.set_footer(text="October 25th, 2024")

    trickortreat.add_field(
        name="",
        value="https://discord.com/channels/847313025919746129/847313574040305704/1304922777924665395\n",
    )

    trickortreat.set_thumbnail(
        url="https://oldschool.runescape.wiki/images/thumb/Magical_pumpkin_%28garden%29_built.png/300px-Magical_pumpkin_%28garden%29_built.png?cf101"
    )

    trickortreat.set_image(url="https://i.imgur.com/0g6k1qE.png")

    duobingo = discord.Embed(title="Tale of Two Cats Duo Bingo (2025)")

    duobingo.add_field(
        name="",
        value=f"{trophy_emojis[1]} MvM Sensei, Shadow Elves",
        inline=False,
    )

    duobingo.set_footer(text="March 7th, 2025")

    duobingo.add_field(
        name="",
        value="https://discord.com/channels/847313025919746129/847313574040305704/1350512109334823034\n",
    )

    duobingo.set_image(url="https://i.imgur.com/VAjJRaA.png")

    skw = discord.Embed(title="Super Kitty World (2025)")

    skw.add_field(
        name="",
        value=f"{trophy_emojis[1]} Pot PvM, itzfluffy72, Scampr, Shadow Elves, Pot Tequila, Pot Cannabis, Star Mew, Am eer, Pot Latinas, Voteyes2pvp, Lilpaleo, Meowmiix, Pot Tacos, Meowskeys, Lilliann, Big Vorki, padingy, 3nv07",
        inline=False,
    )

    skw.set_footer(text="August 14th, 2025")

    skw.add_field(
        name="",
        value="https://discord.com/channels/847313025919746129/847313574040305704/1405605880317083718\n",
    )

    skw.set_image(url="https://i.imgur.com/KxfBeG1.jpeg")

    garden = discord.Embed(title="Enchanted Garden (2026)")

    garden.add_field(
        name="",
        value=f"{trophy_emojis[1]} Pot Tequila, MvM Sensei, itzfluffy72, Cripz, Shadow Elves, Scampr, Anhooter, VoteYes2PvP, Lilpaleo, Pot Tacos, Banhammering, Big Nerg, Pot Latinas, Meowmiix, Padingy, Fe Ursus, Chirm, Lightmaige, Boob Ay",
        inline=False,
    )

    garden.set_footer(text="March 19th, 2026")

    garden.add_field(
        name="",
        value="https://discord.com/channels/847313025919746129/847313574040305704/1484326399115399168\n",
    )

    garden.set_image(url="https://i.imgur.com/YHcLWJU.jpeg")

    embeds.append(firstbingo_embed)
    embeds.append(candyland_embed)
    embeds.append(snakes_embed)
    embeds.append(battle_gods)
    embeds.append(blackcatbingo)
    embeds.append(darts)
    embeds.append(summerland)
    embeds.append(trickortreat)
    embeds.append(duobingo)
    embeds.append(skw)
    embeds.append(garden)

    return embeds


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
