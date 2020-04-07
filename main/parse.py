import requests
from bs4 import BeautifulSoup as bs


response = requests.get('https://www.hltv.org/matches')


soup = bs(response.text, 'lxml')


class MatchParser():
    days_matches = []


    def get_matches_in_dicts(self):
        for match_day in soup.findAll('div', {'class': 'match-day'}):
            for match in match_day.findAll('div', {'class': 'match'}):
                selected_match = []
                for child in match.recursiveChildGenerator():
                    if child.name == 'td':
                        selected_match.append(child.text.strip())
                self.days_matches.append({match_day.find('span', {'class': 'standard-headline'}).text: selected_match})
    

    def return_matches_in_dicts(self):
        return(self.days_matches)


    def print_matches(self):
        for i in self.days_matches:
            for j, k in i.items():
                print(j + ' ' + ' | '.join(k))


if __name__ == "__main__":
    MatchParser.get_matches_in_dicts(MatchParser)
    MatchParser.print_matches(MatchParser)
