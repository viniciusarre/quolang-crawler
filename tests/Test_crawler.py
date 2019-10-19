import unittest
import requests
from bs4 import BeautifulSoup
from dev.fetch.fr import French

class TestCrawler(unittest.TestCase):

    def test_fetch_French(self):
        """Test quotes, language, author and source
        """
        data_init = []

        url_name = "Bernard_de_Clairvaux"
        author_expect = "Bernard de Clairvaux"
        language_expect = "fr"
        citations_expect = [
            "L’ingratitude est un vent brûlant qui déssèche pour soi la source de la bonté, la rosée de la miséricorde, les fleuves de la grâce.",
            "[...] il faut persuader la foi, au lieu de l’imposer par la violence. Quoiqu’il serait mieux sans doute qu’ils [les hérétiques] fussent punis par l’épée de celui qui ne la porte pas en vain, que de souffrir qu’ils en entraînassent d’autres dans leurs erreurs."
        ]
        sources_expect = [
            "Œuvres complètes de saint Bernard, Bernard de Clairvaux (trad. Alfred-Louis Charpentier), éd. Librairie Louis Vivès, 1867, t. 4, partie Sermons de saint Bernard, abbé de Clairvaux, sur le Cantique des cantiques, Sermon LI. L’Épouse demande que les fruits des bonnes œuvres soient aussi nombreux que les fleurs, et aussi abondants que les parfums de l’espérance. De l’espérance et de la crainte, p. 396",
            "Œuvres complètes de saint Bernard, Bernard de Clairvaux (trad. Alfred-Louis Charpentier), éd. Librairie Louis Vivès, 1867, t. 4, partie Sermons de saint Bernard, abbé de Clairvaux, sur le Cantique des cantiques, Sermon LXVI. Erreur des hérétiques touchant le mariage, le baptême des enfants, le purgatoire, les prières pour les défunts, l’invocation des saints, p. 479-480"
        ]

        # Make an instance
        testfr = French()

        # Fetch from live wikiquote
        res = requests.get("{}{}".format(testfr.url, url_name))
        html = res.text
        soup = BeautifulSoup(html, "html.parser")

        # Run the function
        test_data = testfr.fetch_data(data_init, soup, url_name)

        # Assert
        self.assertEqual(test_data["language"], language_expect)
        self.assertEqual(test_data["author"], author_expect)
        self.assertEqual(test_data["url_name"], url_name)
        self.assertEqual(test_data["data"][0]["quotes"], citations_expect)
        self.assertEqual(test_data["data"][0]["source"], sources_expect)


if __name__ == '__main__':
    unittest.main()
