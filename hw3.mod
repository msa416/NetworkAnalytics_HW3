param n; #Number of weeks
param k; #Rolling weeks

set N := 1..n;
set K := 1..k;

param revenue{N};
param cum_rev{N};

var F{1..k+1}>=0;
var p;
var q;
var m := cum_rev[k]; #Set initial value at maximum revenue to prevent local minima


subject to initForecast: p * m = F[1];
subject to Forecast{t in 2..k}: (m * p + q * (cum_rev[t-1])) * (m - cum_rev[t-1]) = m * F[t];

minimize error_squared: sum{t in K} (F[t] - revenue[t])^2;