# Changelog

## 2026-10-19 — Added clear setup instructions for seven more emulators

- Replaced long single-paragraph PS5 Library descriptions with plain-text INSTALL, BEFORE YOU PLAY, and IF IT WON'T START sections for Castation, RetroArch PS5, Porpoise, PS5X360, XPSemu, PICO-8 PS5, and Ruffle Flash PS5.
- Checked all seven installation flows against their developer READMEs and added separate detailed README guides for each.
- Highlighted Castation as a Homebrew Launcher ELF (not an installable PS5 title); appropriate title-folder destinations; game, BIOS and licensed data locations; precise ELF helper requirements; and useful upstream-specific troubleshooting.
- Regenerated source, main/mirror, category, Pegasus and website feeds together to preserve automatic-update consistency.
- All nine emulator download URLs, version/title metadata and all four Payload Manager entries remain unchanged.


## 2026-10-19 — Improved PS5SX3 PS5 Library installation description

- Reformatted the on-console PS5SX3 description with clear plain-text INSTALL, BEFORE YOU PLAY and IF IT WON'T START sections, matching the PS5SX2 style.
- Included the exact `/data/homebrew/PPSA99303/` folder path, `eboot.bin` placement, ShadowMount+ -> no-data-mount helper order, and the confirmed `CE-107750-0` permissions fix (`755`).
- Added a dedicated PS5SX3 README installation guide, with Sony PS3 firmware guidance and warnings about unverified provenance, distribution rights, and overlapping title IDs.
- Updated source configuration and generated main, mirror, Other-category and website descriptions together so scheduled updates preserve the formatting. ZIP/7z download URLs, versions and helper entries remain unchanged.


## 2026-10-19 — Improved PS5SX2 PS5 Library description layout

- Reformatted the on-console PS5SX2 description as plain text with headings, line breaks, numbered installation folder paths and short troubleshooting bullets.
- Preserved the two-folder manual-install warning, helper loading order, BIOS and games paths, permissions advice, and PS2-disc shutdown warning.
- Updated the source configuration and generated main/mirror/Other category and web feeds together so scheduled refreshes retain the wording. All download URLs, version metadata and payload helper entries are unchanged.


## 2026-10-19 — Expanded PS5SX2 setup instructions in PS5 Library and README

- Made the PS5SX2 PS5 Library description a self-contained manual-install guide, explaining both required folder destinations, BIOS/game paths, helper load order, 755 permissions and PS2 disc shutdown warning.
- Added a dedicated step-by-step PS5SX2 README section, including careful merging of `/data/PCSX2/` to preserve existing save data.
- Updated source configuration and generated main/mirror/Other category feeds and web catalogue together, so automatic catalogue regeneration retains the description.
- No changes to release download URLs, title IDs, PS5SX3 or Payload Manager helpers.


## 2026-10-19 — Added official PS5SX2 emulator and helper

- Added PS5SX2 2.10 (GitHub tag `vk-285-171`, PS5 title ID `PPSA99203`) to PS5 Library main/mirror, Other category and web catalogue.
- Linked official `PS5SX2-vk-285-171.zip` asset (18,523,969 bytes; release SHA-256 `226ac24866f0b94566c0680c3b99c0d5abfe8030723f5b28dae20af039c76963`).
- Marked PS5SX2 manual-install/download-only and excluded it from Pegasus because the ZIP has two top-level folders with separate destinations: `PPSA99203/` under `/data/homebrew/` and `PCSX2/` under `/data/`.
- Added official default PS5SX2 helper as a separate Payload Manager entry, filename `ps5sx2-helper.elf`, hash `9fa809eb10e1fe5149b2d031f55497d7b050e950ec5aec38bac7ebe1ef6da153`; the previous no-data-mount helper entry remains unchanged.
- Documented required BIOS and games paths, ShadowMount+ and helper load order, permissions troubleshooting, and PS2 disc shutdown warning.


## 2026-10-19 — Documented PS5SX3 startup permissions fix

- Added confirmed troubleshooting instructions for PS5SX3's `CE-107750-0` launch error to the README.
- Documented setting the `/data/homebrew/PPSA99303/` folder and `eboot.bin` to Unix mode `755`, checking parent/subfolder traversal permissions, avoiding nested title folders and loading ShadowMount+ before the no-data-mount helper.
- Clarified that this is one verified fix, not a universal remedy for the error code; PS5 Library catalogues and payload URLs remain unchanged.


## 2026-10-18 — Updated PS5SX3 release link to v7.1

- Switched PS5SX3 PS5 Library download from `v7/PPSA99303.zip` to `v7.1/PPSA99303.7z` in the source configuration, main and mirror catalogs, Other category and website data.
- Verified GitHub v7.1 release asset metadata: 233,951,274 bytes, SHA-256 `4ecd504bb8e1ab02ab723e18014c054949bfa71f7c2adb0aeeb61fdc116ef646` (not an independent download/hash verification).
- Confirmed PS5 Library documentation supports `.7z` archives; release notes say a PS3 update file was added, but its actual contents and licensing are not independently verified. The README cautions against redistributing Sony firmware.
- Preserved the existing no-data-mount ELF in the Payload Manager feed, all other PS5 Library entries and the Pegasus exclusions.


## 2026-10-18 — Added user-hosted PS5SX3 ZIP to PS5 Library

- Checked GitHub Release `v7` (`PS5SX3-TB7`): `PPSA99303.zip` is exactly 40,435,329 bytes and matches the previously uploaded archive SHA-256 (`b7761ebd1b50e95d446740bcb83a714df896e51dff1483023c57cb60f37b57e3`).
- Added PS5SX3/RPCS3 to PS5 Library main, mirror and Other category feeds using the verified GitHub Release asset and the archive's actual `PPSA99303` title folder/metadata.
- Added an optimised copy of the provided title icon for the entry.
- Retained the no-data-mount ELF in the separate Payload Manager feed; flagged PS5SX3 as experimental/user-provided with provenance and distribution rights unverified.
- Excluded PS5SX3 from Pegasus DL due to the reused `PPSA99303` title ID; existing six Pegasus entries remain.


## 2026-10-18 — Added PS5SX3 no-data-mount helper to Payload Manager

- Added a separate `PS5SXHelper-no-data-mount.elf` entry to the Payload Manager `payloads.json` feed as a PS5SX3 helper, based on the user's tested setup.
- Linked the original Swordpdf PS5SX2 `vk-285-171` release asset because the uploaded ELF has an identical SHA-256 (`3fd3707a2eee7cd68a3a019d3fec19e923db444dd0811d90102ddbf26398484f`).
- Documented the original PS5SX2 provenance, ShadowMount+ prerequisite and helper-loading cautions; kept existing entries unchanged.
- This change does not publish or redistribute the PS5SX3 app ZIP.


## 2026-10-18 — Fix Payload Manager helper filename collision

- Gave XPSemu and Ruffle distinct local ELF filenames (`xpsemu-helper.elf` and `ruffle-flash-helper.elf`) in `payloads.json`.
- This avoids v0.5.2 treating both payloads as installed when it detects one generic `helper.elf` filename.
- Preserved each original GitHub release download URL and its SHA-256 checksum; binary contents are unchanged.


## 2026-10-18 — Restored Castation as a manual-download entry

- Re-added Castation to the PS5 Library main and Nintendo & Sega catalogues with `title_id: PPSA50003`, from the developer's `sce_sys/param.json` source metadata.
- Confirmed the GitHub release asset `castation-0.4.0.zip`, which includes an ELF-based Homebrew Launcher app rather than an installable PS5 title.
- Marked Castation as manual-install on the website and updated the setup instructions and developer download link.
- Kept Castation out of the Pegasus DL installable-title feed and updated the generator so release refreshes preserve these rules.
- The title ID should help distinguish the entry, but PS5 Library's wrong-game navigation bug is not confirmed fixed until tested on-console.

## 2026-10-18 — Catalogue display-name metadata

- Declared `name: "Gradwahls Source"` in the main and Pegasus catalogs, and named each optional category feed.
- Updated the generator so automatic release refreshes preserve the names.
- PS5 Library may still show the host domain if it does not support displaying catalogue-provided names.
- Kept the six installable-format emulator entries unchanged.

## 2026-10-18 — Castation manual-install correction

- Excluded Castation from the PS5 Library main, mirror and Nintendo & Sega catalog feeds because it is an ELF-based Homebrew Launcher app.
- Retained Castation on the website with its upstream download and manual setup instructions.
- Marked the source configuration as `manual_only` so scheduled updates cannot accidentally re-add it to installable catalogs.
- The other six emulator download entries and the separate ELF payload feed remain unchanged.

## 2026-10-18 — Expanded emulator catalog

- Reorganised emulator feeds into system-specific PS5 Library catalogs.
- Added Pegasus DL-compatible feed and a browseable catalog web page.
- Added release update script and twice-daily GitHub Actions workflow.
- Kept all seven original upstream emulator release links; no binaries are rehosted.
- Updated all links to renamed repository `gradwahl/Gradwahls-emulators`.
