# Problem description can be found at https://leetcode.com/problems/unique-morse-code-words/

# first approach, its an easy problem


class Solution:
    def uniqueMorseRepresentations(self, words):
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        unique = set()
        data = ""
        for word in words:
            for l in word:
                data+=morse[alphabets.index(l)]
            unique.add(data)
            data = ""
        return len(unique)


# Second approach with a bit of code reduction but kind of works the same as above code


class Solution1:
    def uniqueMorseRepresentations(self, words):
        morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                 "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                     'u', 'v', 'w', 'x', 'y', 'z']

        unique = {"".join(morse[alphabets.index(l)] for l in word) for word in words}
        return len(unique)