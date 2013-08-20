# coding: utf-8

from django.test import TestCase
from eventex.core.models import Contact, Speaker

class ContactManagerTest(TestCase):
    def setUp(self):
        s = Speaker.objects.create(name='Márcio Ramos Corrêa',
        slug='marcio-ramos-correa', url='http://github.com/marciorc')
        s.contact_set.add(Contact(kind='E', value='marcio.ramos.correa@gmail.com'),
        Contact(kind='P', value='14-96186180'), Contact(kind='F', value='14-12345678'))

    def test_emails(self):
        qs = Contact.emails.all()
        expected = ['<Contact: marcio.ramos.correa@gmail.com>']
        self.assertQuerysetEqual(qs, expected)

    def test_phones(self):
        qs = Contact.phones.all()
        expected = ['<Contact: 14-96186180>']
        self.assertQuerysetEqual(qs, expected)

    def test_faxes(self):
        qs = Contact.faxes.all()
        expected = ['<Contact: 14-12345678>']
        self.assertQuerysetEqual(qs, expected)