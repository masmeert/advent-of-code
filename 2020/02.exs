defmodule DayTwo do
  defp read_input() do
    {:ok, values} = File.read("./inputs/02.txt")

    values
    |> String.split("\n", trim: true)
    |> Enum.map(&parse_row/1)
  end

  defp parse_row(row) do
    [[min, max, letter, password]] =
      Regex.scan(
        ~r/(\d+)-(\d+) (\w+): (\w+)/,
        row,
        capture: :all_but_first
      )

    %{
      min: String.to_integer(min),
      max: String.to_integer(max),
      letter: letter,
      password: password
    }
  end

  def part_one do
    input = read_input()

    input
    |> Enum.count(fn %{min: min, max: max, letter: letter, password: password} ->
      count =
        password
        |> String.graphemes()
        |> Enum.filter(fn l -> l == letter end)
        |> length

      count >= min && count <= max
    end)
    |> IO.inspect()
  end

  def part_two do
    input = read_input()

    input
    |> Enum.count(fn %{min: min, max: max, letter: letter, password: password} ->
      min_match = String.at(password, min - 1) == letter
      max_match = String.at(password, max - 1) == letter
      
      (min_match || max_match) && min_match != max_match
    end)
    |> IO.inspect()
  end
end

DayTwo.part_one()
DayTwo.part_two()
