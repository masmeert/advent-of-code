defmodule DaySix do
  defp parse_line(line, y) do
    line
    |> String.trim()
    |> String.graphemes()
    |> Enum.with_index()
    |> Enum.map(fn {char, x} -> {{x, y}, char} end)
  end

  defp read_input do
    "./inputs/06.txt"
    |> File.stream!()
    |> Enum.with_index()
    |> Enum.flat_map(fn {line, y} -> parse_line(line, y) end)
    |> Enum.into(%{})
  end

  defp turn_right(:up), do: :right
  defp turn_right(:right), do: :down
  defp turn_right(:down), do: :left
  defp turn_right(:left), do: :up

  defp forward({x, y}, :up), do: {x, y - 1}
  defp forward({x, y}, :down), do: {x, y + 1}
  defp forward({x, y}, :left), do: {x - 1, y}
  defp forward({x, y}, :right), do: {x + 1, y}

  defp is_blocked?(grid, position) do
    Map.get(grid, position, ".") == "#"
  end

  defp is_out_of_bounds?(grid, {x, y}) do
    xs = grid |> Map.keys() |> Enum.map(fn {x, _} -> x end)
    ys = grid |> Map.keys() |> Enum.map(fn {_, y} -> y end)
    min_x = Enum.min(xs)
    max_x = Enum.max(xs)
    min_y = Enum.min(ys)
    max_y = Enum.max(ys)

    x < min_x or x > max_x or y < min_y or y > max_y
  end

  defp find_guard(grid) do
    {position, char} =
      grid
      |> Enum.find(fn {_, c} -> c in ["^", "v", "<", ">"] end)

    direction =
      case char do
        "^" -> :up
        "v" -> :down
        "<" -> :left
        ">" -> :right
      end

    {position, direction}
  end

  defp simulate_move(grid, position, direction, visited) do
    next = forward(position, direction)

    cond do
      is_blocked?(grid, next) ->
        simulate_move(grid, position, turn_right(direction), visited)

      is_out_of_bounds?(grid, next) ->
        MapSet.size(visited)

      true ->
        simulate_move(grid, next, direction, MapSet.put(visited, next))
    end
  end

  def part_one() do
    grid = read_input()
    {position, direction} = find_guard(grid)
    visited = MapSet.new() |> MapSet.put(position)
    simulate_move(grid, position, direction, visited)
  end
end

IO.inspect(DaySix.part_one())
