
hue = csvread('hue.csv');
sat = csvread('sat.csv');
val = csvread('val.csv');

hue_cropped = hue(3:end, 2);
sat_cropped = sat(3:end, 2);
val_cropped = val(3:end, 2);

hue_normalized = hue_cropped / length(hue_cropped);
sat_normalized = sat_cropped / length(sat_cropped);
val_normalized = val_cropped / length(val_cropped);


figure(1)
hist3([hue_cropped;sat_cropped], [50 50]);
title("hue vs sat")
% 
% figire(2)
% hist3([hue_normalized;val_normalized], [50 50]);
% title("hue vs val")
% 
% 
% figure(3)
% hist3([val_normalized;sat_normalized], [50 50]);
% title("val vs sat")


% hist3([data1;data2], [50 50]);