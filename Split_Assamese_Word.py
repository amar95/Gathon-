import re
print(re.split(r'\s*',"here are some words"))
print(re.split(r'(s*)',"here are some words"))   
print(re.split(r'[ক-চ]','অসমীয়া বয়ন শিল্পৰ এক চানেকী চাওঁক।অামাৰ পৰিয়ালত সংৰক্ষিত ৰজাদিনীয়া পাটৰ কিংখাপৰ মেখেলা'))
print(re.split(r'\s*',"অসমীয়া বয়ন শিল্পৰ এক চানেকী চাওঁক।অামাৰ পৰিয়ালত সংৰক্ষিত ৰজাদিনীয়া পাটৰ কিংখাপৰ মেখেলা "))
