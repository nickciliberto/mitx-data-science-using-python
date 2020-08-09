#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 15 12:02:44 2020

@author: nicholas
"""

def song_playlist(songs, max_size):
    """
    songs: list of tuples, ('song_name', song_len, song_size)
    max_size: float, maximum size of total songs that you can fit

    Start with the song first in the 'songs' list, then pick the next 
    song to be the one with the lowest file size not already picked, repeat

    Returns: a list of a subset of songs fitting in 'max_size' in the order 
             in which they were chosen.
    """
    songsCopy = songs[:]
    playlist = []
    availableSize = max_size
    if songsCopy[0][2] <= max_size:
        playlist.append(songsCopy[0][0])
        availableSize -= songsCopy[0][2]
        songsCopy.pop(0)
    else:
        return []
    
    songsCopy.sort(key = lambda x: x[2])
    for song in songsCopy:
        if song[2] <= availableSize:
            playlist.append(song[0])
            availableSize -= song[2]
        else:
            break
    return playlist

songs = [('Roar',4.4, 4.0),('Sail',3.5, 7.7),('Timber', 5.1, 6.9),('Wannabe',2.7, 1.2)]
max_size1 = 12.2
max_size2 = 11

print(song_playlist(songs, max_size1))
print(song_playlist(songs, max_size2))