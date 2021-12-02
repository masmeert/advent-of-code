program DAY02;

type
    splitResult = array of string;

var
    result: splitResult;
    depth, horizontal, x: integer;
    data: array[0..5] OF STRING = ('forward 5','down 5','forward 8','up 3','down 8','forward 2');

function isSeparator(const ch: char; const separator: string): boolean;
var sep: char;
begin
    for sep in separator do begin
        if sep=ch then begin
            isSeparator := true;
            exit;
        end;
    end;
    isSeparator := false;
end;

function splitString(const str; separator: string): splitResult;
var
    charIndex, itemIndex, len, separatorCount, start: integer;
begin
    len := Length(str);
    if len=0 then begin
        result := nil;
        exit;
    end;
    separatorCount := 0;
    for charIndex := 1 to len do begin
        if isSeparator(str[charIndex], separator) then begin
            inc(separatorCount)
        end;
    end;
    SetLength(result, separatorCount+1);
    itemIndex := 0;
    start := 1;
    for charIndex := 1 to len do begin
        if isSeparator(str[charIndex], separator) then begin
            if charIndex > start then begin
                result[itemIndex] := Copy(str, start, charIndex - start);
                inc(itemIndex);
            end;
            start := charIndex + 1
        end;
    end;
    if len > start then begin
        result[itemIndex] := Copy(str, start, len - start + 1);
        inc(itemIndex);
    end;
    SetLength(result, itemIndex);
end;

begin
    writeln ('');
end.
