function foto = funcion_recuadro(imagen,h,w,x,y)

    foto = imagen;
    m = size(foto,1);
    n = size(foto,2);

    e = 4;
    R = 0;
    G = 255;
    B = 0;
    
    h = 2*round(h/2);
    w = 2*round(w/2);
    
    if (y-h/2-e > 0 && x-w/2-e > 0 && y+h/2+e < m && x+w/2+e < n) 
        % Primera linea horizontal
        foto(y-h/2-e : y-h/2, x-w/2-e : x+w/2+e,:) = 0;
        foto(y-h/2-e : y-h/2, x-w/2-e : x+w/2+e,1) = R;
        foto(y-h/2-e : y-h/2, x-w/2-e : x+w/2+e,2) = G;
        foto(y-h/2-e : y-h/2, x-w/2-e : x+w/2+e,3) = B;

        % Segunda linea horizontal
        foto(y+h/2 : y+h/2+e, x-w/2-e : x+w/2+e,:) = 0;
        foto(y+h/2 : y+h/2+e, x-w/2-e : x+w/2+e,1) = R;
        foto(y+h/2 : y+h/2+e, x-w/2-e : x+w/2+e,2) = G;
        foto(y+h/2 : y+h/2+e, x-w/2-e : x+w/2+e,3) = B;

        % Primera linea vertical
        foto(y-h/2-e : y+h/2+e, x-w/2-e : x-w/2,:) = 0;
        foto(y-h/2-e : y+h/2+e, x-w/2-e : x-w/2,1) = R;
        foto(y-h/2-e : y+h/2+e, x-w/2-e : x-w/2,2) = G;
        foto(y-h/2-e : y+h/2+e, x-w/2-e : x-w/2,3) = B;

        % Segunda linea vertical
        foto(y-h/2-e : y+h/2+e, x+w/2 : x+w/2+e,:) = 0;
        foto(y-h/2-e : y+h/2+e, x+w/2 : x+w/2+e,1) = R;
        foto(y-h/2-e : y+h/2+e, x+w/2 : x+w/2+e,2) = G;
        foto(y-h/2-e : y+h/2+e, x+w/2 : x+w/2+e,3) = B;
    else
        %disp("Cuadro fuera de rango");
    end
    
end