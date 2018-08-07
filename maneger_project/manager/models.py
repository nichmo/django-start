from django.db import models

# Create your models here.
class Person(models.Modal):
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
	server = models.CharField()
	# テストサーバー
	test_server = models.CharField()
	# 備考
	remarks = models.CharField()

class Forms(models.Modal):
	#ID
	form_id = models.IntegerField()

	

	