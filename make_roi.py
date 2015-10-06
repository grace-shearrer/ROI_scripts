import sys
import glob
import os
from subprocess import check_output


#f=open('make_rois.sh', 'w')

def make_roi (region, cope_num):
  for file in glob.glob('/corral-repl/utexas/poldracklab/data/sugar_brain/sb_00*/model/Lev2/lev2_taste_fnirt.gfeat/cope'+cope_num+'.feat/stats/cope1.nii.gz'): 
    x=subprocess.call(['fslstats',file,'-m', '-k /corral-repl/utexas/poldracklab/data/sugar_brain/ROIs/func_',region,'.nii.gz']) 
    print x

def main():
  check_args=2
  if len(sys.argv)<3:
    print (' need roi name and which cope.feat please')
    sys.exit()
  elif check_args==2:
    region=sys.argv[1]
    cope_num=sys.argv[2]
  make_roi(region, cope_num)
main()



#subprocess.call(['wc', '-l', file])
