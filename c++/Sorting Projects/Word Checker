// WordChecker.cpp
//
// ICS 46 Winter 2022
// Project #4: Set the Controls for the Heart of the Sun
//
// Replace and/or augment the implementations below as needed to meet
// the requirements.

#include "WordChecker.hpp"



WordChecker::WordChecker(const Set<std::string>& words)
    : words{words}
{
}


bool WordChecker::wordExists(const std::string& word) const
{
    return words.contains(word);
}


std::vector<std::string> WordChecker::findSuggestions(const std::string& word) const
{
    // Nonsensical code because the compiler requires the member variables
    // 'words' to be used somewhere, or else it becomes a warning (which
    // turns into an error).
    std::vector<std::string> wordlist;
    
    
    for (int i =0; i< word.size()-1; i++)
    {
        std::string suggested_word1 = word;
        std::swap(suggested_word1[i], suggested_word1[i+1]);
        if (wordExists(suggested_word1) == true)
        {
            if (std::find(wordlist.begin(), wordlist.end(), suggested_word1) == wordlist.end())
            {
                wordlist.push_back(suggested_word1);
            }
        }
    }
    for (int i =0; i <= word.size(); i++)
    {
        for(int c =0; c < 26 ; c++)
        {
            std::string suggested_word;
            if (i == 0)
            {
                std::string add = upper_chars[c] + word;
                suggested_word += add;
            }
            else if (i < word.size())
            {
                suggested_word += word.substr(0,i);
                suggested_word +=  upper_chars[c];
                suggested_word += word.substr(i);
            }
            else
            {
                std::string add = word + upper_chars[c];
                suggested_word += add;
            }
            if (wordExists(suggested_word) == true)
            {
                if (std::find(wordlist.begin(), wordlist.end(), suggested_word) == wordlist.end())
                {
                    wordlist.push_back(suggested_word);
                }
            }
        }
    }
    std::string suggested_word_d = word;
    for (int i =0; i < word.size(); i++)
    {
        suggested_word_d.erase(0,1);
        if (wordExists(suggested_word_d) == true)
        {
            if (std::find(wordlist.begin(), wordlist.end(), suggested_word_d) == wordlist.end())
            {
                wordlist.push_back(suggested_word_d);
            }
        }
        
    }

    for (int i =0; i <= word.size(); i++)
    {
        for(int c =0; c < 26 ; c++)
        {
            std::string suggested_word_r = word;
            suggested_word_r[i] = upper_chars[c];
            if (wordExists(suggested_word_r) == true)
            {
                if (std::find(wordlist.begin(), wordlist.end(), suggested_word_r) == wordlist.end())
                {
                    wordlist.push_back(suggested_word_r);
                }
            }
        }
    }
    std::string a;
    std::string b;
    for (int i =1; i < word.size(); i++)
    {
        a = word.substr(0,i);
        b = word.substr(i);
        std::string pair = a + " " + b;
        if (wordExists(pair) == true)
        {
            if (std::find(wordlist.begin(), wordlist.end(), pair) == wordlist.end())
            {
                wordlist.push_back(pair);
            }
        }
    }

    return wordlist;
}

