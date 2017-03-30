
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
hs_crop = [hue_cropped,sat_cropped];
hs_norm = [hue_normalized, sat_normalized];
subplot(2, 1, 1)
hist3(hs_crop, [50 50]);
title("hue vs sat")
subplot(2,1, 2)
hist3(hs_norm, [50 50]);


figure(2)
hv_norm = [hue_normalized, val_normalized];
hist3(hv_norm, [50 50]);
title("hue vs val")


figure(3)
vs_norm = [val_normalized,sat_normalized];
hist3(vs_norm, [50 50]);
title("val vs sat")
fi
