#!/usr/bin/python

import argparse
import csv
import glob
from subprocess import call
from os import path
import pandas

def handle_args():
  parser = argparse.ArgumentParser()
  parser.add_argument('-w', '--wavdir', help='directory with wav files', default="wav/segmented_16bit")
  parser.add_argument('-c', '--config', help='openSMILE config file', default= "conf/emobase2010.conf")
  parser.add_argument('-l', '--labels', help='file with class labels', default="eval/category.txt")
  return vars(parser.parse_args())

if __name__=="__main__":
  args = handle_args()
  print(args)

  wavnames = glob.glob("%s/*.wav" % args['wavdir'])

  labels = pandas.read_csv(args['labels'])

  config = args['config']
  configid = path.splitext(path.basename(config))[0]    # e.g. emobase2010

  for w in wavnames:
    fname, ext = path.splitext(path.basename(w))
    fid, uid = fname.split('-')
    classlabel = labels.ans1[(labels.fid==fid) & (labels.uid==int(uid))].to_string()[-3:]
    instname = "%s.%s" % (fid, uid)
    call(["SMILExtract", '-C', config, '-I', w, '-O', "%s.arff" % configid, '-N', instname, '-classtype', "{NEU,JOY,DIS,ANG,SAD,ACC,SUR,OTH,FEA}", '-class', classlabel])
