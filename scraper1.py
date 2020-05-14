from facebook_scraper import get_posts
import csv

list1 = []
temp = []
temp.append("post_id")
temp.append("text")
temp.append("time")
temp.append("likes")
temp.append("comments")
temp.append("shares")
list1.append(temp)
count = 0;
print("flag1")
for post in get_posts('vidhi.bekaroo',pages = 50):
	list2 = []
	count+=1;
	print("count - ",count)
	print(post['post_id'][:])
	list2.append(post['post_id'][:])
	list2.append(post['text'][:])
	print(post['time'])
	list2.append(post['time'])
	list2.append(post['likes'])
	list2.append(post['comments'])
	list2.append(post['shares'])
	list1.append(list2)
	print("End - 1\n")

with open('train_test_1.csv','w') as writeFile:
	writer = csv.writer(writeFile)
	writer.writerows(list1)

writeFile.close()
print("flag2")
