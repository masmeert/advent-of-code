defmodule Mix.Tasks.Day2 do
  use Mix.Task
  require Timer
  require Input

  @input "input.txt"

  defp parse_line(line) do
    line
    |> String.trim()
    |> String.split()
    |> Enum.map(&String.to_integer/1)
  end

  defp parse_input do
    __ENV__.file
    |> Input.read_lines(@input)
    |> Enum.map(&parse_line/1)
  end

  defp pairs(list) do
    Enum.chunk_every(list, 2, 1, :discard)
  end

  defp is_monotonic?(list, comparator),
    do: Enum.all?(pairs(list), fn [a, b] -> comparator.(a, b) end)

  defp valid_deltas?(list),
    do: Enum.all?(pairs(list), fn [a, b] -> abs(b - a) in 1..3 end)

  defp is_safe?(list) do
    (is_monotonic?(list, &(&1 < &2)) or is_monotonic?(list, &(&1 > &2))) and valid_deltas?(list)
  end

  defp is_safe_with_dampener?(list) do
    Enum.any?(0..(length(list) - 1), &is_safe?(List.delete_at(list, &1)))
  end

  def part_one(data) do
    Enum.count(data, &is_safe?/1)
  end

  def part_two(data) do
    Enum.count(data, &is_safe_with_dampener?/1)
  end

  def run(_) do
    data = Timer.measure(fn -> parse_input() end, "Parsing")
    p1_result = Timer.measure(fn -> part_one(data) end, "Part 1")
    p2_result = Timer.measure(fn -> part_two(data) end, "Part 2")
    IO.puts(p1_result)
    IO.puts(p2_result)
  end
end
