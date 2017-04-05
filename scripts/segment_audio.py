#!/usr/bin/python

from glob import glob
from subprocess import call
from os import path

wavdir = "wav"
transdir = "trans"
outdir = "wav/segmented_16bit"

wavs = glob("%s/*.wav" % wavdir)

for w in wavs:
  t = w.replace(wavdir, transdir, 1).replace('wav','txt')
  fname, ext = path.splitext(path.basename(w))
  
  with open(t, 'r') as tf:
    for utt in tf:
      uid, start, end, speaker, text = utt.split(',')
      outname = "%s/%s-%s%s" % (outdir, fname, uid, ext)
      
      call(['sox', w, '-b16', outname, 'trim', start, "=%s" %end])
