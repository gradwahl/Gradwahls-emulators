# Gradwahl's Sources — PS5 Emulators

Community emulators catalogue for [deox1111/ps5-library](https://github.com/deox1111/ps5-library), maintained independently. The catalogue links to original authors' GitHub release assets. No ROMs, BIOS, games, firmware, keys or console-specific files are hosted here.

## Install catalogue in PS5 Library

1. Upload `catalog.json` to the **main** branch of this GitHub repository.
2. Open **PS5 Library → Settings → Catalogs → Add catalog**.
3. Paste the raw URL below (no access key required for a public repository).
4. Choose **Add catalog**. Then check the Store or use **Refresh all**.

```text
https://raw.githubusercontent.com/gradwahl/Gradwahls-Sources/main/catalog.json
```

## Included emulators

| Emulator | System | Original project | Release |
|---|---|---|---|
| RetroArch PS5 | Multi-system | [mihawk-99/PS5_RetroArch](https://github.com/mihawk-99/PS5_RetroArch) | v3.0.0-beta-3 |
| Castation | Sega Dreamcast | [BrinooTk/castation](https://github.com/BrinooTk/castation) | v0.4.0 |
| Porpoise | GameCube / Wii | [elripalda/Porpoise-Dolphin-Emulator-for-PS5](https://github.com/elripalda/Porpoise-Dolphin-Emulator-for-PS5) | v3.0 |
| PS5X360 | Xbox 360 | [BrinooTk/PS5X360](https://github.com/BrinooTk/PS5X360) | v0.6.0 |
| XPSemu | Original Xbox | [ZiZc3/XPSemu](https://github.com/ZiZc3/XPSemu) | Alpha-2.1 |
| PICO-8 PS5 | PICO-8 | [RafaelNGP/pico8-ps5](https://github.com/RafaelNGP/pico8-ps5) | v0.1.2 |
| Ruffle Flash PS5 | Flash / SWF | [ZiZc3/Ruffle-Flash-PS5](https://github.com/ZiZc3/Ruffle-Flash-PS5) | 1.2.0 |

## Important caveats

- Entries are **links to downloads, not a guarantee of automatic installation** or compatibility with your firmware or payload versions. Homebrew setup (such as etaHEN, kstuff and ShadowMountPlus) is generally required.
- **Castation** is an ELF-based **Homebrew Launcher** app rather than a native home-screen title. Its ZIP may need manual extraction to `/data/homebrew/Castation/`, and launch through Homebrew Launcher; PS5 Library may not automatically install it.
- **XPSemu** and **Ruffle Flash** each require their own upstream `helper.elf` separately loaded through kstuff. Helpers are intentionally not mixed into the main download file lists, because PS5 Library expects multiple `files` items to be parts of one download, not independent prerequisites.
- **PICO-8 PS5** needs a separately licensed PICO-8 Linux installation (`pico8_dyn` and `pico8.dat`), copied manually.
- **RetroArch** recommends ShadowMountPlus 1.7beta4 or newer, and **Porpoise** requires it for a supported install.
- **PS5X360** and **XPSemu** are experimental with limited compatibility. None of these entries contains games, ROMs, keys or firmware.

## Updating releases

Releases are currently pinned as checked on **18 October 2026**. To update an emulator, edit the matching entry in `catalog.json`, changing `version`, `size`, `files[].url`, and `files[].name` to match the new upstream release. PS5 Library checks public catalogues roughly every 10 minutes or on **Refresh all**.

Catalog format documentation: [PS5 Library — Make your own catalog](https://github.com/deox1111/ps5-library#make-your-own-catalog).
