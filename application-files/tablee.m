% Copyright (c) 2015, BENCHOP, Slobodan MilovanoviÄ‡

% Input problem_to_solve is string to know which problem to use
function [time, relerr, filepaths] = tablee(problem_to_solve, sig)
format long
warning off

Methods={'MC','MC-S','QMC-S','MLMC','MLMC-A',...
    'FFT','FGL','COS',...
    'FD','FD-NU','FD-AD',...
    'RBF','RBF-FD','RBF-PUM','RBF-LSML','RBF-AD','RBF-MLT'};

%% Problem 1 a) I
if problem_to_solve == 1
    rootpath=pwd;
    S=[90,100,110]; K=100; T=1.0; r=0.03; %sig=0.15;
    U=[2.758443856146076 7.485087593912603 14.702019669720769];
    
    filepathsBSeuCallUI=getfilenames('./','BSeuCallUI_*.m');
    par = {S,K,T,r,sig};
    [timeBSeuCallUI,relerrBSeuCallUI] = executor(rootpath, filepathsBSeuCallUI, U, par);
    cd(rootpath);
    
    filepaths = filepathsBSeuCallUI';
    time = timeBSeuCallUI';
    relerr = relerrBSeuCallUI';
    %% Problem 1 b) I
elseif problem_to_solve == 2
    rootpath=pwd;
    S=[90,100,110]; K=100; T=1.0; r=0.03; %sig=0.15;
    U=[10.726486710094511 4.820608184813253 1.828207584020458];
    
    filepathsBSamPutUI=getfilenames('./','BSamPutUI_*.m');
    par={S,K,T,r,sig};
    [timeBSamPutUI,relerrBSamPutUI] = executor(rootpath,filepathsBSamPutUI,U,par);
    cd(rootpath);
    
    filepaths = filepathsBSamPutUI';
    time = timeBSamPutUI';
    relerr = relerrBSamPutUI';
    %% Problem 1 c) I
elseif problem_to_solve == 3
    rootpath=pwd;
    S=[90,100,110]; K=100; T=1.0; r=0.03; B=1.25*K; % sig=0.15;
    U=[1.822512255945242 3.294086516281595 3.221591131246868];
    
    filepathsBSupoutCallI=getfilenames('./','BSupoutCallI_*.m');
    par={S,K,T,r,sig,B};
    [timeBSupoutCallI,relerrBSupoutCallI] = executor(rootpath,filepathsBSupoutCallI,U,par);
    cd(rootpath);
    
    filepaths = filepathsBSupoutCallI';
    time = timeBSupoutCallI';
    relerr = relerrBSupoutCallI';
    %% Problem 1 a) II
elseif problem_to_solve == 4
    rootpath=pwd;
    S=[97,98,99]; r=0.1; T=0.25; K=100; % sig=0.01;
    U=[0.033913177006141   0.512978189232598   1.469203342553328];
    
    filepathsBSeuCallUII=getfilenames('./','BSeuCallUII_*.m');
    par={S,K,T,r,sig};
    [timeBSeuCallUII,relerrBSeuCallUII] = executor(rootpath,filepathsBSeuCallUII,U,par);
    cd(rootpath);
    
    filepaths = filepathsBSeuCallUII';
    time = timeBSeuCallUII';
    relerr = relerrBSeuCallUII';
    %% Problem 1 b) II
elseif problem_to_solve == 5
    rootpath=pwd;
    S=[97,98,99]; K=100; T=0.25; r=0.1; % sig=0.01;
    U=[3.000000000000682 2.000000000010786   1.000000000010715];
    
    filepathsBSamPutUII=getfilenames('./','BSamPutUII_*.m');
    par={S,K,T,r,sig};
    [timeBSamPutUII,relerrBSamPutUII] = executor(rootpath,filepathsBSamPutUII,U,par);
    cd(rootpath);
    
    filepaths = filepathsBSamPutUII';
    time = timeBSamPutUII';
    relerr = relerrBSamPutUII';
    %% Problem 1 c) II
elseif problem_to_solve == 6
    rootpath=pwd;
    S=[97,98,99]; r=0.1; T=0.25; K=100; B=1.25*K; % sig=0.01;
    U=[0.033913177006134   0.512978189232598   1.469203342553328];
    
    filepathsBSupoutCallII=getfilenames('./','BSupoutCallII_*.m');
    par={S,K,T,r,sig,B};
    [timeBSupoutCallII,relerrBSupoutCallII] = executor(rootpath,filepathsBSupoutCallII,U,par);
    cd(rootpath);
    
    filepaths = filepathsBSupoutCallII';
    time = timeBSupoutCallII';
    relerr = relerrBSupoutCallII';
end

end
