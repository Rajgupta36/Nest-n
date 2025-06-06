export const formatDate = (input: number | string) => {
  if (!input) {
    return ''
  }

  const date =
    typeof input === 'number'
      ? new Date(input * 1000) // Unix timestamp in seconds
      : new Date(input) // ISO date string

  if (isNaN(date.getTime())) {
    throw new Error('Invalid date')
  }

  return date.toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'short',
    day: 'numeric',
  })
}

export const formatDateRange = (startDate: number | string, endDate: number | string) => {
  const start = typeof startDate === 'number' ? new Date(startDate * 1000) : new Date(startDate)
  const end = typeof endDate === 'number' ? new Date(endDate * 1000) : new Date(endDate)

  if (isNaN(start.getTime()) || isNaN(end.getTime())) {
    throw new Error('Invalid date')
  }

  if (
    start.getTime() === end.getTime() ||
    (start.getFullYear() === end.getFullYear() &&
      start.getMonth() === end.getMonth() &&
      start.getDate() === end.getDate())
  ) {
    return formatDate(startDate)
  }

  const sameMonth = start.getMonth() === end.getMonth() && start.getFullYear() === end.getFullYear()
  const sameYear = start.getFullYear() === end.getFullYear()

  if (sameMonth) {
    // Format as "Month Day - Day, Year" (e.g., "Sep 1 - 4, 2025")
    return (
      `${start.toLocaleDateString('en-US', { month: 'short' })} ` +
      `${start.getDate()} — ${end.getDate()}, ${start.getFullYear()}`
    )
  } else if (sameYear) {
    // Different months but same year (e.g., "Sep 29 - Oct 2, 2025")
    const startMonth = start.toLocaleDateString('en-US', { month: 'short' })
    const endMonth = end.toLocaleDateString('en-US', { month: 'short' })
    const startDay = start.getDate()
    const endDay = end.getDate()
    const year = start.getFullYear()

    return `${startMonth} ${startDay} — ${endMonth} ${endDay}, ${year}`
  } else {
    // Different years (e.g., "Dec 30, 2025 - Jan 3, 2026")
    return `${formatDate(startDate)} — ${formatDate(endDate)}`
  }
}
