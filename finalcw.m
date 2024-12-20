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


%simulation results
tree_pop = [25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 26, 27, 31, 33, 35, 39, 42, 46, 47, 53, 63, 67, 71, 79, 91, 96, 97, 105, 112, 112, 111, 110, 99, 97, 91, 87, 89, 85, 88, 89, 85, 89, 90, 101, 101, 97, 93, 85, 85, 81, 85, 91, 90, 84, 81, 81, 85, 86, 87, 88, 95, 92, 92, 94, 98, 107, 112, 113, 118, 114, 117, 120, 126, 131, 134, 143, 152, 146, 144, 152, 152, 163, 168, 170, 175, 173, 164, 167, 173, 182, 183, 190, 195, 195, 194, 206, 212, 230, 228, 242, 243, 247, 253, 250, 258, 263, 269, 262, 258, 250, 266, 264, 257, 259, 255, 250, 256, 260, 266, 276, 282, 284, 283, 277, 286, 289, 289, 289, 290, 284, 295, 296, 305, 306, 314, 305, 312, 315, 326, 332, 332, 348, 359, 371, 389, 398, 405, 410, 407, 402, 405, 393, 387, 385, 393, 402, 400, 401, 401, 398, 409, 404, 404, 395, 402, 416, 432, 438, 439, 443, 445, 443, 459, 449, 448, 443, 427, 439, 450, 447, 434, 439, 424, 441, 433, 431, 439, 440, 440, 453, 448, 456, 468];
slice_150_to_250 = tree_pop(88:110);



% Plot the  predicted curve with tree data
figure;
scatter(time, number, 'o', 'LineWidth', 2, 'Color', [0.5 0 0.5], 'DisplayName', 'Observed Trees');
hold on;
scatter(time, slice_150_to_250, 'o', 'LineWidth', 2, 'Color', [0.5 0 0], 'DisplayName', 'Simulation results')
plot(t, pred_y, '-', 'LineWidth', 2, 'Color', 'b', 'DisplayName', 'Constrained Growth Model');
xlabel('Time');
ylabel('Tree Population/mHa');
title('Constrained Growth ODE Graph');
legend;
grid on;
%%realtive error part
% Calculate the relative error
relative_error = abs(number - pred_y) ./ number * 100;
sim_relative_error = abs(slice_150_to_250' - pred_y) ./ slice_150_to_250' * 100;


disp('Relative Error (%):');
disp(relative_error);


%plot the relative error
figure;
hold on
plot(time, relative_error, '-o', 'LineWidth', 2);
plot(time, sim_relative_error, '-o', 'LineWidth', 2);
xlabel('Time');
ylabel('Relative Error (%)');
title('Relative Error Graph');
grid on;
