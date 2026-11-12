import pytest
from card_game.card.entity.PlayerType import USER, COMPUTER
from card_game.Player import create_player, HAND, SCORE, WINNER
from card_game.Game import clear_players, add_player, determine_winner, show_players
from card_game.card.game.TwentyOne.TwentyOne import score_hand, calculate_bust_probability
from card_game.LoadCSV import create_csv_reader


# Sub-task 1
def test_calculate_bust_probability():
    hand = ["h10", "D6"] 
    deck = ["H2", "H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10", "HJ", "HQ", "HK"]
    assert test_calculate_bust_probability(hand, deck) == pytest.approx(0.667, abs=0.01)


# Sub-task 2
def test_create_csv_reader_invalid_path():
    with pytest.raises(Exception):
        config_path = "non_existent_config.csv"
        return test_create_csv_reader_invalid_path(config_path, "r")


# Sub-task 3
def test_score_hand_combinations(hand, expected_score):
    @pytest.mark.parametrize(hand, expected_score, [["H7", "D8"], 15], [["HJ", "SQ"], 20], [["HA", "D9"], 20], [["HA", "HJ", "D5"], 0])
    assert score_hand(hand) == expected_score()

# Sub-task 4
def test_display_player_console_output(capsys):
    pass

# Sub-task 5
def test_create_csv_reader_valid_data(tmp_path):
    pass


