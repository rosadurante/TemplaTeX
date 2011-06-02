
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

import json

from django.shortcuts import render_to_response

from latex.forms import BasicDocument, Article


def get_basic_datas(BasicDocument):
    return BasicDocument.cleaned_data['type_content']


def get_article_datas(Article):
    title = Article.cleaned_data['title']
    author = Article.cleaned_data['author']
    date = Article.cleaned_data['date']
    abstract = Article.cleaned_data['abstract']
    tableofcontents = Article.cleaned_data['tableofcontents']
    num_sections = Article.cleaned_data['num_sections']
    file_name = Article.cleaned_data['file_name']

    font_size = Article.cleaned_data['font_size']

    return {'title': title, 'author': author, 'date': date,
               'abstract': abstract, 'tableofcontents': tableofcontents,
               'num_sections': range(num_sections), 'file_name': file_name,
               'font_size': font_size}
