for x in /corral-repl/utexas/poldracklab/data/sugar_brain/sb_00*/model/feat/taste_run*/reg/highres2standard_warp.nii.gz;
do
  echo "invwarp -w $x -o standard2highres_warp -r highres | applywarp -i /corral-repl/utexas/poldracklab/data/sugar_brain/ROIs/RCaudate_mask.nii.gz -r example_func -o RCaudateMaskFunc -w standard2highres_warp --postmat=highres2example_func.mat | fslmaths RCaudateMaskFunc.nii.gz -thr 0.5 -bin RCaudateMaskFuncBin.nii.gz"
done
 


#subprocess.call(['wc', '-l', file])
