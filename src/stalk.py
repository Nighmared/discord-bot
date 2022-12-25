import logging
import traceback
from typing import Optional

import discord
from discord.abc import PrivateChannel
from discord.ext.commands import Bot


IMPORTS = ()
logger = logging.getLogger("botlogger")


async def stalk(
    client: Bot, trackercolor: int, errorcolor: int, message: discord.Message
) -> tuple[int, Optional[discord.Embed]]:
    def make_date_nice(date) -> str:
        return date.strftime("`%A, %d %B %Y, %H:%M`")

    args = message.content[1:].split(" ")
    try:
        target_id = args[1]
    except IndexError:
        target_id = message.author.id
    t_id = int(target_id)
    try:
        if message.guild is None:
            raise ValueError
        try:  # id belongs to a member of the guild

            target = await message.guild.fetch_member(t_id)
            embObj = discord.Embed(
                title="Stalking | User",
                description=f"Info about {target.mention}",
                color=trackercolor,
            )
            embObj.add_field(
                name="Username", value=f"{target.name}#{target.discriminator}"
            )
            embObj.add_field(name="UID", value=target.id, inline=False)
            embObj.add_field(
                name="Account Created",
                value=make_date_nice(target.created_at),
                inline=False,
            )
            embObj.add_field(
                name="Joined Server",
                value=make_date_nice(target.joined_at),
                inline=False,
            )
            embObj.add_field(name="Is bot", value=target.bot)
            embObj.add_field(name="Highest Role", value=target.top_role.mention)
            if target.avatar is not None:
                embObj.set_image(url=target.avatar.url)
            if message.guild is not None and message.guild.icon is not None:
                embObj.set_thumbnail(url=message.guild.icon.url)
        except discord.NotFound:  # id belongs to a non-member user
            try:
                target = await client.fetch_user(t_id)
                embObj = discord.Embed(
                    title="Stalking | User",
                    description=f"Info about {target.mention}",
                    color=trackercolor,
                )
                embObj.add_field(
                    name="Username", value=f"{target.name}#{target.discriminator}"
                )
                embObj.add_field(name="UID", value=target.id, inline=False)
                embObj.add_field(
                    name="Account Created", value=make_date_nice(target.created_at)
                )
                embObj.add_field(name="Is bot", value=target.bot)
                if target.avatar is not None:
                    embObj.set_image(url=target.avatar.url)
            except discord.NotFound:  # id belongs to a channel

                try:
                    try:
                        target = await client.fetch_channel(t_id)
                    except discord.Forbidden:
                        target = list(
                            filter(
                                lambda x: x.id == t_id,
                                await message.guild.fetch_channels(),
                            )
                        )[0]
                    mention = "Some private channel?"
                    name = str(t_id)
                    if isinstance(target, PrivateChannel):
                        embObj = discord.Embed(
                            title="Stalking | Channel",
                            description=f"Info about {mention}",
                            color=trackercolor,
                        )
                        embObj.add_field(
                            name="??????", value="Private Channel doesnt give info"
                        )
                        return (0, embObj)
                    embObj = discord.Embed(
                        title="Stalking | Channel",
                        description=f"Info about {mention}",
                        color=trackercolor,
                    )
                    embObj.add_field(name="Channel Name", value=name)
                    if isinstance(target, discord.TextChannel):
                        attrs = " None "
                        if target.is_nsfw():
                            attrs = "NSFW "
                        if target.is_news():
                            attrs += " NEWS "
                        embObj.add_field(name="Special Attributes", value=str(attrs))
                        embObj.add_field(name="Topic", value=target.topic)
                        if target.category is not None:
                            embObj.add_field(
                                name="Category", value=target.category.mention
                            )

                    elif isinstance(target, discord.VoiceChannel):  # voice channel
                        embObj.add_field(name="Bitrate", value=target.bitrate)
                        embObj.add_field(name="Max User #", value=target.user_limit)
                        if target.category is not None:
                            embObj.add_field(
                                name="Category", value=target.category.mention
                            )

                    elif isinstance(
                        target, discord.CategoryChannel
                    ):  # category channel
                        embObj.add_field(name="NSFW", value=target.is_nsfw())
                        txt_chans = [x.mention for x in target.text_channels]
                        vic_chans = [x.mention for x in target.voice_channels]
                        if len(txt_chans) > 0:
                            embObj.add_field(name="Text Channels", value=txt_chans)
                        if len(vic_chans) > 0:
                            embObj.add_field(name="Voice Channels", value=vic_chans)

                    embObj.add_field(name="Server", value=target.guild.name)
                    embObj.add_field(
                        name="Created at", value=make_date_nice(target.created_at)
                    )
                    if target.guild.icon is not None:
                        embObj.set_thumbnail(url=target.guild.icon.url)

                except discord.NotFound:  # guild
                    try:
                        target = await client.fetch_guild(t_id)
                        if target is None:
                            raise ValueError
                        embObj = discord.Embed(
                            title="Stalking | Server",
                            description=f"Info about {target.name}",
                            color=trackercolor,
                        )
                        embObj.add_field(
                            name="Boosts", value=target.premium_subscription_count
                        )
                        embObj.add_field(name="Boost Level", value=target.premium_tier)
                        embObj.add_field(
                            name="Description",
                            value=target.description,
                            inline=False,
                        )
                        embObj.add_field(
                            name="Created at",
                            value=make_date_nice(target.created_at),
                            inline=False,
                        )
                        if target.owner:
                            embObj.add_field(
                                name="Owner",
                                value=(
                                    await client.fetch_user(target.owner.id)
                                ).mention,
                            )
                        embObj.add_field(
                            name="Max Members", value=f"{target.max_members} "
                        )

                        role_str = ""
                        for role in target.roles[::-1]:
                            if len(role_str + role.mention) > 512:
                                role_str += "..."
                                break
                            role_str += f"{role.mention} "
                        embObj.add_field(name="Roles", value=role_str, inline=False)
                        if message.guild.icon is not None:
                            embObj.set_thumbnail(url=message.guild.icon.url)
                        if message.guild.banner is not None:
                            embObj.set_image(url=message.guild.banner.url)
                    except (discord.NotFound, discord.Forbidden, ValueError):  # role?
                        try:
                            target = list(
                                filter(lambda x: x.id == t_id, message.guild.roles)
                            )[0]
                        except IndexError:
                            target = None
                        if target is None:
                            embObj = discord.Embed(
                                title="Stalking | ...what is this?",
                                description=f"Couldnt find out what {target_id} represents.. sawry\n Probably a Server the bot has no access to",
                                color=errorcolor,
                            )
                        else:  # yup role
                            embObj = discord.Embed(
                                title="Stalking | Role",
                                description=f"Info about {target.mention}",
                                color=trackercolor,
                            )
                            embObj.add_field(name="Color", value=str(target.color))
                            embObj.add_field(name="Pingable", value=target.mentionable)
                            embObj.add_field(
                                name="Default role", value=target.is_default()
                            )
                            embObj.add_field(name="Position", value=target.position)
                            embObj.add_field(
                                name="Created at",
                                value=make_date_nice(target.created_at),
                                inline=False,
                            )
                            if message.guild.icon is not None:
                                embObj.set_thumbnail(url=message.guild.icon.url)

        return (0, embObj)
    except Exception as e:
        traceback.print_exc()
        embObj = discord.Embed(
            title="Stalking",
            description=str(e) + str(type(e)),
            color=errorcolor,
        )
        return (1, embObj)
