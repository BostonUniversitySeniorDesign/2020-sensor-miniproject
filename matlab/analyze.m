function analyze(file)
arguments
  file (1,1) string {mustBeFile}
end

dat = load_data(file);

plot_time(dat.time)

end
