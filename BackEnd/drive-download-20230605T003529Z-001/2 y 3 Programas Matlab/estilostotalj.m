%%todo
%--------------Plano de puntos ideales------------------------------------
%Los puntos ideales se tomaron del documento de excel, es una matriz
%que consta de 4 filas, cada una representa un estilo:
%Activo, Reflexivo, Teórico y Pragmático
%Estas condiciones solo se pueden editar en excel
%Aquí solo se usan los vectores finales

%De preferencia, no modificar el código

%matriz de estilos ideales
basedatos='EstiloseInteligencias.xlsx';
celdasestilos='C2:CD5';
estilosideales=xlsread(basedatos,6,celdasestilos);

%grafica de estilos ideales
[S_Sokal,S_Jaccard,D2_S,D2_J]=socal_jaccard(estilosideales);

%[R,vaps,percent,acum]=coorp(D2_S);
[R,vaps,percent,acum]=coorp3c(D2_J);
R
grid

%-----------------Incluir puntos----------------------------------------
%Se debe tener la base de datos en formato de excel para llamarla
%desde Matlab.
%Se selecciona 1)nombre del documento, 2)# de hoja y
%3)Rango con el comando -- xlsread(basedatos,3,celdasestilos15);--

%------SOLO PUNTO IDEAL-----
basedatos='EstiloseInteligencias.xlsx';
celdasestilosp='B2:CC2';
estup=xlsread(basedatos,10,celdasestilosp);

X=estilosideales;
%x=estu1;
%x=estu15;
%x=estu1360;
x=estup;
[m,n]=size(x);
r=zeros(m,3);
for i=1:m
[yt]=puntos_idealesi(X,x(i,:));
r(i,1:3)= yt(1:3);
end
r
%-------------
%
%
%--------CUALQUIER ESTUDIANTE O GRUPO------ 
%matriz de 15 estudiantes
basedatos='EstiloseInteligencias.xlsx';

%celdasestilos1='C2:CD2';
%celdasestilos15='C2:CD16';
celdasestilos1360='C2:CD1361';
%celdasestilosp='B40:CC59';

%estu1=xlsread(basedatos,3,celdasestilos1);
%estu15=xlsread(basedatos,3,celdasestilos15);
estu1360=xlsread(basedatos,2,celdasestilos1360);
%estup=xlsread(basedatos,10,celdasestilosp);

%x son los datos recolectados/obtenidos
%r es el punto, por cada individuo, que representa la combinación
%de estilos, en el orden: Activo, Reflexivo, Teórico y Pragmático
X=estilosideales;
%x=estu1;
%x=estu15;
x=estu1360;
%x=estup;
[m,n]=size(x);
r=zeros(m,3);
for i=1:m
[yt]=puntos_ideales(X,x(i,:));
r(i,1:3)= yt(1:3);
end
r


%------------Normas euclidianas--------------
%Se midió las normas euclidianas entre cada uno de los puntos
%y el punto ideal de cada estilo
[p q]=size(r);
[n m]=size(R);
normat=zeros(p,n);
%normat es la matriz donde constan las normas de cada vector(individuo)
%con cada punto ideal(4 estilos) del grupo total de datos obtenidos
for j=1:p
   for i=1:n
normat(j,i)=norm(R(i,:)-r(j,:));
    end
end
normat
grid
