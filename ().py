# coding: utf-8
from carsmaincategory.models import Category
from carsmaincategory.models import Cars
from carsmaincategory.models import Cars
from carsmaincategory.models import TagPost
Category.objects.create(name='Спецтехніка',slug='spectechnik')
Category.objects.create(name='Автобуси',slug='autobus')
Category.objects.create(name='Водний транспорт',slug='water-transport')
Category.objects.create(name='Повітряний транспорт',slug='air-transport')
Category.objects.create(name='Авто будинки',slug='home-on-wheels')
Category.objects.create(name='Сільгосптехніка',slug='silgotechnik')
get_ipython().run_line_magic('save', '()')
TagPost.objects.create(name="Нові",slug="novi")
TagPost.objects.create(name="Уживані",slug="uzivani")
TagPost.objects.create(name="Під пригін",slug="pid_prigin")
TagPost.objects.create(name="Усі типи транспорту",slug="all_types_of_transport")
TagPost.objects.create(name="Vin code",slug="vin-code")
TagPost.objects.create(name="Державинй номер",slug="derzavniy-nomer")
TagPost.objects.create(name="Був у дтп",slug="buv-u-dtp")
TagPost.objects.create(name="Не був у дтп",slug="ne-buv-u-dtp")
TagPost.objects.create(name="Крашена",slug="krashena")
TagPost.objects.create(name="Не крашена",slug="ne-krashena")
TagPost.objects.create(name="Бензин",slug="bensin")
TagPost.objects.create(name="Газ",slug="gas")
TagPost.objects.create(name="Дизель",slug="dizel")
TagPost.objects.create(name="Електро",slug="electro")
TagPost.objects.create(name="Ручна/Механіка",slug="kpp-mechanik")
TagPost.objects.create(name="Автомат",slug="kpp-automatically")
TagPost.objects.create(name="Робот",slug="kpp-robot")
TagPost.objects.create(name="Передній привід",slug="privid-pepedniy")
TagPost.objects.create(name="Передній привід",slug="privid-zdniy")
TagPost.objects.create(name="Повний привід",slug="privid-povniy")