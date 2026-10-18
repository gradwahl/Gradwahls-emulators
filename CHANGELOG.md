# Changelog

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
