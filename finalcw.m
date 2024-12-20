%% TEAM 20 MODELLING AND SIMULATION COURSEWORK
% This coursework is about modelling the growth of the forest in the Mekong 
% Region. We compare this model with the simulaion created to compare and analyse 
% the differences.


clear;
%we read data from matrix
data = readmatrix("team20_data.xlsx");

time = data(:, 1);   % Time
number = data(:, 2); % Number of trees

% we defined the constrained growth ODE
func_ode = @(t, y, a, b) a * y - b * y^2;

a = 0.0215;  
b = 0.0000001; 




y0 = number(1);

opts=odeset('RelTol',1e-5);
[t, y] = ode45(@(t, y) func_ode(t, y, a, b), time, y0,opts);


pred_y = y;

% Plot the  predicted curve with tree data
figure;
scatter(time, number, 'o', 'LineWidth', 2, 'Color', [0.5 0 0.5], 'DisplayName', 'Observed Trees');
hold on;
plot(t, pred_y, '-', 'LineWidth', 2, 'Color', 'b', 'DisplayName', 'Constrained Growth Model');
xlabel('Time');
ylabel('Tree Population/mHa');
title('Constrained Growth ODE Graph');
legend;
grid on;
%%realtive error part
% Calculate the relative error
relative_error = abs(number - pred_y) ./ number * 100;


disp('Relative Error (%):');
disp(relative_error);


%plot the relative error
figure;
plot(time, relative_error, '-o', 'LineWidth', 2, 'Color', 'r');
xlabel('Time');
ylabel('Relative Error (%)');
title('Relative Error Graph');
grid on;
