import sys
import glob
import os
import subprocess
from subprocess import check_output
#invwarp 
#-w /corral-repl/utexas/poldracklab/data/sugar_brain/SUBNUM/model/feat/taste_run*/reg/highres2standard_warp.nii.gz 
#-o standard2highres_warp.nii.gz 
#-r highres.nii.gz | applywarp 
#-i /corral-repl/utexas/poldracklab/data/sugar_brain/ROIs/RCaudate_mask.nii.gz 
#-r example_func.nii.gz 
#-o RCaudateMaskFunc.nii.gz 
#-w standard2highres_warp 
#--postmat=highres2example_func.mat | fslmaths RCaudateMaskFunc.nii.gz -thr 0.5 -bin RCaudateMaskFuncBin.nii.gz
 
 
#f=open('make_mask.sh', 'w')
def make_mask(basedir, targetdir, targetfile, sub, repl_dict):
  for dir in glob.glob(basedir+sub+targetdir+'taste_run*/reg/'):
    os.chdir(dir)
    print "hello"
    print "now in" +os.getcwd()
    subprocess.call( 'invwarp -w  highres2standard_warp.nii.gz -o standard2highres_warp.nii.gz -r highres.nii.gz', shell=True)
    print "starting apply warp"
    subprocess.call('applywarp -i /corral-repl/utexas/poldracklab/data/sugar_brain/ROIs/RCaudate_mask.nii.gz -r example_func.nii.gz -o RCaudateMaskFunc.nii.gz -w standard2highres_warp --postmat=highres2example_func.mat', shell=True)
    print "starting fslmaths"
    subprocess.call('fslmaths RCaudateMaskFunc.nii.gz -thr 0.5 -bin RCaudateMaskFuncBin.nii.gz', shell=True)
  #f.write('%s\n' % (new_file,))

#f.close() 

def main():
  check_args=1
  if len(sys.argv)<2:
    print (' subject number')
    sys.exit()
  elif check_args==1:
    sub=sys.argv[1]

#Global variables
  basedir='/corral-repl/utexas/poldracklab/data/sugar_brain/'
  targetdir='/model/feat/'
  targetfile='highres2standard_warp.nii.gz'
  repl_dict={'SUBNUM':sub}
  make_mask(basedir, targetdir, targetfile, sub, repl_dict)
main()
