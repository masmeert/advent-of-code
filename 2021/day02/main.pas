PROGRAM DAY02;

 
TYPE 
 splitresult = ARRAY OF STRING;

 
VAR 
 depth, horizontal, x:INTEGER;

result, val:splitresult;

data:ARRAY[0. .5]
     OF STRING =
       ('forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2');

 
FUNCTION IsSeparator (CONST C:CHAR;
CONST Separators: STRING):BOOLEAN;

VAR 
 sep:CHAR;

BEGIN 
 FOR sep IN Separators DO BEGIN 
 IF sep = C THEN BEGIN 
 IsSeparator:= True;

EXIT;

END;

END;

IsSeparator:= False;

END;

 
FUNCTION Split (CONST Str, Separators: STRING):splitresult;

var 
 charIndex, ItemIndex:INTEGER;

len:INTEGER;

separatorCount:INTEGER;

start:INTEGER;

BEGIN 
 len:= Length (Str);

IF len = 0 THEN BEGIN 
 result:= nil;

EXIT;

END;

separatorCount:= 0;

FOR charIndex:= 1 TO len DO BEGIN 
  IF IsSeparator (Str[charIndex], Separators)
     THEN
       BEGIN 
     inc (separatorCount);

END;

END;

SetLength (result, separatorCount + 1);

ItemIndex:= 0;

start:= 1;

charIndex:= 1;

FOR charIndex:= 1 TO len DO BEGIN 
  IF IsSeparator (Str[charIndex], Separators)
     THEN
       BEGIN 
       IF
       charIndex >
       start
       THEN
       BEGIN 
       result[ItemIndex]: = Copy (Str, start, charIndex - start);

inc (ItemIndex);

END;

start:= charIndex + 1;

END;

END;

 
IF len > start THEN BEGIN 
 result[ItemIndex]:= Copy (Str, start,
	len - start + 1);

inc (ItemIndex);

END;

 
SetLength (result, ItemIndex);

END;

 
FUNCTION PartOne ():INTEGER;

BEGIN 
 depth:= 0;

horizontal:= 0;

FOR x: = 0 TO Length (data) DO 
 BEGIN 
 val:= Split (data[x], ' ');

write (val[0]);

END;

PartOne:= depth * horizontal 
 END;

 
BEGIN 
 writeln (PartOne ());

writeln ('');

END.
