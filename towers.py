import discord
from discord import app_commands 
from random import randint
import time


class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents = discord.Intents.all())
        self.synced = False 

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced: 
            await tree.sync()
            self.synced = True
        print(f"We have logged in as {self.user}.")

client = aclient()
tree = app_commands.CommandTree(client)

@tree.command(name = 'towers', description='towers gamemode')
@app_commands.checks.has_any_role("Founder")
async def towers(interaction: discord.Interaction, round_id:str, tile_amount:int):
    if len(round_id) == 36:
        start_time = time.time()
        grid = [['❓','❓','❓'],['❓','❓','❓'],['❓','❓','❓'],['❓','❓','❓'],['❓','❓','❓'],['❓','❓','❓'],['❓','❓','❓'],['❓','❓','❓']]

        count = 0
        while count < tile_amount:
            a = randint(0,2)
            grid[count][a] = '✅'
            count += 1

        chance = randint(45,95)
        if tile_amount < 4:
                chance = chance - 15

        em = discord.Embed(color=0x0025ff)
        em.add_field(name="Grid", value="```"+grid[7][0]+grid[7][1]+grid[7][2]+"\n"+grid[6][0]+grid[6][1]+grid[6][2]+"\n"+grid[5][0]+grid[5][1]+grid[5][2]+"\n"+grid[4][0]+grid[4][1]+grid[4][2] +"\n"+ \
            grid[3][0]+grid[3][1]+grid[3][2] + "\n" + grid[2][0]+grid[2][1]+grid[2][2] + "\n" + grid[1][0]+grid[1][1]+grid[1][2] + "\n" + grid[0][0]+grid[0][1]+grid[0][2] + "```" \
                + f"**Accuracy**\n```{chance}%```\n**Round ID**\n```{round_id}```\n**Response Time:**\n```{str(int(time.time() - int(start_time)))}```")
        
        await interaction.response.send_message(embed=em)
    else:
        em = discord.Embed(color=0xff0000)
        em.add_field(name='Error', value="Invalid round id")
        await interaction.response.send_message(embed=em)


client.run('bot token')
