defmodule DayOne do
  defp read_input() do
    {:ok, values} = File.read("./inputs/01.txt")

    values
    |> String.split("\n\n")
    |> Enum.map(fn x ->
      x
      |> String.split("\n")
      |> Enum.map(fn y -> String.to_integer(y) end)
      |> Enum.reduce(fn i, acc -> i + acc end)
    end)
    |> Enum.sort(&(&1 > &2))
  end

  def part_one do
    calories = read_input()

    calories
    |> Enum.at(0)
    |> IO.inspect()
  end

  def part_two do
    calories = read_input()

    calories
    |> Enum.slice(0..2)
    |> Enum.reduce(fn i, acc -> i + acc end)
    |> IO.inspect()
  end
end

DayOne.part_one()
DayOne.part_two()
