# TempGBA4PSP-Single-game

Fork of TempGBA4PSP

## What is this?
This emulator is a modified a version of TempGBA4PSP that allows to launch roms straight from the PSP Menu! It works by having a multiple instances of this emulator, each one for each game.

## Usage
- Download this emulator from the [releases tab](https://github.com/GrabowskiDev/TempGBA4PSP-Single-game/releases)
- Put you GBA game in roms folder, and name it `game.gba` (It needs to be unzipped)
  - (Note: If you're importing save file or config, put them in respective folders and also name them `game`)
- Optional: Change the icon and background picture of the PBP to mach the game (You can use [PSP Brew](https://www.brewology.com/downloads/download.php?id=5487&mcid=1) for this but there are also other programs)
  - The Main Icon can be 144x80 for rectangle sized image, or 80x80 for square GBA icons (and probably anything between 80-144x80 would work)
  - The Background image should be 480x272 (at least that's what has been working for me)
  - The Background music must be in .AT3 (You can use [this converter](https://www.modconsoles.fr/club-articles.html/pc/at9at3-converter-v23-r36/))
  - Keep in mind that the size of .AT3 combined with the size of .PMF (Animated icon) can't exceed 500KB. You may need to crop the sound.

- Drag your TempGBA folder onto your PSP memory card (into PSP/GAME folder)
- Enjoy your game!

### Development
This project was build using older SDK, specifically [This one](https://github.com/PSP-Archive/ARK-4/tree/main/contrib/PC/PSPSDK) on Ubuntu 22.04LTS

If you find any bugs or problems, feel free to address them or write me a message.
