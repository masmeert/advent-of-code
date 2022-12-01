const data = await Deno.readTextFile("./inputs/.txt").then((data) => {
  return data.split("\n");
});
