# Easy Rage Quit
You can easily rage quit your game using this python script. If your HP in the game goes below the threshold (configurable but set to 10 by default), the exe will quit.

I wouldn't recommend using this in online matches, but it's fun to experiment with.

## How it works
The script uses computer vision (via tesseract) to detect how much HP you have left from your in-game HUD. This is configured per game and you can find the supported games (or add new ones!) in `EXE_MAP`

For example, `python main.py csgo` will run the script for csgo on your main display.
You can also run a test file like `python main.py csgo test` if you add an image to the working directory called `csgo_test.jpg` and compare the printed health value with te image's health value.
