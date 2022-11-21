from django.contrib import admin

from .models import Question

'''
# PASO 1
# Creamos una clase administradora
class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']

# Pasamos la clase administradora creada como el segundo argumento de nuestro método para registrar
admin.site.register(Question, QuestionAdmin)
'''

'''
# PASO 2
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Información de fecha y hora', {'fields': ['pub_date']}),
    ]

admin.site.register(Question, QuestionAdmin)
'''

'''
# PASO 3
from .models import Choice
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Información de fecha y hora', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
'''

'''
# PASO 4
from .models import Choice
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Información de fecha y hora', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
'''

'''
# PASO 5
from .models import Choice
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Información de fecha y hora', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    # Agregamos la opción list_display que nos permite mostrar una lista de campos como columnas
    list_display = ('question_text', 'pub_date', 'was_published_recently')

admin.site.register(Question, QuestionAdmin)
'''

# En el PASO 6 modificaremos la columna WAS PUBLISHED RECENTLY en models.py

'''
# PASO 7
from .models import Choice
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Información de fecha y hora', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # Añadimos una columna para filtrar por fecha de publicación
    list_filter = ['pub_date']

admin.site.register(Question, QuestionAdmin)
'''

# PASO 8
from .models import Choice
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # Agregamos una entrada para buscar la pregunta ingresando texto
    search_fields = ['question_text']
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Información de fecha y hora', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']

admin.site.register(Question, QuestionAdmin)

# Para el paso 9 crearemos el directorio templates en la raíz del proyecto y editaremos settings.py

