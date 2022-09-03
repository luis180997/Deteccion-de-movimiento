clc; clear; close all;

cam = webcam(1);

% ventana para salir del video
hWaitbar = waitbar(0, 'Iteration1', 'Name','Solving problem',...
    'CreateCancelBtn', 'delete(gcbf)');

% Se inializa el contador y la imagen gris
gray_a=0;
i=0;

while 1
    
    Img = snapshot(cam); % Se toma un frame del video de la webcam
    
    % Se convierte el frame a escala de grises y se halla la diferencia
    gray = rgb2gray(Img);
    dif = gray-gray_a;
    
    % Se binariza la diferencia con un umbral de 0.05
    img_bin = imbinarize(dif,0.05); % 0.05: umbral[0-1]
    % Se aplica un filtro para borrar algunos puntos
    img_bin = medfilt2(img_bin,[8,8]);
    
    % Mediante funciones se halla el centro y se dibuja un recuadro
    [h,w,x,y] = funcion_centro(img_bin);
    imagen_final = funcion_recuadro(Img,h,w,x,y);
    
    A = sum(sum(img_bin)); % Se halla el Area (pixeles^2)
    if A>600
        disp('hay movimiento');
    else
        disp('no hay movimiento');
    end
    
    % Se actualiza la imagen gris anterior cada 2 frames
    if mod(i,2) == 0
        gray_a = gray;
    end
    
    % Se muestra el resultado del procesamiento
    imshow(imagen_final);
    
    %codigo para salir del bucle y apagar la camara
    if ~ishandle(hWaitbar)
        disp('Detenido');
        clear cam
        close all
        break
    else
        waitbar(i/5, hWaitbar, ['Iteration', num2str(i)]); % muestra las iteraciones
    end
    i = i+1;

end