import pandas as pd
import requests
import datetime
import json
from bs4 import BeautifulSoup as bs


response = requests.get('https://www.hltv.org/matches')
soup = bs(response.text, 'lxml')


class MatchParser():
    ids = []

    timestamps = []
    datetime_formatted_cet = []
    datetime_formatted_msc = []

    teams_total = []
    teams_left = []
    teams_right = []

    events = []

    match_maps = []


    final_match_list = []


    team_counter = 0

    def format_data(self):
        for match in soup.findAll('div', {'class': 'match'}):
            if match.find('div', {'class': 'time'}) and match.find('td', {'class': 'vs'}):
                for time_tag in match.findAll('div', {'class': 'time'}):
                    self.timestamps.append(time_tag['data-unix'])


        for stamp in self.timestamps:
            timestamp = datetime.datetime.fromtimestamp(int(stamp[:10]))
            self.datetime_formatted_cet.append(timestamp.strftime('%Y-%m-%d %H:%M'))
            self.datetime_formatted_msc.append((timestamp + datetime.timedelta(hours=3)).strftime('%H:%M'))


        for team in soup.findAll('div', {'class': 'team'}):
            if '\n' in team:
                continue
            self.team_counter += 1
            self.teams_total.append(team.text)
        self.team_counter -= 1

        team_index = 0
        while team_index < self.team_counter:
            self.teams_left.append(self.teams_total[team_index])
            self.teams_right.append(self.teams_total[team_index+1])
            team_index += 2

        
        for i in range(self.team_counter):
            self.ids.append(i)


        for event in soup.findAll('span', {'class': 'event-name'}):
            self.events.append(event.text)


        for match_map in soup.findAll('div', {'class': 'map-text'}):
            self.match_maps.append(match_map.text)


        for index, date_cet, date_msc, team_a, team_b, event, match_type in zip(
            self.ids, self.datetime_formatted_cet, self.datetime_formatted_msc, self.teams_left, self.teams_right, self.events, self.match_maps):
            self.final_match_list.append({
                'index': index, 'date_cet': date_cet, 'date_msc': date_msc, 'team_a': team_a, 'team_b': team_b, 'event': event, 'match_type': match_type})


    def pandas_df_to_json(self):
        df = pd.DataFrame(self.final_match_list)
        formatted_dict = df.to_dict(orient='records')
        return formatted_dict


if __name__ == "__main__":
    parser = MatchParser()
    parser.format_data()
    print(parser.pandas_df_to_json())