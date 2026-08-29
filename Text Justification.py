class Solution:
    def fullJustify(self, words, maxWidth):
        result = []
        i = 0

        while i < len(words):
            line = []
            line_length = 0

            while i < len(words) and line_length + len(words[i]) + len(line) <= maxWidth:
                line.append(words[i])
                line_length += len(words[i])
                i += 1

            spaces = maxWidth - line_length

            if i == len(words) or len(line) == 1:
                result.append(" ".join(line) + " " * (maxWidth - (line_length + len(line) - 1)))
            else:
                gaps = len(line) - 1
                space = spaces // gaps
                extra = spaces % gaps

                text = ""

                for j in range(gaps):
                    text += line[j]
                    text += " " * (space + (1 if j < extra else 0))

                text += line[-1]
                result.append(text)

        return result
