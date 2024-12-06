defmodule Mix.Tasks.Day1 do
  use Mix.Task
  require Timer
  require Input

  @input "input.txt"

  defp parse_line(line) do
    line
    |> String.trim()
    |> String.split()
    |> Enum.map(&String.to_integer/1)
    |> List.to_tuple()
  end

  defp parse_input do
    {left, right} =
      __ENV__.file
      |> Input.read_lines(@input)
      |> Enum.map(&parse_line/1)
      |> Enum.unzip()

    {Enum.sort(left), Enum.sort(right)}
  end

  defp part_one({left, right}) do
    Enum.zip_with(left, right, &abs(&1 - &2))
    |> Enum.sum()
  end

  defp part_two({left, right}) do
    rfreq = Enum.frequencies(right)

    Enum.reduce(left, 0, &(&2 + &1 * Map.get(rfreq, &1, 0)))
  end

  def run(_) do
    data = Timer.measure(fn -> parse_input() end, "Parsing")
    p1_result = Timer.measure(fn -> part_one(data) end, "Part 1")
    p2_result = Timer.measure(fn -> part_two(data) end, "Part 2")
    IO.puts(p1_result)
    IO.puts(p2_result)
  end
end
