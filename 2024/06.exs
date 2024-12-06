defmodule DaySix do
  def parse_input(file \\ "./inputs/06.txt") do
    {grid, start} =
      file
      |> File.read!()
      |> String.split("\n", trim: true)
      |> Enum.with_index()
      |> Enum.reduce({%{}, nil}, fn {line, y}, {grid, start} ->
        line
        |> String.graphemes()
        |> Enum.with_index()
        |> Enum.reduce({grid, start}, fn
          {char, x}, {grid, _} when char in ["^", "v", "<", ">"] ->
            {Map.put(grid, {x, y}, "."), {{x, y}, direction_to_int(char)}}

          {char, x}, {grid, start} ->
            {Map.put(grid, {x, y}, char), start}
        end)
      end)

    {Map.keys(grid), grid, start}
  end

  def direction_to_int("^"), do: 0
  def direction_to_int(">"), do: 1
  def direction_to_int("v"), do: 2
  def direction_to_int("<"), do: 3

  def calculate_next_position({x, y}, direction) do
    case direction do
      0 -> {x, y - 1}
      1 -> {x + 1, y}
      2 -> {x, y + 1}
      3 -> {x - 1, y}
    end
  end

  def simulate_movement({grid_points, grid, {start_pos, start_dir}}, obstacle \\ nil) do
    bounds = {
      grid_points |> Enum.map(&elem(&1, 0)) |> Enum.min_max(),
      grid_points |> Enum.map(&elem(&1, 1)) |> Enum.min_max()
    }

    move(
      {grid, bounds},
      {start_pos, start_dir},
      MapSet.new([start_pos]),
      MapSet.new([]),
      obstacle
    )
  end

  def move({grid, {{min_x, max_x}, {min_y, max_y}}} = env, {pos, dir}, visited, states, obstacle) do
    next_pos = calculate_next_position(pos, dir)
    {x, y} = next_pos
    current_state = {pos, dir}

    cond do
      MapSet.member?(states, current_state) ->
        {:loop_detected, visited}

      x < min_x or x > max_x or y < min_y or y > max_y ->
        {:out_of_bounds, visited}

      next_pos == obstacle or Map.get(grid, next_pos, "#") == "#" ->
        next_dir = rem(dir + 1, 4)
        move(env, {pos, next_dir}, visited, MapSet.put(states, current_state), obstacle)

      true ->
        move(
          env,
          {next_pos, dir},
          MapSet.put(visited, next_pos),
          MapSet.put(states, current_state),
          obstacle
        )
    end
  end

  def part_one(input \\ parse_input()) do
    input
    |> simulate_movement()
    |> elem(1)
    |> MapSet.size()
  end

  def part_two(input \\ parse_input()) do
    {_points, grid, {start_pos, _}} = input

    grid
    |> Map.filter(fn {pos, value} -> value == "." and pos != start_pos end)
    |> Map.keys()
    |> Task.async_stream(
      fn pos ->
        case simulate_movement(input, pos) do
          {:loop_detected, _} -> 1
          _ -> 0
        end
      end,
      max_concurrency: System.schedulers_online() * 2
    )
    |> Enum.map(fn {:ok, result} -> result end)
    |> Enum.sum()
  end
end

IO.inspect(DaySix.part_one())
IO.inspect(DaySix.part_two())
