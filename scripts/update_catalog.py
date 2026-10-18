#!/usr/bin/env python3
"""Refresh original-release URLs and generate PS5 Library / Pegasus catalogs.

Requires Python 3.10+ only. No packages, ROMs, BIOS files or ELF binaries are downloaded.
Run: python scripts/update_catalog.py [--refresh] [--check]
"""
import argparse
import json
import os
import re
import sys
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / 'config' / 'emulators.json'
BASE_URL = 'https://raw.githubusercontent.com/gradwahl/Gradwahls-emulators/main'
GROUPS = ['multi-system', 'nintendo-sega', 'xbox', 'other']

def dump_json(path, value, check=False):
    content = json.dumps(value, ensure_ascii=False, indent=2) + '\n'
    path.parent.mkdir(parents=True, exist_ok=True)
    if check:
        if not path.exists() or path.read_text(encoding='utf-8') != content:
            raise RuntimeError(f'Out of date: {path.relative_to(ROOT)}')
        return
    if not path.exists() or path.read_text(encoding='utf-8') != content:
        path.write_text(content, encoding='utf-8')
        print(f'Updated {path.relative_to(ROOT)}')

def catalog_entry(item):
    entry = {
        'id': item['id'], 'title': item['title'], 'platform': 'ps5',
        'version': item['version'],
        'size': size_str(item['size_bytes']), 'description': item['description'],
        'cover': item['cover'],
        'files': [{'url': item['release_url'], 'name': item['filename']}]
    }
    if item.get('title_id'):
        entry['title_id'] = item['title_id']
    return entry

def size_str(number):
    size = float(number)
    for suffix in ('B','KB','MB','GB','TB'):
        if size < 1000 or suffix == 'TB':
            return f'{size:.2f}{suffix}' if suffix != 'B' else f'{int(size)}B'
        size /= 1000

def latest_release(item):
    repo = item['repo']
    url = f'https://api.github.com/repos/{repo}/releases/latest'
    headers = {'Accept':'application/vnd.github+json', 'User-Agent':'Gradwahl-Emulator-Catalog/1.0', 'X-GitHub-Api-Version':'2022-11-28'}
    token = os.environ.get('GH_TOKEN') or os.environ.get('GITHUB_TOKEN')
    if token:
        headers['Authorization'] = f'Bearer {token}'
    request = Request(url, headers=headers)
    with urlopen(request, timeout=18) as response:
        release = json.load(response)
    pattern = re.compile(item['asset_regex'], re.IGNORECASE)
    assets = [a for a in release.get('assets',[]) if pattern.fullmatch(a.get('name',''))]
    if len(assets) != 1:
        raise ValueError(f'Expected 1 matching asset in {repo} {release.get("tag_name")}, found {len(assets)}')
    asset = assets[0]
    return {'version': release['tag_name'], 'filename':asset['name'], 'release_url':asset['browser_download_url'], 'size_bytes':asset['size']}

def validate(items):
    ids=set()
    for item in items:
        assert item['id'] not in ids, f'Duplicate id: {item["id"]}'
        ids.add(item['id'])
        assert item['group'] in GROUPS, item['group']
        assert item['release_url'].startswith(f'https://github.com/{item["repo"]}/releases/download/'), item['id']
        assert item['release_url'].endswith('/'+item['filename']), item['id']
        assert item['size_bytes'] > 0
        assert item['cover'].startswith('https://raw.githubusercontent.com/')

def generate(items, check=False):
    # Homebrew Launcher apps without installable PS5 titles are website-only.
    library_items = [x for x in items if not x.get('manual_only', False)]
    main = {'entries':[catalog_entry(x) for x in library_items]}
    dump_json(ROOT/'catalog.json', main, check)
    dump_json(ROOT/'json/emulators.json', main, check)
    for group in GROUPS:
        dump_json(ROOT/'json/categories'/f'{group}.json', {'entries':[catalog_entry(x) for x in library_items if x['group']==group]}, check)
    pegasus = {'name':"Gradwahl's Emulators",'packages':[]}
    for item in library_items:
        if not item.get('title_id'):
            continue  # Pegasus requires a titleId
        pegasus['packages'].append({
            'titleId':item['title_id'], 'title':item['title'], 'version':item['version'],
            'description':item['description'], 'posterUrl':item['cover'],
            'downloadSource':f'https://github.com/{item["repo"]}',
            'sizeBytes':item['size_bytes'],
            'downloadLinks':[{'name':'GitHub Releases', 'url':item['release_url']}]
        })
    dump_json(ROOT/'json/pegasus_catalog.json', pegasus, check)
    site = []
    for item in items:
        row = {k:item.get(k) for k in ['id','title','repo','title_id','category','group','system','version','size_bytes','release_url','cover','description','install_note','install_type']}
        if item.get('manual_only'):
            row['manual_only'] = True
        site.append(row)
    dump_json(ROOT/'data/emulators.json', site, check)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--refresh', action='store_true', help='Check GitHub for newer release assets')
    parser.add_argument('--check', action='store_true', help='Verify generated files match config; do not write')
    args = parser.parse_args()
    if args.refresh and args.check:
        parser.error('--refresh and --check cannot be combined')
    items = json.loads(CONFIG.read_text(encoding='utf-8'))
    validate(items)
    if args.refresh:
        failures = 0
        for item in items:
            try:
                details = latest_release(item)
                if any(item[k]!=v for k,v in details.items()):
                    print(f'{item["id"]}: {item["version"]} -> {details["version"]}')
                    item.update(details)
                else:
                    print(f'{item["id"]}: current at {item["version"]}')
            except (URLError, HTTPError, ValueError, TimeoutError, KeyError) as exc:
                failures += 1
                print(f'Warning: could not refresh {item["id"]}: {exc}', file=sys.stderr)
        if failures:
            print(f'Keeping pinned releases for {failures} project(s)', file=sys.stderr)
        CONFIG.write_text(json.dumps(items,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    generate(items, check=args.check)
    print(f'{len(items)} emulators ({sum(not x.get("manual_only", False) for x in items)} in PS5 Library); outputs {"verified" if args.check else "generated"}.')

if __name__ == '__main__':
    main()
