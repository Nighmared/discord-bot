import discord

IMPORTS = ()


async def stalk(message:discord.Message)->tuple:
	try:
		args = message.content[1:].split(" ")
		target_id = args[1]
		target_user = await message.guild.fetch_member(target_id)
		embObj = discord.Embed(title="Stalking", description =f"Info about {target_user.mention}")
		embObj.add_field(name="Username",value=f"{target_user.name}#{target_user.discriminator}")
		embObj.add_field(name="UID", value=target_user.id)
		embObj.add_field(name="Account Created", value=target_user.created_at)
		embObj.add_field(name="Joined Server",value=target_user.joined_at)
		embObj.set_image(url=target_user.avatar_url)
		return (0, embObj)
	except Exception as e:
		embObj = discord.Embed(title="Stalking", description = str(e))
		return (1,embObj)

