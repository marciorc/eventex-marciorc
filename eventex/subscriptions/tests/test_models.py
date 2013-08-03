# coding: utf-8
from django.test import TestCase
from django.db import IntegrityError
from datetime import datetime
from eventex.subscriptions.models import Subscription

class SubscriptionTest(TestCase):
	def setUp(self):
		self.obj = Subscription(
		name=u'Márcio Ramos Corrêa',
		cpf='12345678901',
		email='marcio.ramos.correa@gmail.com',
		phone='14-96274121'
		)
	def test_create(self):
		'Subscription must have name, cpf, email, phone'
		self.obj.save()
		self.assertEqual(1, self.obj.id)

	def test_has_created_at(self):
		'Subscription must have automatic created_at'
		self.obj.save()
		self.assertIsInstance(self.obj.created_at, datetime)

	#''' # slide 158
	def test_unicode(self):
		self.assertEqual(u'Márcio Ramos Corrêa', unicode(self.obj))
	#'''

class SubscriptionUniqueTest(TestCase):
	def setUp(self):
		'Create a fist entry to force the colision'
		Subscription.objects.create(name='Márcio Ramos Corrêa', cpf='12345678901', 
									email='marcio.ramos.correa@gmail.com', phone='14-96274121')

	def test_cpf_unique(self):
		'CPF must be unique.'
		s = Subscription(name='Márcio Ramos Corrêa',cpf='12345678901',
						email='marcio557@yahoo.com.br', phone='14-96274121')
		self.assertRaises(IntegrityError, s.save)

	def test_email_unique(self):
		'Email must be unique.'
		s = Subscription(name='Márcio Ramos Corrêa',cpf='00000000011',
						email='marcio.ramos.correa@gmail.com', phone='14-96274121')
		self.assertRaises(IntegrityError, s.save)