# -*- coding: utf-8 -*-

from django import forms
from post.models import Post
from django.core.files.images import get_image_dimensions


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
        w, h = get_image_dimensions(image)
        if image:
            if image.size > 2*1024*1024:
                raise forms.ValidationError(
                    "Image file size should be less than 2MB"
                )
            elif image.size < 10*1024:
                raise forms.ValidationError(
                    "Image file size should be more than 1MB"
                )
            elif w < 400:
                raise forms.ValidationError(
                    "The image is %i pixel wide. It's supposed to be more than 400px" % w
                )
            elif h < 400:
                raise forms.ValidationError(
                    "The image is %i pixel wide. It's supposed to be more than 400px" % h
                )
            return image
        else:
            raise forms.ValidationError(
                'Could not upload image.'
            )

    def clean_slug(self):
        slug = self.cleaned_data['slug']
        if Post.objects.filter(slug=slug).exists():
            raise forms.ValidationError(
                    "The post with %s slug already exist. Please use another slug." % slug
            )
        return slug

    def clean(self):
        pass
