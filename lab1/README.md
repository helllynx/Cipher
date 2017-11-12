# Lab 1

**(I'll use Bless Hex Editor)**


## Ex 2


| format        | 	    HEX     |	   ASCII	|
| ------------- |:-------------:|:-------------:|
| flac      	| 66 4C 61 43 00 00 00 22 | fLaC..."	|
| ogg       	| 4F 67 67 53 00 02 00 00  00 00 00 00 00 00  | OggS..........	|
| wav       	| 57 41 56 45 66 6D 74	| WAVEfmt |
| JPG			| FF D8 FF E0 xx xx 4A 46 49 46 00 | ÿØÿà..JFIF. |
| PDF 			| 25 50 44 46 | %PDF |
| PNG 			| 89 50 4E 47 0D 0A 1A 0A | ‰PNG.... |
| ZIP 			| 50 4B 03 04 | PK.. |
| Unix exec file| 7F 45 4C 46 | .ELF |
| MP4  			| 66 74 79 70 69 73 6F 6D| ftypisom|

Or u can see [here](http://www.garykessler.net/library/file_sigs.html)


## Ex 4

```
file chess16.jpg 

chess16.jpg: JPEG image data, JFIF standard 1.01, resolution (DPI), density 72x72, segment length 16, progressive, precision 8, 4x4, frames 3
```

FF D8 - Generic JPEGimage file

JPEG file header: The proper JPEG header is the two-byte sequence, 0xFF-D8, aka Start of Image (SOI) marker.

Between the SOI and EOI, JPEG files are composed of segments. Segments start with a two-byte Segment Tag followed by a
two-byte Segment Length field and then a zero-terminated string identifier (i.e., a character string followed by a 0x00), as
shown below with the JFIF, Exif, and SPIFF segments.


0xFF-D8-FF-E0 — Standard JPEG/JFIF file, as shown below.

```
FF D8 FF E0 xx xx 4A 46
49 46 00 	  	ÿØÿà..JF
IF.
```

JFIF, JPE, JPEG, JPG 	  	JPEG/JFIF graphics file
Trailer: FF D9 (ÿÙ)



## Ex 5

```
file 08
08: Ogg data, Vorbis audio, stereo, 44100 Hz, ~160000 bps, created by: Xiphophorus libVorbis I (1.0 beta 3)
```


**It's just audio file.**



## Ex 6

BlackWhite
```
42 4D 92 00 00 00 00 00 00 00 82 00 00 00 6C 00 00 00 04 00 00 00 04 00 00 00 01 00 01 00 00 00 00 00 10 00 00 00 
13 0B 00 00 13 0B 00 00 02 00 00 00 02 00 00 00 42 47 52 73 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 02 00 00 00 00 00 00 00 
00 00 00 00 00 00 00 00 00 00 00 00 FF FF FF 00 C0 00 00 00 C0 00 00 00 30 00 00 00 30 00 00 00
```

BlueWhite
```
42 4D 92 00 00 00 00 00 00 00 82 00 00 00 6C 00 00 00 04 00 00 00 04 00 00 00 01 00 01 00 00 00 00 00 10 00 00 00 
13 0B 00 00 13 0B 00 00 02 00 00 00 02 00 00 00 42 47 52 73 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 02 00 00 00 00 00 00 00 
00 00 00 00 00 00 00 00 FF FF 00 00 FF FF FF 00 C0 00 00 00 C0 00 00 00 30 00 00 00 30 00 00 00

```


