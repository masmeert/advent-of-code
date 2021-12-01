PROGRAM DAY01;

VAR
    sum, x: INTEGER;
    data: ARRAY[0..9] OF INTEGER = (199,200,208,210,200,207,240,269,260,263);

FUNCTION Increases(step: INTEGER) : INTEGER;
BEGIN
    sum := 0;
    FOR x := step TO Length(data) DO
    BEGIN
      IF data[x] > data[x-step] THEN 
        sum := sum + 1;
    END;
    Increases := sum
END;

BEGIN
    writeln (Increases(1));
    writeln (Increases(3))
END.