%%COORP
%%SEGUNDA FUNCION TESIS
%%la funcion [X,vaps,percent,acum]=coorp(D)
%%Calcula las coordenadas principales a partir
%%de una matriz de D de cuadrados
%%distancias
%%
%%Entradas: D=matriz de cuadrados distancias
%%D ES D2_S
%%
%%Devuelve:
%%X=matriz de coordenadas principales
%%vaps=Vector fila que contiene
%%los autovalores
%%acum=vector fila que contiene los porcentajes
%% de variabilidad acumulados

function [X,vaps,percent,acum]=coorp3c(D)
[n,n]=size(D);
%%comprobamos que D es euclidea (ie,B>=0)
H=eye(n)-ones(n)/n;
B=-H*D*H/2;
L=eig(B);
m=min(L);
epsilon=1.e-6;
if abs(m)< epsilon
%%hacemos la transformacion non2euclid
  D1=non2euclid(D);
  B=-H*D1*H/2;
end
%%%------
%%calculo de coordenadas principales
%%(solo consideramos las no nulas)
%%
[T,lambda,V]=svd(B);
vaps=diag(lambda)';
j=1;
while vaps (j)> epsilon
  T1=T(:,1:j);
  X=T1*sqrt(lambda(1:j,1:j));
  j=min(j+1,n);
end

percent=vaps/sum(vaps)*100;
acum=zeros(1,n);
for i=1:n
  acum(i)=sum(percent(1:i));
end
%%----
%%vector de etiquetas para los individuos
%%
for i=1:n
  lab(i,:)=sprintf('%3g',i);
end
%%-------
%%representacion de los datos
%%en dimension 2
plot3(X(:,1),X(:,2),X(:,3),'*b','MarkerSize',15)
grid
hold on
xlabel('Primera coordenada principal','FontSize',10)
ylabel('Segunda coordenada principal','FontSize',10)
zlabel('Tercera coordenada principal','FontSize',10)
title(['Porcentaje de variabilidad explicada',num2str(acum(3)),'%'],'FontSize',12)

for i=1:n;
  text(X(i,1),X(i,2),lab(i,:));
end