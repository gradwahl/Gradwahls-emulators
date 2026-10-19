# 🎮 Gradwahl's Emulators — PS5 Homebrew Catalog

A curated, emulator-only homebrew catalog for **[PS5 Library](https://github.com/deox1111/ps5-library)**, inspired by the organisation of [evoX-CoreOS](https://github.com/nexgen999/evoX-CoreOS). Most downloads point to developers' **original GitHub release assets**. Exception: the user-supplied PS5SX3 test archive is hosted in this repository's `v7.1` release; its upstream origin and redistribution rights have not been independently confirmed. The catalog itself contains no games, ROMs, BIOS, firmware or keys; the separately hosted PS5SX3 v7.1 release claims to include a PS3 update file. Do not redistribute Sony firmware without permission.

> [!IMPORTANT]
> This catalog lists community software, not guaranteed one-click installers. Some projects require a separate helper ELF, a Homebrew Launcher, purchased software, or other manual setup. Read the upstream instructions before running them.

## 🔗 Add to PS5 Library

1. Open **Settings → Catalogs → Add catalog** in PS5 Library.
2. Add the following raw JSON URL (no access key needed for a public catalog).
3. Select **Add catalog** (or **Refresh all** if it was already added).

The catalogue declares its display name as **Gradwahls Source** using the root JSON `name` field. **Note:** PS5 Library may still show `raw.githubusercontent.com` if its current UI labels sources by hostname rather than reading catalogue names. In that case, changing the visible label requires a PS5 Library update; the catalogue URL and nine emulator entries still work.

```text
https://raw.githubusercontent.com/gradwahl/Gradwahls-emulators/main/catalog.json
```

**Castation is now listed as a *manual-download* emulator in PS5 Library** using the developer's official source metadata title ID `PPSA50003`. Its published ZIP is an ELF-based Homebrew Launcher app, **not** a native title package, so PS5 Library must not be treated as its installer. Download the ZIP, extract the `Castation/` folder into `/data/homebrew/`, and launch it with Homebrew Launcher. The other catalogue entries remain available. If tapping Castation still opens a different game, that is a PS5 Library navigation issue rather than a bad Castation release URL.

The public PS5 Library catalog is also at [`json/emulators.json`](json/emulators.json), which is identical to `catalog.json`. Do **not** add both unless you want duplicate entries.

## 🕹️ Emulator collection

| Emulator | System | Version | Project | Setup |
| --- | --- | --- | --- | --- |
| RetroArch PS5 | Multi-system | v3.0.0-beta-3 | [Source](https://github.com/mihawk-99/PS5_RetroArch) | PS5 title folder; ShadowMountPlus |
| Castation | Dreamcast | v0.4.0 | [Source](https://github.com/BrinooTk/castation) | **Download-only** — manual Homebrew Launcher installation |
| Porpoise (Dolphin) | GameCube / Wii | v3.0 | [Source](https://github.com/elripalda/Porpoise-Dolphin-Emulator-for-PS5) | PS5 title folder |
| PS5SX2 (PCSX2) | PlayStation 2 | 2.10 (`vk-285-171`) | [Source](https://github.com/Swordpdf/PS5SX2/releases/tag/vk-285-171) | **Download-only/manual install** — two folder destinations, helper and own PS2 BIOS |
| PS5SX3 (RPCS3) | PlayStation 3 | v7.1 | [User-hosted 7z](https://github.com/gradwahl/Gradwahls-emulators/releases/tag/v7.1) | Experimental title folder; separate no-data-mount helper; upstream and firmware redistribution rights unverified |
| PS5X360 | Xbox 360 | v0.6.0 | [Source](https://github.com/BrinooTk/PS5X360) | PS5 title folder; experimental |
| XPSemu | Original Xbox | Alpha-2.1 | [Source](https://github.com/ZiZc3/XPSemu) | Separate `helper.elf` and own BIOS/MCPX |
| PICO-8 PS5 | Fantasy console | v0.1.2 | [Source](https://github.com/RafaelNGP/pico8-ps5) | Own licensed PICO-8 Linux files |
| Ruffle Flash PS5 | Flash / SWF | 1.2.0 | [Source](https://github.com/ZiZc3/Ruffle-Flash-PS5) | Separate `helper.elf` |

### Extra files / prerequisites

- **Castation:** listed in PS5 Library for discoverability/download, but its archive contains an ELF-based Homebrew Launcher app, **not** a normal PS5 title. Extract it to `/data/homebrew/Castation`, then launch via Homebrew Launcher. [Instructions](https://github.com/BrinooTk/castation#installing).
- **PS5SX2 (PlayStation 2):** download the [official PS5SX2 2.10 ZIP](https://github.com/Swordpdf/PS5SX2/releases/download/vk-285-171/PS5SX2-vk-285-171.zip) in PS5 Library, but **install manually**: it contains TWO top-level folders requiring different destinations. Copy **`PPSA99203/` to `/data/homebrew/PPSA99203/`** and **`PCSX2/` to `/data/PCSX2/`**. Keep the complete contents of each folder and avoid extra nesting. Place your PS2 BIOS dumped from your own console in `/data/PCSX2/bios/` and game backups in `/data/PCSX2/games/`. Load kstuff, then ShadowMount+, then **exactly one** PS5SX2 helper. The [standard helper `PS5SXHelper.elf`](https://github.com/Swordpdf/PS5SX2/releases/download/vk-285-171/PS5SXHelper.elf) is the upstream default and is in [our Payload Manager catalogue](payloads.json); the existing no-data-mount variant is an alternative for **ShadowMount+ 1.7-beta5fix1+**. Never load both, and reboot before switching. If launch shows `CE-107750-0`, check title folder and `eboot.bin` permissions (usually **755**). **Remove PS2 discs before shutdown** to avoid a developer-reported kernel panic. [Official setup/release notes](https://github.com/Swordpdf/PS5SX2/releases/tag/vk-285-171).
- **PS5SX3 (PlayStation 3):** `v7.1` is a 234 MB user-hosted `.7z` archive; PS5 Library supports `.7z` extraction. The GitHub release notes state that a **PS3 update file was added**, but the archive's internal contents and ability to install firmware have **not been independently verified**. Extract `PPSA99303/` to `/data/homebrew/PPSA99303/`, then use compatible ShadowMount+ and [the matching no-data-mount ELF in Payload Manager](payloads.json). Title ID `PPSA99303` is shared with other homebrew and may confuse PS5 Library. Obtain PS3 firmware from [Sony's official PS3 update site](https://www.playstation.com/en-gb/support/hardware/ps3/system-software/), and **do not redistribute Sony's firmware without permission**. Original developer and distribution rights for this build remain unverified.
- **XPSemu:** install the ZIP title folder **and** separately obtain/load [the matching helper.elf](https://github.com/ZiZc3/XPSemu/releases/download/Alpha-2.1/helper.elf) with kstuff. Your own Xbox BIOS and MCPX dumps are required. [Instructions](https://github.com/ZiZc3/XPSemu#installation).
- **Ruffle Flash PS5:** install the ZIP title folder **and** separately obtain/load [the matching helper.elf](https://github.com/ZiZc3/Ruffle-Flash-PS5/releases/download/1.2.0/helper.elf) with kstuff. [Instructions](https://github.com/ZiZc3/Ruffle-Flash-PS5#install).
- **PICO-8 PS5:** requires a legally licensed copy of PICO-8 Linux. The archive does not contain `pico8_dyn` or `pico8.dat`. [Instructions](https://github.com/RafaelNGP/pico8-ps5#installation).
- **RetroArch / Porpoise / PS5X360:** review each upstream readme and your console's firmware and homebrew setup before installing.


### Installing PS5SX2 from PS5 Library

PS5SX2 2.10 (`vk-285-171`, PS5 title ID `PPSA99203`) is available in the **Gradwahls Source** catalogue. Its on-screen **description also contains a short setup guide**. **Choose Download, not automatic installation**: the official ZIP contains **two top-level folders** with **different destinations**, which a normal single-folder installer may not handle.

1. Download [`PS5SX2-vk-285-171.zip`](https://github.com/Swordpdf/PS5SX2/releases/download/vk-285-171/PS5SX2-vk-285-171.zip) in PS5 Library or on your computer and extract it.
2. Move the complete `PPSA99203/` directory to **`/data/homebrew/PPSA99203/`**. Check that `eboot.bin`, `sce_sys/` and `sce_module/` are directly inside it, **not** within a second nested `PPSA99203` folder.
3. Move or merge the ZIP's `PCSX2/` directory into **`/data/PCSX2/`**. **If `/data/PCSX2/` already exists, back up settings, memory cards and saves; merge carefully rather than deleting/replacing your existing data.**
4. Copy your own dumped **PS2 BIOS** to `/data/PCSX2/bios/`. Put legally obtained game backups in `/data/PCSX2/games/`.
5. After a PS5 reboot, load your jailbreak/**kstuff**, then **ShadowMount+**, then **exactly one** PS5SX2 helper ELF. The upstream default is [`PS5SXHelper.elf`](https://github.com/Swordpdf/PS5SX2/releases/download/vk-285-171/PS5SXHelper.elf), which is listed as *PS5SX2 Helper (Standard)* in our [Payload Manager source](payloads.json). The no-data-mount variant (already in that feed) needs ShadowMount+ **1.7-beta5fix1 or later**. **Never load both variants in one session; reboot before switching helpers.**
6. Start PS5SX2 from the PS5 home screen. If you get **CE-107750-0**, first check permissions on `/data/homebrew/PPSA99203/`, its subfolders and `eboot.bin` (typically **755**, `rwxr-xr-x`) and verify the folder isn't nested. This is a troubleshooting tip, not a guaranteed fix for every error.

**Safety tip from the developer:** remove PS2 discs before shutting down your PS5 to avoid a possible kernel panic. This archive does **not** contain PS2 BIOS files or commercial games.

### Installing PS5SX3 from PS5 Library

PS5SX3 v7.1 is an **experimental, user-hosted PlayStation 3 (RPCS3) emulator**. The [v7.1 GitHub release](https://github.com/gradwahl/Gradwahls-emulators/releases/tag/v7.1) provides `PPSA99303.7z` (approximately 234 MB). PS5 Library supports `.7z` extraction; the on-console **PS5SX3 description includes the short installation guide**.

1. Download and unpack `PPSA99303.7z`. Put the **complete `PPSA99303/` title folder** in **`/data/homebrew/PPSA99303/`**.
2. Check that `/data/homebrew/PPSA99303/eboot.bin` and `sce_sys/` are **directly inside** that folder. Do **not** leave a double-nested path such as `PPSA99303/PPSA99303/eboot.bin`.
3. Load your jailbreak and **kstuff**, then a compatible **ShadowMount+**, then **`PS5SXHelper-no-data-mount.elf`** using [Gradwahl's Payload Manager feed](payloads.json). This helper **does not mount `/data` itself**: ShadowMount+ must provide the mount. Do not load both PS5SX helper variants in the same session.
4. Launch PS5SX3. If the PS5 displays **`CE-107750-0`** ("Can't start the game or app"), check that the **`PPSA99303/` title folder** and **`eboot.bin`** have Unix permissions **755** (`rwxr-xr-x`). Its parent/subdirectories must also be traversable. Incorrect title-folder permissions caused this exact launch error and fixing them let PS5SX3 open on a tested PS5. See the [permissions troubleshooting guide](#ps5sx3-startup-error-ce-107750-0) below.
5. **PS3 firmware:** RPCS3 uses Sony's **`PS3UPDAT.PUP`**, obtainable from [Sony's PS3 system software page](https://www.playstation.com/en-gb/support/hardware/ps3/system-software/). The v7.1 release says a PS3 update file was added, but its contents, licensing and exact installation behaviour have **not** been independently verified. Never select a PS5 system software update to install PS3 emulator firmware, and don't redistribute Sony's firmware without permission.

**Important:** `PPSA99303` may overlap with other homebrew title IDs, so check that the PS5 home-screen tile actually opens **PS5SX3**. The original author and redistribution permissions for this user-supplied test build remain unverified. The `rpcs3` data directory may not be created until the emulator successfully launches; you **do not** need to install desktop/Linux RPCS3 separately.

### PS5SX3 startup error: CE-107750-0

**Confirmed fix on a PS5:** if PS5SX3 shows **"Can't start the game or app" (CE-107750-0)** immediately after launching, check the **folder and executable permissions** before changing firmware or reinstalling RPCS3. Incorrect permissions on the extracted title folder prevented PS5SX3 from starting; correcting them allowed the app to open.

1. Using FTP (for example, FileZilla) or a file manager that can change Unix permissions, navigate to `/data/homebrew/PPSA99303/`.
2. Check the **`PPSA99303` folder itself**: set permissions to **755** (`rwxr-xr-x`). Make sure its parent directory `/data/homebrew/` is also traversable and its subdirectories (`sce_sys/`, `sce_module/`, etc.) have suitable execute/traverse permission (commonly **755**).
3. Check `/data/homebrew/PPSA99303/eboot.bin`: set permissions to **755** so it can be executed. Ordinary data files do not all need executable permission; avoid setting the whole tree to **777**.
4. Confirm the layout is `/data/homebrew/PPSA99303/eboot.bin`, **not** `/data/homebrew/PPSA99303/PPSA99303/eboot.bin`.
5. Ensure your jailbreak and kstuff are running, load a compatible **ShadowMount+**, then the **PS5SXHelper-no-data-mount.elf** payload, and try opening PS5SX3 again.

This addresses an observed permission-related startup failure, **not every possible cause** of CE-107750-0. If it still fails, check ShadowMount+ registration/logs and the actual error code. The `rpcs3` data directory may not exist until the emulator starts successfully; do not download a desktop/Linux RPCS3 binary to fix this.


No ROMs, games, commercial binaries, console keys or BIOS/firmware dumps are bundled.

## 📂 Catalog feeds

| Catalog | URL path | Purpose |
| --- | --- | --- |
| **PS5 Library emulator downloads** | [`catalog.json`](catalog.json) | Recommended main source; 9 entries including manual-install Castation and PS5SX2, plus the experimental PS5SX3 test build |
| Multi-system | [`json/categories/multi-system.json`](json/categories/multi-system.json) | RetroArch |
| Nintendo & Sega | [`json/categories/nintendo-sega.json`](json/categories/nintendo-sega.json) | Porpoise and Castation (manual-download only) |
| Xbox | [`json/categories/xbox.json`](json/categories/xbox.json) | PS5X360 and XPSemu |
| Other | [`json/categories/other.json`](json/categories/other.json) | PICO-8, Ruffle, PS5SX2 and PS5SX3 |
| Pegasus DL | [`json/pegasus_catalog.json`](json/pegasus_catalog.json) | Pegasus-compatible `packages` feed (6 titles; Castation and PS5SX2 excluded as manual-install apps, and PS5SX3 excluded owing to title-ID collision/provenance uncertainty) |

### Category catalogs

If you'd rather display separate catalog rows in PS5 Library, **add these category URLs instead of the all-emulators URL**:

```text
https://raw.githubusercontent.com/gradwahl/Gradwahls-emulators/main/json/categories/multi-system.json
https://raw.githubusercontent.com/gradwahl/Gradwahls-emulators/main/json/categories/nintendo-sega.json
https://raw.githubusercontent.com/gradwahl/Gradwahls-emulators/main/json/categories/xbox.json
https://raw.githubusercontent.com/gradwahl/Gradwahls-emulators/main/json/categories/other.json
```

PS5 Library supports up to 30 catalogs and checks public catalogs periodically. All four together are equivalent to the combined nine-entry catalog. Castation is downloadable but cannot be installed as a normal PS5 title through PS5 Library.

## 🌐 Browseable web page (optional)

`index.html` is a lightweight catalog browser with searchable cards, version information and links to the original developer releases. To publish it using GitHub Pages:

1. In your repository go to **Settings → Pages**.
2. Under **Build and deployment**, choose **Deploy from a branch**, select `main` and `/ (root)`, then save.
3. Once published the page should appear at `https://gradwahl.github.io/Gradwahls-emulators/`.

This web page is optional. **PS5 Library only needs the raw catalog JSON.**

## 🤖 Automatic update checking

The [update workflow](.github/workflows/update-catalog.yml) checks developers' latest GitHub release assets **twice per day**, and regenerates the PS5 Library, category, Pegasus and web catalog files. Castation uses `manual_only: true` (to display manual setup instructions) together with `ps5_library: true` (to include its downloadable release in PS5 Library). The generator excludes manual-install Castation and PS5SX2 from the Pegasus installable-title feed while retaining both as PS5 Library downloads. A new commit is made only when a tracked release changes. It never downloads or rehosts binaries itself; the `v7.1` PS5SX3 user-provided `.7z` archive is separately hosted as a GitHub Release asset.

To run manually: **Actions → Update emulator catalogs → Run workflow**.

On first use, GitHub may require you to enable Actions, and the repository's Actions permissions may need **Read and write permissions** for the workflow to push its updates. If the workflow cannot update, inspect the run logs.

To maintain manually, edit [`config/emulators.json`](config/emulators.json) and run:

```bash
python scripts/update_catalog.py          # regenerate all catalog formats
python scripts/update_catalog.py --check  # verify files match config
python scripts/update_catalog.py --refresh # check upstream GitHub releases
```

`config/emulators.json` is the source of truth; auto-generated JSON should not be edited directly. The updater uses Python standard library only, and keeps a pinned release when the upstream GitHub request fails or the expected asset is missing.

## 📁 Repository layout

```text
Gradwahls-emulators/
├── README.md
├── catalog.json                    # 9 PS5 Library entries; Castation/PS5SX2 manual-download
├── index.html                      # Optional GitHub Pages catalog
├── config/
│   └── emulators.json              # Authoritative emulator list
├── json/
│   ├── emulators.json
│   ├── pegasus_catalog.json        # Pegasus DL schema
│   └── categories/
│       ├── multi-system.json
│       ├── nintendo-sega.json
│       ├── xbox.json
│       └── other.json
├── data/
│   └── emulators.json              # Web page data
├── assets/
│   ├── site.css
│   ├── site.js
│   └── ps5sx3-icon0.png     # Optimised icon from user-supplied ZIP
├── scripts/
│   └── update_catalog.py
└── .github/workflows/
    └── update-catalog.yml
```

## Credits and rights

All emulators and their icons belong to their original authors. Most artwork and downloads are upstream-linked. The catalog also contains a resized icon from the user-supplied PS5SX3 ZIP, and links to the user-hosted `v7.1` archive Release. Its original author, licensing and redistribution permissions remain unverified. This fan-made catalog is independent of Sony, PS5 Library and evoX-CoreOS. The upstream repositories control their releases and licenses. No ROMs, games or BIOS are provided.
