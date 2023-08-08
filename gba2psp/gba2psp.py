#!/usr/bin/env python
# coding: utf-8
#

import argparse
import io
import os
import requests
import shutil
import struct
import subprocess
import sys
import tempfile
import zipfile

from PIL import Image, ImageDraw, ImageFont
from pytube import YouTube
from pytube.contrib.search import Search

from gamedb import games
from riff import copy_riff, create_riff, parse_riff


def read_eboot(f):
    def read_blob(f, eboot, i, name):
        if i == 7:
            f.seek(offsets[i])
            eboot[name] = f.read()
            return
        if offsets[i] < offsets[i+1]:
            f.seek(offsets[i])
            eboot[name] = f.read(offsets[i+1] - offsets[i])
    
    buf = f.read(0x28)
    eboot = {}
    eboot['magic'] = struct.unpack_from('<I', buf, 0)[0]
    if eboot['magic'] != 0x50425000:
        print('Not an EBOOT')
        return None
    
    eboot['version'] = struct.unpack_from('<I', buf, 0x04)[0]
    offsets = struct.unpack_from('<IIIIIIII', buf, 0x08)
    read_blob(f, eboot, 0, 'param.sfo')
    read_blob(f, eboot, 1, 'icon0.png')
    read_blob(f, eboot, 2, 'icon1.png')
    read_blob(f, eboot, 3, 'pic0.png')
    read_blob(f, eboot, 4, 'pic1.png')
    read_blob(f, eboot, 5, 'snd0.at3')
    read_blob(f, eboot, 6, 'data.psp')
    read_blob(f, eboot, 7, 'data.psar')
    return eboot

def write_eboot(f, eboot):
    def write_blob(f, offset, eboot, pos, name):
        buf = bytearray(4)
        struct.pack_into('<I', buf, 0, offset)
        f.seek(pos)
        f.write(buf)
        if name in eboot:
            f.seek(offset)
            f.write(eboot[name])
            return f.tell()
        return offset
        
    buf = bytearray(4)
    struct.pack_into('<I', buf, 0, eboot['magic'])
    f.write(buf)
    struct.pack_into('<I', buf, 0, eboot['version'])
    f.write(buf)
    offset = 0x28
    offset = write_blob(f, offset, eboot, 0x08, 'param.sfo')
    offset = write_blob(f, offset, eboot, 0x0c, 'icon0.png')
    offset = write_blob(f, offset, eboot, 0x10, 'icon1.png')
    offset = write_blob(f, offset, eboot, 0x14, 'pic0.png')
    offset = write_blob(f, offset, eboot, 0x18, 'pic1.png')
    offset = write_blob(f, offset, eboot, 0x1c, 'snd0.at3')
    offset = write_blob(f, offset, eboot, 0x20, 'data.psp')
    offset = write_blob(f, offset, eboot, 0x24, 'data.psar')

def get_icon0(f):
    if f[:8] == 'https://':
        ret = requests.get(f)
        print('Downloading ICON0 from', f)
        if ret.status_code != 200:
            print('Failed to download', f)
            return None
        if ret.apparent_encoding:
            icon0 = Image.open(io.BytesIO(ret.content.decode(ret.apparent_encoding)))
        else:
            icon0 = Image.open(io.BytesIO(ret.content))
    else:
        icon0 = Image.open(f)


    if icon0.size[0] / icon0.size[1] < 1.4 and icon0.size[0] / icon0.size[1] > 0.75:
        image = icon0.resize((80, 80), Image.Resampling.BILINEAR)
    else:
        image = icon0.resize((144, 80), Image.Resampling.BILINEAR)
    i = io.BytesIO()
    image.save(i, format='PNG')
    i.seek(0)
    return i.read()


def convert_snd0_to_at3(snd0, at3, duration, max_size, subdir = './'):
    print('Creating SND0.AT3')
    tmp_wav = subdir + '/SND0.WAV'
    tmp_snd0 = subdir + '/SND0.EA3'
    s = parse_riff(snd0)
    if not s:
        print('Not a WAVE file')
        return None

    while True:
        print('Creating temporary WAV file clamped to %d second duration %s' % (duration, tmp_wav))
        copy_riff(snd0, tmp_wav, max_duration_ms=duration * 1000)
        s = parse_riff(tmp_wav)
        print('Creating temporary ATRAC3 file', tmp_snd0)
        try:
            if os.name == 'posix':
                subprocess.run(['atracdenc', '--encode=atrac3', '-i', tmp_wav, '-o', tmp_snd0], check=True)
            else:
                subprocess.run(['atracdenc.exe', '--encode=atrac3', '-i', tmp_wav, '-o', tmp_snd0], check=True)
        except:
            print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\natracdenc not found.\nCan not create SND0.AT3\nPlease see README file for how to install atracdenc\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
        print('Converting EA3 to AT3 file')
        create_riff(tmp_snd0, at3, number_of_samples=int(len(s['data']['data'])/4), max_data_size=0, loop=True)
        if os.stat(at3).st_size < max_size:
            break
        # Too big. Clamp duration and try again
        duration = int(duration * 0.95 / (os.stat(at3).st_size / max_size))


def get_snd0(snd0, td):
    if snd0[:24] == 'https://www.youtube.com/':
        try:
            fn = YouTube(snd0).streams.filter(only_audio=True)[0].download(td)
        except:
            print('Failed to download', snd0)
            return None
        snd0 = fn

    if os.name == 'posix':
        subprocess.call(['ffmpeg', '-y', '-i', snd0, '-filter:a', 'atempo=0.91', '-ar', '44100', '-ac', '2', td + '/snd0_tmp.wav'])
    else:
        subprocess.call(['ffmpeg.exe', '-y', '-i', snd0, '-filter:a', 'atempo=0.91', '-ar', '44100', '-ac', '2', td + '/snd0_tmp.wav'])

    convert_snd0_to_at3(td + '/snd0_tmp.wav', td + '/SND0.AT3', 59, 500000, subdir=td)
    with open(td + '/SND0.AT3', 'rb') as i:
        return i.read()

        
def get_pic0(f):
    if f[:8] == 'https://':
        ret = requests.get(f)
        print('Downloading PIC0 from', f)
        if ret.status_code != 200:
            print('Failed to download', f)
            return None
        if ret.apparent_encoding:
            pic0 = Image.open(io.BytesIO(ret.content.decode(ret.apparent_encoding)))
        else:
            pic0 = Image.open(io.BytesIO(ret.content))
    else:
        pic0 = Image.open(f)


    # Scale it down a bit so it will not cover most of the screen
    #image = pic0.resize((310, 180), Image.Resampling.BILINEAR)
    img = pic0.resize((155, 90), Image.Resampling.BILINEAR)
    image = Image.new(img.mode, (310, 180), (0,0,0)).convert('RGBA')
    image.putalpha(0)
    image.paste(img, (72,45))

    i = io.BytesIO()
    image.save(i, format='PNG')
    i.seek(0)
    return i.read()

def get_pic1(f):
    if f[:8] == 'https://':
        ret = requests.get(f)
        print('Downloading PIC1 from', f)
        if ret.status_code != 200:
            print('Failed to download', f)
            return None
        if ret.apparent_encoding:
            pic1 = Image.open(io.BytesIO(ret.content.decode(ret.apparent_encoding)))
        else:
            pic1 = Image.open(io.BytesIO(ret.content))
    else:
        pic1 = Image.open(f)


    image = pic1.resize((480, 272), Image.Resampling.BILINEAR)
    i = io.BytesIO()
    image.save(i, format='PNG')
    i.seek(0)
    return i.read()

def read_game(game):
    if game[-4:].lower() == '.zip':
        z = zipfile.ZipFile(game)
        for f in z.namelist():
            if f[-4:].lower() == '.gba':
                with z.open(f) as zf:
                    return zf.read()
        
    with open(game, 'rb') as f:
        return f.read()

    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', action='store_true', help='Verbose')
    parser.add_argument('--psp-game-dir',
                help='Where to install the files (/PSP/GAME on your device)')
    parser.add_argument('--icon0', help='Image for ICON0')
    parser.add_argument('--pic0', help='Image for PIC0')
    parser.add_argument('--pic1', help='Image for PIC1')
    parser.add_argument('--snd0', help='Image for SND0')
    parser.add_argument('game', help='GBA image')
    args = parser.parse_args()

    if not args.psp_game_dir:
        print('Must specify --psp-game-dir')
        os._exit(1)

    td = tempfile.TemporaryDirectory(prefix='gba2psp-')

    game = read_game(args.game)
        
    game_id = bytearray(game[0xa0:0xb0])
    for i in range(16):
        if game_id[i] == 0x00:
            game_id[i] = 0x20
    game_id = game_id.decode()
        
    print('GameID: [%s]' % game_id)
    print('Title:', games[game_id]['title'])

    icon0 = None
    if args.icon0:
        icon0 = get_icon0(args.icon0)
    if not icon0 and 'icon0' in games[game_id]:
        icon0 = get_icon0(games[game_id]['icon0'])

    pic0 = None
    if args.pic0:
        pic0 = get_pic0(args.pic0)
    if not pic0 and 'pic0' in games[game_id]:
        pic0 = get_pic0(games[game_id]['pic0'])
        
    pic1 = None
    if args.pic1:
        pic1 = get_pic1(args.pic1)
    if not pic1 and 'pic1' in games[game_id]:
        pic1 = get_pic1(games[game_id]['pic1'])

    snd0 = None
    if args.snd0:
        snd0 = get_snd0(args.snd0, td.name)
    if not snd0 and 'snd0' in games[game_id]:
        snd0 = get_snd0(games[game_id]['snd0'], td.name)
        
        
    print('Installing to', args.psp_game_dir + '/' + game_id)
    shutil.copytree('TempGBA-Single-Game', args.psp_game_dir + '/' + game_id,
                    dirs_exist_ok=True)

    
    with open('TempGBA-Single-Game/PBOOT.PBP', 'rb') as f:
        eboot = read_eboot(f)

    if icon0:
        eboot['icon0.png'] = icon0
    if pic0:
        eboot['pic0.png'] = pic0
    if pic1:
        eboot['pic1.png'] = pic1
    if snd0:
        eboot['snd0.at3'] = snd0

    print('Writing', args.psp_game_dir + '/' + game_id + '/PBOOT.PBP')
    with open(args.psp_game_dir + '/' + game_id + '/PBOOT.PBP', 'wb') as f:
        write_eboot(f, eboot)
        
    with open(args.psp_game_dir + '/' + game_id + '/roms/game.gba', 'wb') as o:
        print('Writing', args.psp_game_dir + '/' + game_id + '/roms/game.gba')
        o.write(game)
