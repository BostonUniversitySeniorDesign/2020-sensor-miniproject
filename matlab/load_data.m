function dat = load_data(file)
arguments
  file (1,1) string {mustBeFile}
end

fid = fopen(file, "r");

dat.temperature = [];
dat.occupancy = [];
dat.co2 = [];
dat.time = datetime.empty;

while ~feof(fid)
  r = jsondecode(fgetl(fid));
  room = string(fieldnames(r));
  dat.time(end+1) = datetime(r.(room).time, 'inputFormat', 'yyyy-MM-dd''T''HH:mm:ss.SSSSSS'); %#ok<*AGROW>

  dat.temperature(end+1) = r.(room).temperature;
  dat.occupancy(end+1) = r.(room).occupancy;
  dat.co2(end+1) = r.(room).co2;
end

fclose(fid);

end
