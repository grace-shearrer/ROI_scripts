#This creates the necessary masks and ROIs in every feat directory
#The region is hard coded and requires you to change it
#at the end use "find . -name RCaudatevalues.txt -exec cat {} \; >> TotalCaudate.txt" 
#this will cat all the files for this particular region

import sys
import glob
import os
import subprocess
from subprocess import check_output
 

def make_mask(basedir, targetdir):
  for dir in glob.glob(basedir+'sb_00*'+targetdir+'taste_run*/'):
    os.chdir(dir+'reg/')
    print "hello"
    print "now in" +os.getcwd()
    subprocess.call( 'invwarp -w  highres2standard_warp.nii.gz -o standard2highres_warp.nii.gz -r highres.nii.gz', shell=True)
    print "starting apply warp"
    subprocess.call('applywarp -i /corral-repl/utexas/poldracklab/data/sugar_brain/ROIs/RCaudate_mask.nii.gz -r example_func.nii.gz -o RCaudateMaskFunc.nii.gz -w standard2highres_warp --postmat=highres2example_func.mat', shell=True)
    print "starting fslmaths"
    subprocess.call('fslmaths RCaudateMaskFunc.nii.gz -thr 0.5 -bin RCaudateMaskFuncBin.nii.gz', shell=True) 
    print "starting fslstats"
    os.chdir('../stats/')
    print "now in" +os.getcwd()
    print "starting fslstats"
    f=open('RCaudatevalues.txt', 'w')
    for filename in glob.glob('cope*'):
      output=subprocess.Popen(['fslstats', filename, '-m','-k','../reg/RCaudateMaskFuncBin.nii.gz'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
      x=output.communicate()
      f.write('%s\n' % (x[0],))
    f.close()
      
def main():
#Global variables
  basedir='/corral-repl/utexas/poldracklab/data/sugar_brain/'
  targetdir='/model/feat/'
  make_mask(basedir, targetdir)
main()

