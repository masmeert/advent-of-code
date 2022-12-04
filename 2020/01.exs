defmodule DayOne do
  defp read_input() do
    {:ok, values} = File.read("./inputs/01.txt")

    values
    |> String.split("\n", trim: true)
    |> Enum.map(&String.to_integer/1)
  end

  def part_one do
    input = read_input()

    input
    |> Enum.map(fn x ->
      input
      |> Enum.find(fn y -> x + y == 2020 end)
      |> case do
        nil -> nil
        y -> x * y
      end
    end)
    |> Enum.reject(&is_nil/1)
    |> List.first()
    |> IO.inspect()
  end

  def part_two do
    input = read_input()

    input
    |> Enum.map(fn x ->
      input
      |> Enum.map(fn y ->
        input
        |> Enum.find(fn z -> x + y + z == 2020 end)
        |> case do
          nil -> nil
          z -> x * y * z
        end
      end)
      |> Enum.reject(&is_nil/1)
      |> List.first()
    end)
    |> Enum.reject(&is_nil/1)
    |> List.first()
    |> IO.inspect()
  end
end

DayOne.part_one()
DayOne.part_two()
