from django.db import models

# Create your models here.
class Person(models.Model):
	MAN = 0
	WOMAN = 1

	# ユーザーID
	user_id = models.IntegerField()
	# 名前
	name = models.CharField(max_length=128)
	# メールアドレス
	email = models.EmailField()
	# allFlg 通常は0
	all_flg = models.IntegerField()

class Custormer(models.Model):
	# ID
	customer_id = models.IntegerField()
	# 名前
	name = models.CharField(max_length=128)
	# 担当者 Person in Charge
 	pic_id = models.IntegerField()
	# サブ担当者
	sub_pic_id = models.IntegerField()
	# 本番サーバー
	server = models.CharField(max_length=128)
	# テストサーバー
	test_server = models.CharField(max_length=128)
	# 備考
	remarks = models.CharField(max_length=128)

class Forms(models.Model):
	#ID
	form_id = models.IntegerField()
	#

class ToDos(models.Model):
	#ID
	todo_id = models.IntegerField()

	customer_id = models.IntegerField()

	title = models.CharField(max_length=128)

	text = models.CharField(max_length=128)
	# 所要時間
	duration = models.IntegerField()
	# 締切
	deadline = models.DateTimeField()



	

	