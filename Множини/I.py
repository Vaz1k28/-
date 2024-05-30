def find_languages(n, students_languages):
    from functools import reduce

    languages_list = []

    for languages in students_languages:
        languages_set = set(languages)
        languages_list.append(languages_set)

    common_languages = reduce(set.intersection, languages_list)

    all_languages = reduce(set.union, languages_list)

    return len(common_languages), sorted(common_languages), len(all_languages), sorted(all_languages)

n = 3
students_languages = [
    ["Ukrainian", "English"],
    ["English", "Japanese"],
    ["Ukrainian", "Japanese", "English"]
]

common_languages_count, common_languages, all_languages_count, all_languages = find_languages(n, students_languages)

print(common_languages_count)
for language in common_languages:
    print(language)

print(all_languages_count)
for language in all_languages:
    print(language)
