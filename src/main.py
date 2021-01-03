from src.model.htmlparser import ChampionHTMLParser

champion = ChampionHTMLParser('Anivia').parse()
print(vars(champion))