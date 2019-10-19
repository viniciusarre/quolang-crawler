from dev.fetch.fr import French
from dev.util.authors import fr_authors, general_authors


class Main:
    lang = ('fr', 'it', 'pt', 'es', 'en')
    # This should be implemented in the future, as more languages will be supported
    ind = 0

    def select_language(self):
        if self.lang[self.ind] == 'fr':
            f = French()
            print('***** going through authors in French *******')
            for i in range(len(fr_authors)):
                f.url_set_up(fr_authors[i],self.lang[self.ind])
            print('***** going through general_authors in French ****** ')
            for j in range(len(general_authors)):
                f.url_set_up(general_authors[j],self.lang[self.ind])



