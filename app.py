# nba_api
from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.endpoints import commonplayerinfo
from nba_api.stats.endpoints import commonplayerinfo

# Basic Request
# Anthony Davis
career = playercareerstats.PlayerCareerStats(player_id='203076')
print(career.get_data_frames()[0])
