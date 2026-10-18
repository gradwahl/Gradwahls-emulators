# Changelog

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
