# Easy Rage Quit
You can easily rage quit your game using this python script. If your HP in the game goes below the threshold (configurable but set to 10 by default), the exe will quit.

## How it works
The script uses computer vision (via tesseract) to detect how much HP you have left from your in-game HUD. This is configured per game (in this case, the defaults are for a 4k monitor). You can find the supported games (or add new ones!) in `EXE_MAP`

For example, `python main.py csgo` will run the script for csgo