# -*- coding: utf-8 -*-

from django import forms
from post.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ()
        widgets_attrs = {
            'title': forms.TextInput(attrs={
                'class': 'ui container',
                'placeholder': 'Укажите название'
            }),
            'slug': forms.URLInput(attrs={
                'class': 'ui container',
            }),
            'category': forms.Select(attrs={
                'class': 'ui container',
            }),
            'create_at': forms.TextInput(attrs={
                'class': 'ui container',
            }),
            'picture': forms.FileInput(attrs={
                'class': 'ui container',
            }),
            'text': forms.Textarea(attrs={
                'class': 'ui container',
            }),
            'display': forms.CheckboxInput(attrs={
                'class': 'ui container',
            }),
            'like': forms.NumberInput(attrs={
                'class': 'ui container',
            }),
            'dislike': forms.NumberInput(attrs={
                'class': 'ui container',
            }),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 8:
            raise forms.ValidationError(
                'Title length should be at least 8 symbols'
            )
        return title

    def clean_picture(self):
        image = self.cleaned_data.get('picture', False)
        if image:
            if image._size > 1024:
                raise forms.ValidationError(
                    'Image file too large (> 4MB)'
                )
            return image
        else:
            raise forms.ValidationError(
                'Could not upload image.'
            )

    def clean_slug(self):
        pass

    def clean(self):
        pass
