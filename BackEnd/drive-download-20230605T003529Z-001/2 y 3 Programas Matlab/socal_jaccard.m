%%X=[1 1 0 0 1 1; 1 1 1 0 0 1; 1 0 0 1 0 1; 1 0 0 1 0 1; 1 0 0 0 1 1; 0 0 0 0 1 0];%%PRIMERA FUNCION TESIS%% se usa D2_Sfunction [S_Sokal,S_Jaccard,D2_S,D2_J]=socal_jaccard(X)[n,p]=size(X);J=ones(n,p);a=X*X';d=(J-X)*(J-X)';S_Sokal=(a+d)/p;S_Jaccard=a./(p*ones(n)-d);J=ones(n);D2_S=2*(J-S_Sokal);D2_J=1*(J-S_Jaccard);