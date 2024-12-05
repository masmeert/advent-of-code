defmodule DayTwo do
  defp parse_line(line) do
    line
    |> String.trim()
    |> String.split()
    |> Enum.map(&String.to_integer/1)
  end

  defp read_input do
    "./inputs/02.txt"
    |> File.stream!()
    |> Stream.map(&parse_line/1)
    |> Enum.to_list()
  end

  defp is_monotonic?(list, comparator) do
    Enum.chunk_every(list, 2, 1, :discard)
    |> Enum.all?(fn [a, b] -> comparator.(a, b) end)
  end

  defp valid_deltas?(list) do
    Enum.chunk_every(list, 2, 1, :discard)
    |> Enum.all?(fn [a, b] -> abs(b - a) in 1..3 end)
  end

  defp is_safe?(list) do
    (is_monotonic?(list, &Kernel.</2) or is_monotonic?(list, &Kernel.>/2)) and valid_deltas?(list)
  end

  defp is_safe_with_dampener?(list) do
    Enum.with_index(list)
    |> Enum.any?(fn {_, index} ->
      is_safe?(List.delete_at(list, index))
    end)
  end

  def part_one() do
    read_input()
    |> Enum.filter(&is_safe?/1)
    |> Enum.count()
  end

  def part_two() do
    read_input()
    |> Enum.filter(&is_safe_with_dampener?/1)
    |> Enum.count()
  end
end

IO.inspect(DayTwo.part_one())
IO.inspect(DayTwo.part_two())
