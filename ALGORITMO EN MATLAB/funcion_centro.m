function [h,w,x,y] = funcion_centro(mask)
 
    lista_x = [];
    lista_y = [];
    for i = 1:2:size(mask,1)
        for j = 1:2:size(mask,2)
            if mask(i,j) == 1
                lista_y(end+1) = i;
                lista_x(end+1) = j;
            end
        end
    end
    A = length(lista_x);
    r = real(sqrt(A/pi));
    h = round(2*r);
    w = round(2*r);
    x = round(sum(lista_x)/length(lista_x));
    y = round(sum(lista_y)/length(lista_y));
    
end