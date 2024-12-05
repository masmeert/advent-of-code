defmodule DayOne do
  defp parse_line(line) do
    [a, b] = line |> String.trim() |> String.split()
    {String.to_integer(a), String.to_integer(b)}
  end

  defp read_input do
    {left, right} =
      "./inputs/01.txt"
      |> File.stream!()
      |> Stream.map(&parse_line/1)
      |> Enum.unzip()

    {Enum.sort(left), Enum.sort(right)}
  end

  def part_one() do
    {left, right} = read_input()

    Enum.zip_with(left, right, &abs(&1 - &2))
    |> Enum.sum()
  end

  def part_two() do
    {left, right} = read_input()
    rfreq = Enum.frequencies(right)

    Enum.reduce(left, 0, fn a, acc ->
      acc + a * Map.get(rfreq, a, 0)
    end)
  end
end

IO.inspect(DayOne.part_one())
IO.inspect(DayOne.part_two())
