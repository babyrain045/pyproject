

p = [0 0.1 0.3 0.5 0.8 1];

gama = 1.4;
Dm = 540
for i = 1:length(p):
  ED50(i) = log10(log10(Dm)-log10(gama)(sum(p(1:i))-0.5))^-1;
end

X = p; y = ED50;
m = length(y); 


