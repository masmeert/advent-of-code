function findMarkerPosition(buffer: string, markerSize: number): number {
  for (let i = 0; i < buffer.length - markerSize; i++) {
    const slice = buffer.slice(i, i + markerSize);
    if (new Set(slice).size === markerSize) {
      return markerSize + i;
    }
  }
  return 0;
}

const buffer = await Deno.readTextFile("./inputs/06.txt");
console.log(findMarkerPosition(buffer, 4));
console.log(findMarkerPosition(buffer, 14));
