from collections import defaultdict

# قراءة عدد الأغاني
N = int(input())

# خريطة لتخزين عدد الأغاني لكل مغني
singer_count = defaultdict(int)

# قراءة المغنيين وعدد الأغاني لكل مغني
max_count = 0
for _ in range(N):
    singer = int(input())
    singer_count[singer] += 1
    max_count = max(max_count, singer_count[singer])

# حساب عدد المغنيين المفضلين
favourite_singers = sum(1 for count in singer_count.values() if count == max_count)

# طباعة النتيجة
print(favourite_singers)


