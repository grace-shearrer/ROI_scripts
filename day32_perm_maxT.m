
%Assume you have 5 ROIs and for each ROI you want to look at the
%hypothesis test for the overall mean (over 26 measures).  Although we could use a bonferroni
%test to correct for all 5 tests, we might be better off using a
%permuataion based test.

%Steps of the max-statistic based permutation test
%Step 1:  Calculate test statistics for all 5 tests without use of
%permutations
%
%Step 2:  Randomly select some observations and multiply their values by
%negative 1.  Note, if the null were true in this case, then it shouldn't
%matter if we change the sign of our values or not.
%
%Step 3: Calculate the 5 test statistics and store the value of the
%maximum of the 5 statistics
%
%Step 4: Repeat 2 & 3 many, many times (let's do 5000)
%Step 5:  Compare the original test statistics from step 1 to the cutoff
%corresponding to the 95th percentile of the max tstat distribution


%load in data.  Note that each column holds the 20 mesures for a single ROI
roi_vals=load('/Users/imagining/Dropbox/Day32/roi_data.mat', '-ascii');


%=================================
%Step 1: Calculate 15 test statistics


mn_image = mean(roi_vals, 1);
sd_image = std(roi_vals,0, 1);
t_orig = sqrt(26).*mn_image./sd_image;
p_orig = 1-tcdf(t_orig, 25);


%=================================
%Steps 2 & 3 &4

nperm=5000;
tmax=zeros(1,nperm);
for i=1:nperm
    i
    %randomly select 1's and -1's
    random_flip=randsample([1, -1], 26, true);
    random_flip_mat = random_flip'*ones(1,5);
    roi_vals_flipped = random_flip_mat.*roi_vals;
    
    %calculate 5 t stats for permuted data
    mn_loop = mean(roi_vals_flipped, 1);
    sd_loop = std(roi_vals_flipped,0, 1);
    t_loop = sqrt(26).*mn_loop./sd_loop;
 
    
    %Cacluate the max t stat for this iteration
    tmax(i) = max(t_loop);
end

% Step 5:  Calculate the percentiles for each statistic based on
% permutation-based null dist

p_perm=zeros(5,1);
for i=1:5
    p_perm(i)=sum(tmax>=t_orig(i))/nperm;
end

[p_orig', p_perm]

sig_pcer = p_orig<0.05;
sig_bon = p_orig<0.05/5;
sig_perm = p_perm<0.05;

sig_vals = [sig_pcer; sig_bon; sig_perm']'
sum(sig_vals)

