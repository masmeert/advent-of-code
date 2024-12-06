defmodule Timer do
  require Logger

  def measure(callback, label) do
    {time_in_microseconds, result} = :timer.tc(callback)
    Logger.info("[#{label}] #{format_time(time_in_microseconds)}.")
    result
  end

  defp format_time(microseconds) when microseconds < 1_000 do
    "#{microseconds} µs"
  end

  defp format_time(microseconds) when microseconds < 1_000_000 do
    milliseconds = microseconds / 1_000
    "#{Float.round(milliseconds, 2)} ms"
  end

  defp format_time(microseconds) do
    seconds = microseconds / 1_000_000
    "#{Float.round(seconds, 2)} s"
  end
end
