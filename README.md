# pyai_abalone

Python Abalone AI based on Alpha-Zero concept

## Installation

```bash
pip install ...
```

## how-to play

Two options:

### Running the class in an own script

```python

import pyai_abalone

game = pyai_abalone.Game()
```

### Run game_ai.py

After installation run the provided `game_ai.py` found in the package folder

```bash
python game_ai.py [-h] [-s <settings.json>] [-b <position>]
                  [--blue <player-type>] [--blue_mcts <integer>]
                  [--blue_depth <integer>] [--blue_probsum <float>]
                  [--yellow <player-type>] [--yellow_mcts <integer>]
                  [--yellow_depth <integer>] [--yellow_probsum <float>]
```

| option | description |
| --- | --- |
| -h, --help | show this help message and exit |
| -s <settings.json>, --settings  <settings.json> | .json-file containing the game setup. If provided, options will be primarily taken from that file. All settings not provided within the file, will be set to the other, given arguement values (or their default value if they were not specified at all) |
| -b <position>, --board <position> | chooses starting positions, available positions are: classic / standard, belgian_daisy, german_daisy, dutch_daisy, swiss_daisy, domination, pyramid, wall / the_wall (default: belgian_daisy) Note: The A.I. was mainly trained on the 'Beglian Daisy' position, so it might play much worse on the other starting positions
| --blue <player-type> | sets the player for the blue marbles to human or A.I., available options are: human, ai (default: human) |
| --blue_mcts <integer> | sets the number of Monte-Carlo tree searches performed at every move for the blue player (if it is an A.I). This drastically influences playing strength of the A.I, but also the time it needs to calculate for a move (default: 250) |
| --blue_depth <integer> | sets the depth of the MCTS search for the blue player (if it is an A.I). For every search the number of 'blue_depth' moves will be performed and the position evaluated afterwards (default: 13) |
| --blue_probsum <float> | For the root of the MCTS tree only the moves with the highest probabilities summing up to 'blue_probsum' will be considered. For all later nodes this restriction is not in place (default: 0.95)
| --yellow <player-type> | sets the player for the yellow marbles to human or A.I., available options are: human, ai (default: ai) |
| --yellow_mcts integer> | sets the number of Monte-Carlo tree searches performed at every move for the yellow player (if it is an A.I). This drastically influences playing strength of the A.I, but also the time it needs to calculate for a move (default: 250) |
| --yellow_depth <integer> | sets the depth of the MCTS search for the yellow player if it is an A.I). For every search the number of 'yewllow_depth' moves will be performed and the position evaluated afterwards (default: 13) |
| --yellow_probsum <float> | For the root of the MCTS tree only the moves with the highest probabilities summing up to 'yewllow_probsum' will be considered. For all later nodes this restriction is not in place (default: 0.95) |

## GUI

The GUI was taken and modified from [Abalone3](https://github.com/a-pineau/Abalon3) with
the consent of the author.

## Scope & limitations

This is an implementation of an Alpha-Zero style agent for Abalone. It was trained on actual games provided by ... who is running [AbalOnline](https://abal.online/). Despite the algorithm being quite sound, the code is limited by Python's general slow speed and its GIL (genral interpreter lock) which prevents performance efficient threading. Thus the whole package can be rather seen as a prove of concept. In order to at least visibly check the agent the agent was fit into the abalone implementation of ... (with his consent)

## Concept

The agent draws 

## Further improvement

As it is hard to surpass Python's GIL and even more its speed a Rust implementation of this package was produced which can be found here
