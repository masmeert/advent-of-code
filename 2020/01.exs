defmodule DayOne do
  defp read_input() do
    {:ok, values} = File.read("./inputs/01.txt")

    values
    |> String.split("\n")
  end

  def part_one do
    input = read_input()

  end

  def part_two do
    input = read_input()

  end
end

DayOne.part_one()
DayOne.part_two()