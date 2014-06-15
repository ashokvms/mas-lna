% Options
numCols = 10;
opts = {'Delimiter',','};

% Open file for reading
fid = fopen('../../data/istanbul_stock.csv');

% Read header line
headers = textscan(fid, repmat('%s',1,numCols), 1, opts{:});

% Read data
input = textscan(fid,'%s%f%f%f%f%f%f%f%f%f', opts{:});

% Close file
fclose(fid);

% Collect data

features ={};
for i=1:536
    temp = [];
    for j = 4:10
        temp = [temp ; input{1,j}(i,1)];
    end
    features = [features,temp];
end

ise ={};
for i=1:536
    temp = input{1,3}(i,1);
    ise = [ise,temp];
end

headers = [headers{:}];
%input = [input{:}];

clear temp fid opts numCols i j