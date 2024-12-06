# All credit for this module goes to:
# https://github.com/Eoic

defmodule Input do
  defp build_path(cwd, path) do
    cwd
    |> Path.dirname()
    |> Path.join(path)
  end

  def read_lines(cwd, path) do
    cwd
    |> build_path(path)
    |> File.stream!()
    |> Stream.map(&String.trim/1)
  end

  def read_all(cwd, path) do
    cwd
    |> build_path(path)
    |> File.read!()
  end
end
