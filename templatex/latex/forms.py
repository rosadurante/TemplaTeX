
# TemplaTex: a generator LaTeX templates.
# Copyright (C) 2011 Rosa Durante <rosunix@gmail.com>
#                    Noelia Sales <noelia.salesmontes@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from django import forms
from django.utils.translation import ugettext_lazy as _


class BasicDocument(forms.Form):
    required_css_class = 'required'
    error_css_class = 'error'

    type_content = forms.MultipleChoiceField(
        required=True,
        label=_('Type of document'),
        choices=(
            ('article', _(u'Article')),
            ),
            # ('book', _(u'Book')),
            # ('presentation', _(u'Presentation'))),
        initial='article',
        widget=forms.SelectMultiple
        )


class Article(forms.Form):
    required_css_class = 'required'
    error_css_class = 'error'

    title = forms.CharField(
        required=True,
        max_length=200,
        widget=forms.TextInput)
    author = forms.CharField(
        required=False,
        max_length=100,
        widget=forms.TextInput)
    abstract = forms.BooleanField(
        required=False)
    tableofcontents = forms.BooleanField(
        required=False)
    num_sections = forms.IntegerField(
        required=True,
        widget=forms.TextInput)
    file_name = forms.CharField(
        required=False,
        max_length=50,
        widget=forms.TextInput)
