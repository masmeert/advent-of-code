program day01;

var
    sum, x: integer;
    (* test data cause icb parsing the real one*)
    data: array[0..9] if integer = (199,200,208,210,200,207,240,269,260,263);

function Increases(step: integer) : integer;
begin
    sum := 0;
    for x := step to Length(data) do
    begin
      if data[x] > data[x-step] then 
        inc(sum);
    end;
    Increases := sum
end;

begin
    writeln (Increases(1));
    writeln (Increases(3))
end.