from django import forms


class RegistroProveedorForm (forms.Form):
    razon_social = forms.CharField(label='Razón Social', required=True,
                                   max_length=50,
                                   error_messages={
                                       'required': 'La razón social es obligatoria',
                                       'max_length': 'El nombre no puede superar los 50 caracteres'
                                   },
                                   widget=forms.TextInput(attrs={
                                       'placeholder': 'Ingrese la razón social',
                                       'class': 'form-control'
                                   }),
                                   help_text='Queremos colaborar, ingrese la razón social'
                                   )
    nombre = forms.CharField(label='Nombre', required=True,
                             max_length=50,
                             error_messages={
                                 'required': 'El nombre es obligatorio',
                                 'max_length': 'El nombre no puede superar los 50 caracteres'
                             },
                             widget=forms.TextInput(attrs={
                                 'placeholder': 'Ingrese el nombre de la empresa',
                                 'class': 'form-control'
                             }),
                             help_text='Queremos colaborar, ingrese el nombre de la empresa'
                             )
    rep_legal = forms.CharField(label='Representante Legal', required=True,
                                max_length=50,
                                error_messages={
                                    'required': 'El Rep. Legal es obligatorio',
                                    'max_length': 'El Rep- Legal no puede superar los 50 caracteres'
                                },
                                widget=forms.TextInput(attrs={
                                    'placeholder': 'Ingrese al representante legal de la empresa',
                                    'class': 'form-control'
                                }),
                                help_text='Queremos colaborar, ingrese el representante legal de la empresa'
                                )
    rut = forms.CharField(label='RUT', required=True,
                          max_length=13,
                          error_messages={
                                'required': 'El RUT es obligatorio',
                              'max_length': 'El RUT no puede superar los 13 caracteres'
                          },
                          widget=forms.TextInput(attrs={
                              'placeholder': 'Ingrese el RUT de la empresa',
                              'class': 'form-control'
                          }),
                          help_text='Queremos colaborar, ingrese el RUT de la empresa'
                          )
    dirección = forms.CharField(label='Dirección', required=True,
                                 max_length=100,
                                 error_messages={
                                     'required': 'La Dirección es obligatoria',
                                     'max_length': 'La Dirección no puede superar los 100 caracteres'
                                 },
                                 widget=forms.TextInput(attrs={
                                     'placeholder': 'Ingrese la dirección de la empresa',
                                     'class': 'form-control'
                                 }),
                                 help_text='Queremos colaborar, ingrese la dirección de la empresa'
                                 )
    correo = forms.EmailField(label='Email', required=True,
                              max_length=150, min_length=5,
                              error_messages={
                                  'required': 'El email es obligatorio',
                                  'max_length': 'El email no puede superar los 150 caracteres',
                                  'min_length': 'El email debe tener al menos 5 caracteres'
                              },
                              widget=forms.TextInput(attrs={
                                  'placeholder': 'correo@ejemplo.com',
                                  'class': 'form-control'
                              })
                              )
    telefono = forms.CharField(label='Teléfono', required=True,
                               max_length=15, min_length=9,
                               error_messages={
                                   'required': 'El teléfono es obligatorio',
                                   'max_length': 'El teléfono no puede superar los 15 caracteres',
                                   'min_length': 'El teléfono debe tener al menos 9 caracteres'
                               },
                               widget=forms.TextInput(attrs={
                                   'placeholder': 'No olvide ingresar el número de teléfono',
                                   'class': 'form-control'
                               })
                               )
