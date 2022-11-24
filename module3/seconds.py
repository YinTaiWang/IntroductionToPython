def to_seconds(hours,minutes,seconds) :
  total_seconds = 0
  total_seconds += seconds
  total_seconds += minutes * 60
  total_seconds += hours * 60 * 60
  return total_seconds