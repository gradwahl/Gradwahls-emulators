# 🎮 Gradwahl's Emulators — PS5 Homebrew Catalog

A curated, emulator-only homebrew catalog for **[PS5 Library](https://github.com/deox1111/ps5-library)**, inspired by the organisation of [evoX-CoreOS](https://github.com/nexgen999/evoX-CoreOS). All downloads point to developers' **original GitHub release assets**. This repository does not mirror binaries or include games, ROMs, BIOS, firmware or keys.

> [!IMPORTANT]
> This catalog lists community software, not guaranteed one-click installers. Some projects require a separate helper ELF, a Homebrew Launcher, purchased software, or other manual setup. Read the upstream instructions before running them.

## 🔗 Add to PS5 Library

1. Open **Settings → Catalogs → Add catalog** in PS5 Library.
2. Add the following raw JSON URL (no access key needed for a public catalog).
3. Select **Add catalog** (or **Refresh all** if it was already added).

The catalogue declares its display name as **Gradwahls Source** using the root JSON `name` field. **Note:** PS5 Library may still show `raw.githubusercontent.com` if its current UI labels sources by hostname rather than reading catalogue names. In that case, changing the visible label requires a PS5 Library update; the catalogue URL and six emulator entries still work.

```text
https://raw.githubusercontent.com/gradwahl/Gradwahls-emulators/main/catalog.json
```

**Castation is website-only:** it requires a separate ELF Homebrew Launcher and does not belong in the installable PS5 Library catalog. It remains available with its original download link and installation guide on the [web catalogue](https://gradwahl.github.io/Gradwahls-emulators/). The six other emulator entries are unchanged.

The public PS5 Library catalog is also at [`json/emulators.json`](json/emulators.json), which is identical to `catalog.json`. Do **not** add both unless you want duplicate entries.

## 🕹️ Emulator collection

| Emulator | System | Version | Project | Setup |
| --- | --- | --- | --- | --- |
| RetroArch PS5 | Multi-system | v3.0.0-beta-3 | [Source](https://github.com/mihawk-99/PS5_RetroArch) | PS5 title folder; ShadowMountPlus |
| Castation | Dreamcast | v0.4.0 | [Source](https://github.com/BrinooTk/castation) | **Website only** — manual Homebrew Launcher installation |
| Porpoise (Dolphin) | GameCube / Wii | v3.0 | [Source](https://github.com/elripalda/Porpoise-Dolphin-Emulator-for-PS5) | PS5 title folder |
| PS5X360 | Xbox 360 | v0.6.0 | [Source](https://github.com/BrinooTk/PS5X360) | PS5 title folder; experimental |
| XPSemu | Original Xbox | Alpha-2.1 | [Source](https://github.com/ZiZc3/XPSemu) | Separate `helper.elf` and own BIOS/MCPX |
| PICO-8 PS5 | Fantasy console | v0.1.2 | [Source](https://github.com/RafaelNGP/pico8-ps5) | Own licensed PICO-8 Linux files |
| Ruffle Flash PS5 | Flash / SWF | 1.2.0 | [Source](https://github.com/ZiZc3/Ruffle-Flash-PS5) | Separate `helper.elf` |

### Extra files / prerequisites

- **Castation:** listed on the website but **not in PS5 Library feeds**. Its archive contains an ELF-based Homebrew Launcher app, not a normal PS5 title. Extract it to `/data/homebrew/Castation`, then launch via Homebrew Launcher. [Instructions](https://github.com/BrinooTk/castation#installing).
- **XPSemu:** install the ZIP title folder **and** separately obtain/load [the matching helper.elf](https://github.com/ZiZc3/XPSemu/releases/download/Alpha-2.1/helper.elf) with kstuff. Your own Xbox BIOS and MCPX dumps are required. [Instructions](https://github.com/ZiZc3/XPSemu#installation).
- **Ruffle Flash PS5:** install the ZIP title folder **and** separately obtain/load [the matching helper.elf](https://github.com/ZiZc3/Ruffle-Flash-PS5/releases/download/1.2.0/helper.elf) with kstuff. [Instructions](https://github.com/ZiZc3/Ruffle-Flash-PS5#install).
- **PICO-8 PS5:** requires a legally licensed copy of PICO-8 Linux. The archive does not contain `pico8_dyn` or `pico8.dat`. [Instructions](https://github.com/RafaelNGP/pico8-ps5#installation).
- **RetroArch / Porpoise / PS5X360:** review each upstream readme and your console's firmware and homebrew setup before installing.

No ROMs, games, commercial binaries, console keys or BIOS/firmware dumps are bundled.

## 📂 Catalog feeds

| Catalog | URL path | Purpose |
| --- | --- | --- |
| **Installable-format emulator downloads (PS5 Library)** | [`catalog.json`](catalog.json) | Recommended main source; 6 titles |
| Multi-system | [`json/categories/multi-system.json`](json/categories/multi-system.json) | RetroArch |
| Nintendo & Sega | [`json/categories/nintendo-sega.json`](json/categories/nintendo-sega.json) | Porpoise (Castation is website-only) |
| Xbox | [`json/categories/xbox.json`](json/categories/xbox.json) | PS5X360 and XPSemu |
| Other | [`json/categories/other.json`](json/categories/other.json) | PICO-8 and Ruffle |
| Pegasus DL | [`json/pegasus_catalog.json`](json/pegasus_catalog.json) | Pegasus-compatible `packages` feed (6 titles; Castation excluded because no PS5 title ID) |

### Category catalogs

If you'd rather display separate catalog rows in PS5 Library, **add these category URLs instead of the all-emulators URL**:

```text
https://raw.githubusercontent.com/gradwahl/Gradwahls-emulators/main/json/categories/multi-system.json
https://raw.githubusercontent.com/gradwahl/Gradwahls-emulators/main/json/categories/nintendo-sega.json
https://raw.githubusercontent.com/gradwahl/Gradwahls-emulators/main/json/categories/xbox.json
https://raw.githubusercontent.com/gradwahl/Gradwahls-emulators/main/json/categories/other.json
```

PS5 Library supports up to 30 catalogs and checks public catalogs periodically. All four together are equivalent to the combined six-entry catalog. Castation is not included in any PS5 Library feed.

## 🌐 Browseable web page (optional)

`index.html` is a lightweight catalog browser with searchable cards, version information and links to the original developer releases. To publish it using GitHub Pages:

1. In your repository go to **Settings → Pages**.
2. Under **Build and deployment**, choose **Deploy from a branch**, select `main` and `/ (root)`, then save.
3. Once published the page should appear at `https://gradwahl.github.io/Gradwahls-emulators/`.

This web page is optional. **PS5 Library only needs the raw catalog JSON.**

## 🤖 Automatic update checking

The [update workflow](.github/workflows/update-catalog.yml) checks developers' latest GitHub release assets **twice per day**, and regenerates the PS5 Library, category, Pegasus and web catalog files. The `manual_only` flag in `config/emulators.json` prevents Castation from reappearing in PS5 Library feeds after updates. A new commit is made only when a tracked release changes. It never downloads or rehosts the emulator binaries.

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
├── catalog.json                    # 6 PS5 Library entries; Castation website-only
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
│   └── site.js
├── scripts/
│   └── update_catalog.py
└── .github/workflows/
    └── update-catalog.yml
```

## Credits and rights

All emulators and their icons belong to their original authors. The catalog hotlinks upstream artwork and original release assets; it does not copy or redistribute them. This fan-made catalog is independent of Sony, PS5 Library and evoX-CoreOS. The upstream repositories control their releases and licenses. No ROMs, games or BIOS are provided.
