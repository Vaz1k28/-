def common_colors(text):

  irina_colors = text['irina']
  igor_colors = text['igor']


  common_colors = set()
  unique_irina_colors = set()
  unique_igor_colors = set()


  for color in irina_colors:
    if color in igor_colors:
      common_colors.add(color)


  for color in irina_colors:
    if color not in common_colors:
      unique_irina_colors.add(color)


  for color in igor_colors:
    if color not in common_colors:
      unique_igor_colors.add(color)

  common_count = len(common_colors)
  unique_irina_count = len(unique_irina_colors)
  unique_igor_count = len(unique_igor_colors)

  sorted_common_colors = sorted(list(common_colors))
  sorted_unique_irina_colors = sorted(list(unique_irina_colors))
  sorted_unique_igor_colors = sorted(list(unique_igor_colors))

  result = {
      'common': {
          'count': common_count,
          'colors': sorted_common_colors
      },
      'unique_irina': {
          'count': unique_irina_count,
          'colors': sorted_unique_irina_colors
      },
      'unique_igor': {
          'count': unique_igor_count,
          'colors': sorted_unique_igor_colors
      }
  }

  return result


text = {
  'n': 4,
  'm': 3,
  'irina': [0, 1, 10, 9],
  'igor': [1, 3, 0]
}

result = common_colors(text)

print(f"Кількість спільних кольорів: {result['common']['count']}")
print(f"Спільні кольори: {result['common']['colors']}")
print(f"Кількість унікальних кольорів Ірини: {result['unique_irina']['count']}")
print(f"Унікальні кольори Ірини: {result['unique_irina']['colors']}")
print(f"Кількість унікальних кольорів Ігоря: {result['unique_igor']['count']}")
print(f"Унікальні кольори Ігоря: {result['unique_igor']['colors']}")
