from fetch.fr import French
from util.authors import sample_fr_authors, sample_general_authors

class Main:
    lang = ('fr', 'it', 'pt', 'es', 'en')
    # This should be implemented in the future, as more languages will be supported
    ind = 0

    def select_language(self):
        if self.lang[self.ind] == 'fr':
            f = French()
            print('***** going through authors in French *******')
            for i in range(len(sample_fr_authors)):
                f.url_set_up(sample_fr_authors[i], self.lang[self.ind])
            print('***** going through general_authors in French ****** ')
            for j in range(len(sample_general_authors)):
                f.url_set_up(sample_general_authors[j], self.lang[self.ind])
