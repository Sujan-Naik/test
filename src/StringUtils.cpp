/**
 * @file StringUtils.cpp
 * @brief String utility functions for common text processing operations
 * @author Prototype Development Team
 * @version 1.0
 * @date 2024-01-15
 */

#include <string>
#include <vector>
#include <algorithm>
#include <sstream>

/**
 * @class StringUtils
 * @brief Utility class providing common string manipulation functions
 * 
 * This class contains static methods for performing common string operations
 * such as trimming whitespace, splitting strings, and case conversion.
 * All methods are thread-safe as they don't maintain internal state.
 */
class StringUtils {
public:
    /**
     * @brief Trims whitespace from both ends of a string
     * @param str The input string to trim
     * @return A new string with leading and trailing whitespace removed
     * @note This function does not modify the original string
     */
    static std::string trim(const std::string& str) {
        size_t start = str.find_first_not_of(" \t\n\r");
        if (start == std::string::npos) return "";
        
        size_t end = str.find_last_not_of(" \t\n\r");
        return str.substr(start, end - start + 1);
    }

    /**
     * @brief Splits a string into tokens using a delimiter
     * @param str The input string to split
     * @param delimiter The character to use as delimiter
     * @return Vector of string tokens
     * @warning Empty tokens are included in the result
     */
    static std::vector<std::string> split(const std::string& str, char delimiter) {
        std::vector<std::string> tokens;
        std::stringstream ss(str);
        std::string token;
        
        while (std::getline(ss, token, delimiter)) {
            tokens.push_back(token);
        }
        
        return tokens;
    }

    /**
     * @brief Converts string to uppercase
     * @param str Input string to convert
     * @return New string with all characters in uppercase
     * @see toLowerCase()
     */
    static std::string toUpperCase(const std::string& str) {
        std::string result = str;
        std::transform(result.begin(), result.end(), result.begin(), ::toupper);
        return result;
    }

    /**
     * @brief Converts string to lowercase
     * @param str Input string to convert
     * @return New string with all characters in lowercase
     * @see toUpperCase()
     */
    static std::string toLowerCase(const std::string& str) {
        std::string result = str;
        std::transform(result.begin(), result.end(), result.begin(), ::tolower);
        return result;
    }

private:
    /// @brief Private constructor to prevent instantiation
    StringUtils() = delete;
};