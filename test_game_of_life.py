import logging
import unittest

import game_of_life

log = logging.getLogger(__name__)


class GameOfLifeTestCase(unittest.TestCase):
    def test_game_of_lie(self):
        self.assertTrue(game_of_life)


if __name__ == "__main__":
    unittest.main()
