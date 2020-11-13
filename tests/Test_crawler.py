import unittest
from fetch.fr import French


class TestCrawler(unittest.TestCase):

    def test_url_set_up_case01(self):
        """Test quotes, language, author and source
        return mapping with "status" as True and "result" contains data mapping
        """
        data_init = []
        author_data = []

        url_name = "Bernard_de_Clairvaux"
        language = "fr"

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

        # Run the function
        test_data = testfr.url_set_up(url_name, language, save_to_db=False,
                                      data_in=data_init, author_in=author_data)

        # Assert
        self.assertEqual(test_data["status"], True)
        self.assertEqual(test_data["result"]["language"], language_expect)
        self.assertEqual(test_data["result"]["author"], author_expect)
        self.assertEqual(test_data["result"]["url_name"], url_name)
        self.assertEqual(test_data["result"]["data"]
                         [0]["quotes"], citations_expect)
        self.assertEqual(test_data["result"]["data"]
                         [0]["source"], sources_expect)

    def test_url_set_up_case02(self):
        """Test for author data exist
        return mapping with "status" False and "result" contains empty mapping
        """
        data_init = []
        author_data = [{'_id': 1, 'language': 'fr', 'author': 'Bernard de Clairvaux', 'flag': '🇫🇷', 'url_name': 'Bernard de Clairvaux', 'data': [{'quotes': ['L’ingratitude est un vent brûlant qui déssèche pour soi la source de la bonté, la rosée de la miséricorde, les fleuves de la grâce.', '[...] il faut persuader la foi, au lieu de l’imposer par la violence. Quoiqu’il serait mieux sans doute qu’ils [les hérétiques] fussent punis par l’épée de celui qui ne la porte pas en vain, que de souffrir qu’ils en entraînassent d’autres dans leurs erreurs.'], 'source': [
            'Œuvres complètes de saint Bernard, Bernard de Clairvaux (trad. Alfred-Louis Charpentier), éd. Librairie Louis Vivès, 1867, t. 4, partie Sermons de saint Bernard, abbé de Clairvaux, sur le Cantique des cantiques, Sermon LI. L’Épouse demande que les fruits des bonnes œuvres soient aussi nombreux que les fleurs, et aussi abondants que les parfums de l’espérance. De l’espérance et de la crainte, p. 396', 'Œuvres complètes de saint Bernard, Bernard de Clairvaux (trad. Alfred-Louis Charpentier), éd. Librairie Louis Vivès, 1867, t. 4, partie Sermons de saint Bernard, abbé de Clairvaux, sur le Cantique des cantiques, Sermon LXVI. Erreur des hérétiques touchant le mariage, le baptême des enfants, le purgatoire, les prières pour les défunts, l’invocation des saints, p. 479-480']}]}]

        url_name = "Bernard_de_Clairvaux"
        language = "fr"

        # Make an instance
        testfr = French()

        # Run the function
        test_data = testfr.url_set_up(url_name, language, save_to_db=False,
                                      data_in=data_init, author_in=author_data)

        # Assert
        self.assertEqual(test_data["status"], False)
        self.assertEqual(test_data["result"], {})


if __name__ == '__main__':
    unittest.main()
