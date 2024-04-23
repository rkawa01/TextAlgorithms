def fa_string_matching(text, delta):
    q = 0
    count = 0
    length = len(delta) - 1
    for i in range(0, len(text)):
        if text[i] in delta[q]:
            q = delta[q][text[i]]
            if (q == length):
                count += 1
                # print(f"Przesunięcie {i + 1 - q} jest poprawne")
                # ponieważ przeczytaliśmy (s+q)-ty znak te
        else:
            q = 0
    return count

#Function which generates table of transition values
def transition_table(pattern):
    alphabet = set(pattern)
    result = []
    for q in range(0, len(pattern) + 1):
        result.append({})
        for a in alphabet:
            k = min(len(pattern) + 1, q + 2)
            while True:
                k = k - 1
                # x[:k] - prefiks o długości k
                # x[-k:] - sufiks o długości k
                if (k == 0 or pattern[:k] == (pattern[:q] + a)[-k:]):
                    break
            result[q][a] = k
    return result

delta = transition_table("ada")
print(delta)
