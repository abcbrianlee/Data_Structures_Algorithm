#1507 Reformat Date
#Given string date, convert to yyyy-mm-dd
#ex. date = 20th Oct 2052, output = 2052-10-20.

def reformatDate(date):
    month_mapping = {
        "Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06",
        "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"
    }

    day, month, year = date.split()
    day = day[:-2]
    day = day.zfill(2)
    month = month_mapping[month]

    formatted_date = f"{year}-{month}-{day}"

    return formatted_date

date = "20th Oct 2052"
print("Reformated day is: ", reformatDate(date))

#35 Search Insert Position
#Given a SORTED array of distinct integers and target value, return index if target is found. If not, return index where it should be
#algorithm MUST BE O(log n)
#Ex. nums = [1,3,5,6] target = 5, output = 2

def searchInsert(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left
list1 =[1,3,5,6]
print(searchInsert(list1,5))

#58. Length of Last Word
#Given string (s) consisting of words and spaces, return length of last word in string
#ex. input = "Hello World", output = 5.
#Ex. input = "luffy is still joyboy", output = 6

def lengthOfLastWord(s: str) -> int:
    s = s.strip()
    words = s.split()

    if len(words) == 0:
        return 0
    last_word = words[-1]
    return len(last_word)
string1 = "Luffy is still joyboy"
print("Last word has length of:",lengthOfLastWord(string1))