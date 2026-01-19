def longest_common_substring_length(s1, s2):
    n = len(s1)
    m = len(s2)

    dp = [[0] * (m + 1) for _ in range(n + 1)]
    max_len = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):

            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
                max_len = max(max_len, dp[i][j])
            else:
                dp[i][j] = 0

    return max_len


def longest_common_substring(s1, s2):
    n = len(s1)
    m = len(s2)

    dp = [[0] * (m + 1) for _ in range(n + 1)]
    max_len = 0
    end_index = 0   # end position in s1

    for i in range(1, n + 1):
        for j in range(1, m + 1):

            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]

                if dp[i][j] > max_len:
                    max_len = dp[i][j]
                    end_index = i
            else:
                dp[i][j] = 0

    substring = s1[end_index - max_len : end_index]
    return substring, max_len


print(longest_common_substring_length("abcdxyz", "xyzabcd"))  # 4
print(longest_common_substring_length("abc", "ac"))          # 1

sub, length = longest_common_substring("abcdxyz", "xyzabcd")
print(sub, length)   # abcd 4