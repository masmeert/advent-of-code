defmodule Mix.Tasks.Day6 do
  use Mix.Task
  require Timer
  require Input

  @input "input.txt"

  defp direction_to_int(dir) do
    %{"^" => 0, ">" => 1, "v" => 2, "<" => 3}[dir]
  end

  defp calculate_next_position({x, y}, dir) do
    case dir do
      0 -> {x, y - 1}
      1 -> {x + 1, y}
      2 -> {x, y + 1}
      3 -> {x - 1, y}
    end
  end

  defp parse_input do
    lines =
      __ENV__.file
      |> Input.read_lines(@input)

    {grid, start} =
      for {line, y} <- Enum.with_index(lines),
          {char, x} <- Enum.with_index(String.graphemes(line)),
          reduce: {%{}, nil} do
        {g, s} ->
          if char in ~w(^ > v <) do
            {Map.put(g, {x, y}, "."), {{x, y}, direction_to_int(char)}}
          else
            {Map.put(g, {x, y}, char), s}
          end
      end

    {Map.keys(grid), grid, start}
  end

  defp simulate_movement({grid_points, grid, {start_pos, start_dir}}, obstacle \\ nil) do
    {x_min, x_max} = grid_points |> Enum.map(&elem(&1, 0)) |> Enum.min_max()
    {y_min, y_max} = grid_points |> Enum.map(&elem(&1, 1)) |> Enum.min_max()

    move(
      {grid, {x_min, x_max, y_min, y_max}},
      {start_pos, start_dir},
      MapSet.new([start_pos]),
      MapSet.new(),
      obstacle
    )
  end

  defp move({grid, {min_x, max_x, min_y, max_y}} = env, {pos, dir}, visited, states, obstacle) do
    next_pos = calculate_next_position(pos, dir)
    current_state = {pos, dir}
    {x, y} = next_pos

    cond do
      current_state in states ->
        {:loop_detected, visited}

      x < min_x or x > max_x or y < min_y or y > max_y ->
        {:out_of_bounds, visited}

      next_pos == obstacle or Map.get(grid, next_pos, "#") == "#" ->
        move(env, {pos, rem(dir + 1, 4)}, visited, MapSet.put(states, current_state), obstacle)

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

  defp part_one(input) do
    input
    |> simulate_movement()
    |> elem(1)
    |> MapSet.size()
  end

  defp part_two({_, grid, {start_pos, _}} = input) do
    grid
    |> Enum.filter(fn {pos, v} -> v == "." and pos != start_pos end)
    |> Enum.map(&elem(&1, 0))
    |> Task.async_stream(
      fn pos ->
        case simulate_movement(input, pos) do
          {:loop_detected, _} -> 1
          _ -> 0
        end
      end,
      max_concurrency: System.schedulers_online() * 2
    )
    |> Enum.map(&elem(&1, 1))
    |> Enum.sum()
  end

  def run(_) do
    data = Timer.measure(fn -> parse_input() end, "Parsing")
    p1_result = Timer.measure(fn -> part_one(data) end, "Part 1")
    p2_result = Timer.measure(fn -> part_two(data) end, "Part 2")
    IO.puts(p1_result)
    IO.puts(p2_result)
  end
end
