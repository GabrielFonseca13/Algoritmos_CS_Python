def is_anagram(first_string, second_string):
    if first_string == "" or second_string == "":
        return first_string, second_string, False

    return True


# 4.1 - Retorne True se as palavras passadas por parâmetro forem anagramas;

# 4.2 - Retorne False se as palavras passadas por parâmetro não forem
# anagramas;

# 4.3 - Retorne False se alguma das palavras passadas por parâmetro for uma
# string vazia;

# 4.4 - A função deverá, por meio de análise empírica, se comportar
# (no avaliador remoto em sua Pull Request) como no máximo O(n log n), ou seja,
# com complexidade assintótica linearítmica.

# 4.5 - Retorne True se as palavras passadas forem anagramas sem diferenciar
# maiúsculas e minúsculas.
