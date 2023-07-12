%%codigo para incluir SOLAMENTE AL punto ideal
function [yt]=puntos_idealesi(X,x)
%X=[1 1 0 0 1 1; 1 1 1 0 0 1 ; 1 0 0 1 0 1;1 0 0 1 0 1;1 0 0 0 1 1 ;0 0 0 0 1 0 ];
%x=[1 1 0 0 0 1];
[n,p]=size(X);

%x=[1 0 1 1 0 1]; %de prueba
a=X*x'; d=(ones(n,p)-X)*(ones(1,p)-x)';
s=(a+d)/p;
d=2*(ones(n,1)-s);
st=s';
dt=d';

%despues de usar la funcion coorp
% Y es la matriz de coordenadas
[S_Sokal,S_Jaccard,D2_S,D2_J]=socal_jaccard(X);
%[Y,vaps,percent,acum]=coorp(D2_S);
[Y,vaps,percent,acum]=coorp3c(D2_S);
B=Y*Y';
b=diag(B);
[n,p]=size(Y);
Lambda=diag(vaps(1:p));
y=1/2*inv(Lambda)*Y'*(b-d);
yt=y';


%%-------
%%representacion de los datos
%%en dimension 3

%plot (y(1),y(2),'.r','MarkerSize',12);
plot3 (y(1),y(2),y(3),'.r','MarkerSize',12);
%plot3 (y(1),y(2),y(3),'.k','MarkerSize',12);
grid


