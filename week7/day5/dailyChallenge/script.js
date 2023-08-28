function isAnagram(str1, str2) {
    function formatAndSort(str) {
        return str
            .toLowerCase()
            .split('')
            .sort()
            .join('');
    }

    return formatAndSort(str1) === formatAndSort(str2);
}
