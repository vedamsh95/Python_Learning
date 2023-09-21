import numpy as np
import pandas as pd
from nbapy import game
from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamefinder
import matplotlib.pyplot as plt


def one_dict(list_dict):
    keys = list_dict[0].keys()
    out_dict = {key: [] for key in keys}
    for dict_ in list_dict:
        for key, value in dict_.items():
            out_dict[key].append(value)
    return out_dict

pd.set_option('display.max_columns', None)
nba_api = teams.get_teams()
df = pd.DataFrame(one_dict(nba_api))
#print(df)

df_warriors = df[df['nickname'] == 'Hawks']
#print(df_warriors)
id_warriors = df_warriors[['id']].values[0][0]
print(id_warriors)

gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=id_warriors)
games = gamefinder.get_data_frames()[0]
print(games.head())

games_home = games[games['MATCHUP'] == 'ATL vs. PHI']
games_away = games[games['MATCHUP'] == 'ATL @ DEN']

fig, ax = plt.subplots()

games_away.plot(x='GAME_DATE', y='PLUS_MINUS', ax=ax)
games_home.plot(x='GAME_DATE', y='PLUS_MINUS', ax=ax)
ax.legend(["away", "home"])
plt.show()