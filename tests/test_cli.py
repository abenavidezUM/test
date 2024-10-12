# test_cli.py

import unittest
from unittest.mock import patch
from game.cli import CLI

class TestCLI(unittest.TestCase):
    def setUp(self):
        self.cli = CLI()

    @patch('builtins.input', side_effect=['1', 'E2', 'E4', '2'])
    @patch('os.system')
    def test_start_game(self, mock_os_system, mock_input):
        with patch('cli.CLI.clear_terminal'):
            self.cli.menu()
            self.assertEqual(self.cli.chess_game.turn, "BLACK")

    @patch('builtins.input', side_effect=['2'])
    def test_exit_game(self, mock_input):
        with patch('cli.CLI.clear_terminal'):
            self.cli.menu()
            self.assertEqual(self.cli.chess_game.turn, "WHITE")  # Game didn't start

    @patch('builtins.input', side_effect=['1', 'E2', 'E5', '3'])
    @patch('os.system')
    def test_invalid_move_and_resign(self, mock_os_system, mock_input):
        with patch('cli.CLI.clear_terminal'):
            self.cli.menu()
            # Since the move is invalid, turn should still be WHITE
            self.assertEqual(self.cli.chess_game.turn, "WHITE")

    @patch('builtins.input', side_effect=['1', 'E2', 'E4', '2', 'Y'])
    @patch('os.system')
    def test_draw_offer_accepted(self, mock_os_system, mock_input):
        with patch('cli.CLI.clear_terminal'):
            self.cli.menu()
            # Game should end in a draw

if __name__ == '__main__':
    unittest.main()
