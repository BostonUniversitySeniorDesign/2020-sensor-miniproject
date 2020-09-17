function plot_time(time)
arguments
  time (:,1) datetime
end

intervals = seconds(diff(time));

addons = matlab.addons.installedAddons;
if any(addons{:,"Name"} == "Statistics and Machine Learning Toolbox")
  pd = fitdist(intervals, 'Gamma');
  % example of estimating parameters

  histfit(intervals, 100, 'Gamma')
  legend('data', 'fit')
else
  histogram(intervals, 100)
end


xlabel('time interval (seconds)')
ylabel('occurences')

title('time interval observed')
end